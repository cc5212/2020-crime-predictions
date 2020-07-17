import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

crime = pd.read_csv('./data/crime.csv')
print(crime.head())

#Se eliminan filas que contienen otliers en las variables de coordenadas
print(pd.value_counts(crime['Y'] > 50))
crime = crime.drop(crime[crime['Y']>=50].index)
print(pd.value_counts(crime['Y'] > 50))
crime.reset_index();
crime = crime.drop(['id'], axis=1)
crime.tail(3)
crime['Time'] = crime['Time'].str.split(':').str.get(0).astype('str')
crime['Time'] = crime['Time'].astype(int)
pd.value_counts(crime['Category']).head(3)
crime_top_category = crime[(crime['Category'] == 'LARCENY/THEFT') | (crime['Category'] == 'OTHER OFFENSES') | (crime['Category'] == 'NON-CRIMINAL')]
crime_top_category['cat_num'] = crime_top_category['Category'];
crime_top_category['cat_num'] = crime_top_category['cat_num'].replace({'LARCENY/THEFT':1,'OTHER OFFENSES':2,'NON-CRIMINAL':3});
pd.value_counts(crime_top_category['cat_num']).head(3)

#Recordando que la hora en que ocurrió el incidente está almacenada como 'Time', se crean las columnas, mes y dia,
# que indican el número del mes del año y día del mes correspondiente
crime['Dia'] = crime['Date'].str.split('-').str.get(2).astype('str')
crime['Mes'] = crime['Date'].str.split('-').str.get(1).astype('str')

#Se pre-procesa la data para poder utilizar clasificadores
np.unique(crime['Resolution'], return_counts = True)
condiciones = [(crime['Resolution'] == 'NONE') | (crime['Resolution'] == 'UNFOUNDED') | (
            crime['Resolution'] == 'EXCEPTIONAL CLEARANCE') | (
                           crime['Resolution'] == 'DISTRICT ATTORNEY REFUSES TO PROSECUTE') | (
                           crime['Resolution'] == 'NOT PROSECUTED') | (
                           crime['Resolution'] == 'COMPLAINANT REFUSES TO PROSECUTE'),
               (crime['Resolution'] == 'ARREST, BOOKED') | (crime['Resolution'] == 'ARREST, CITED') | (
                           crime['Resolution'] == 'LOCATED') | (
                           crime['Resolution'] == 'PROSECUTED BY OUTSIDE AGENCY') | (
                           crime['Resolution'] == 'PROSECUTED FOR LESSER OFFENSE') | (
                           crime['Resolution'] == 'PSYCHOPATHIC CASE'),
               (crime['Resolution'] == 'CLEARED-CONTACT JUVENILE FOR MORE INFO') | (
                           crime['Resolution'] == 'JUVENILE ADMONISHED') | (
                           crime['Resolution'] == 'JUVENILE BOOKED') | (crime['Resolution'] == 'JUVENILE CITED') | (
                           crime['Resolution'] == 'JUVENILE DIVERTED')]

elecciones = np.array(('No_efectiva', 'Efectiva', 'Juvenil'), dtype="str")
crime["CatResolution"] = np.select(condiciones, elecciones, -1)
crime["CatResolution"].head(20)
crime_catres = crime

crime_catres['catRes'] = crime_catres['CatResolution']
crime_catres['catRes'] = crime_catres['catRes'].replace({'Efectiva':1,'Juvenil':2,'No_efectiva':3})
crime_catres.catRes.describe()

#Como la variable "Category", que integra los features, es categorica nominal, debe ser transformada a variables dummy
# para que pueda ser procesada por sklearn, entonces se utilizan funciones de pandas.
categorydum = crime["Category"].str.get_dummies()
crime_copy_before_one_hot = crime.copy()
crime = pd.concat([crime, categorydum], axis=1).drop(["Category"], axis=1)

#Se realiza el mismo procedimiento para la variable "DayOfWeek"
daydum = crime["DayOfWeek"].str.get_dummies()
crime = pd.concat([crime, daydum], axis=1).drop(["DayOfWeek"], axis=1)
crime.head()

#Se crean los conjuntos X e Y
X = crime.drop(['Descript', 'catRes', 'PdDistrict', 'Address','Date', 'Resolution', 'Dates', 'CatResolution', 'dia_num'], axis = 1)
y = crime["CatResolution"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train.head(10)

#Considerando la gran cantidad de variables categóricas se utiliza un modelo Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
clf.score(X_test, y_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


