from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier

# Start Session
spark = SparkSession.builder.master('local[*]') \
    .appName('projectData') \
    .getOrCreate()

# Set data
data = spark.read.csv('./data/crime.csv', header=True)

# --------------- #
# DATA PROCESSING #
# --------------- #
# Add Label Column: 1 to Efective , 2 to Non Efective , 3 to Juvenile
data = data.withColumn('CatResolution',
                       when((data['Resolution'] == 'NONE') |
                            (data['Resolution'] == 'UNFOUNDED') |
                            (data['Resolution'] == 'EXCEPTIONAL CLEARANCE') |
                            (data['Resolution'] == 'DISTRICT ATTORNEY REFUSES TO PROSECUTE') |
                            (data['Resolution'] == 'NOT PROSECUTED') |
                            (data['Resolution'] == 'COMPLAINANT REFUSES TO PROSECUTE'), 1).
                       when((data['Resolution'] == 'ARREST, BOOKED') |
                            (data['Resolution'] == 'ARREST, CITED') |
                            (data['Resolution'] == 'LOCATED') |
                            (data['Resolution'] == 'PROSECUTED FOR LESSER OFFENSE') |
                            (data['Resolution'] == 'PSYCHOPATHIC CASE') |
                            (data['Resolution'] == 'PROSECUTED BY OUTSIDE AGENCY'), 2).otherwise(3))

# Add Hour Column splitting Time
split_Time = split(data['Time'], ':')
data = data.withColumn('Hour', split_Time.getItem(0))

# Add Day and Month Column Splitting Date
split_Date = split(data['Date'], '-')
data = data.withColumn('Day', split_Date.getItem(2))
data = data.withColumn('Month', split_Date.getItem(1))

# Cast columns string -> double/int
data = data.withColumn("X", data['X'].cast("double"))
data = data.withColumn("Y", data['Y'].cast("double"))
data = data.withColumn("Day", data['Day'].cast("int"))
data = data.withColumn("Month", data['Month'].cast("int"))
data = data.withColumn("Hour", data['Hour'].cast("int"))

# Filter useless columns
columnsToDrop = ['id', 'Descript', 'PdDistrict', 'Address', 'Dates', 'Time', 'Date', 'dia_num', 'Resolution']
data = data.drop(*columnsToDrop)

# ----------------------------------------------#
# Now, the dataset is ready to one-hot encoding #
# ----------------------------------------------#

# Apply one-hot encoders needs to index categorical values. Then, for each category encode data and adds in stage list.
# Finally, adds numeric variables to new dataset.

# Set categorical variables (Strings)
categoricalColumns = ["Category", "DayOfWeek"]
stages = []  # stages is a list to merge in pipeline model
for categoricalCol in categoricalColumns:
    # Category Indexing with StringIndexer
    stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol + "Index")
    # Use OneHotEncoder to convert categorical variables into binary SparseVectors
    encoder = OneHotEncoder(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
    # Add stages. These are not run here, but will run all at once later on.
    stages += [stringIndexer, encoder]

# Convert CatResolution into label target to predict
label_stringIdx = StringIndexer(inputCol="CatResolution", outputCol="label")
stages += [label_stringIdx]

# Transform all features (numeric values) into a vector using VectorAssembler
numericCols = ["X", "Y", "Hour", "Day", "Month"]

# Assemble all data in stages
assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler]

print("Data before one-hot encoding")
data.show()
print("----------------------------")

# Pipeline model chains stages data to can apply a machine learning model
pipeline = Pipeline(stages=stages)
pipelineModel = pipeline.fit(data)
data = pipelineModel.transform(data)

print("Data after one-hot encoding. Feature and Label contains all the information to apply a classificatioin model")
print("Features column contains a 'vector' of indexes for categorical variables")
print("Labels: 0 -> Efective , 1 -> Non-efective, 2 -> Juvenile")
data.show()
print("----------------------------")


# ---------------------------------------- #
#         DECISION TREE CLASSIFIER         #
# ---------------------------------------- #

# Split dataset in training and testing data
trainingData, testData = data.randomSplit([0.7, 0.3], seed=2020)


# Create initial Decision Tree Model
dt = DecisionTreeClassifier(featuresCol='features', labelCol='label', maxDepth=3)

# Fit it
dtModel = dt.fit(trainingData)

# Predict
predictions = dtModel.transform(testData)
predictions.show()

# Results
confusionMatrix = predictions.groupBy("label", "prediction").count()
confusionMatrix.show()

# Use evaluator to compute accuracy level
evaluator = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Accuracy percentage: %g " % accuracy)
