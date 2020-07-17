# 2020-crime-predictions

# Overview
Se quiere correr un modelo de Aprendizaje Automático (Decision Tree) para predecir crímenes en San Francisco (~870.000 registros).

Primero, se utiliza python, con su librería pandas para el pre-procesamiento de la data, y luego, SKlearn para computar un modelo de machine learning (decision tree). 

Para esto, se confecciona un modelo acorde al problema y se utiliza un computador intel core i7 8700 3600 Mhz, con 6 núcleos físicos y 12 virtuales. Se obtuvieron las siguientes métricas: <br>
Tiempo de Pre-procesamiento    : 52 segundos <br>
Tiempo de computo del modelo   : 10 minutos, 13 segundos <br>
Accuracy                       : 0,8 <br>

El proyecto consiste en responder la pregunta: ¿Esto se podría hacer más rápido considerando lo aprendido en este curso?
Para lo anterior, se pre-procesará la data y se computará el mismo modelo con PySpark

# Data
Contenido                        : Registros de crímenes en San Francisco, US <br>
Formato                          : Texto separado por comas (.csv) <br>
Cantidad de Registros            : 878.050, cada registro representa un crímen ocurrido <br>
Cantidad de Atributos            : 10. <br>
Atributos                        : id, categoría, descripción, día de la semana, distrito, dirección, latitudes, longitudes, fecha, resolución. <br>

# Methods
Para llevar a cabo el proyecto se utilizó Spark, especificamente su librería ML la cual está diseñada para implementar modelos de Machine Learning. Como, en esencia, se quería ver el impacto en la ejecución debido a un procesamiento de grandes volúmenes de datos, se aprovechó que Spark proveía tal librería para implementar el Decision Tree. La labor entonces, consistía en ocupar las herramientas de Spark y lo visto en el curso, para adaptar el dataset al input que se necesitaba para correr el modelo.

En primera instancia se limpiaron los datos para dejar las variables importantes para el objetivo del proyecto. Se crearon nuevas columnas (como 'day' y 'month') haciendo split en la columna 'fecha'; se filtraron valores y se asignaron etiquetas a diferentes categorías. No hubo mayores problemas en esta sección debido a que tenía una dificultad y ejecución similar a los laboratorios.

Tras ello, se realizó un proceso de One-hot Encoding que transformaba variables categóricas a binarias. En esta sección se presentaron las mayores complicaciones del proyecto debido al desconocimiento de la librería. En esencia, se utilizaron los métodos StringIndexer y VectorAssembler para llevar los datos de cada fila a un 'vector' que mantiene la información, el cual, al aplicarle one-hot Encoding, los codificaba a variables binarias.

Por otra parte, ML introduce el concepto de Pipeline, el cual corresponde a un método que se encarga de encadenar las transformaciones de los datos para mantener la consistencia y poder obtener el dataframe que necesita el clasificador. Por lo que, en esencia, se procesaron los datos de modo que cuadraran con los tipos que exigía el método DecisionTreeClassifier. Más detalles se pueden revisar en en el script [decisionTree.py](https://github.com/cc5212/2020-crime-predictions/blob/master/decisionTree.py).

Finalmente, se implementó el modelo junto con un 'Evaluator' (incluido en la librería) para usar como métrica de precisión y comparar los resultados del proyecto.


TODO: Detail the methods used during the project. Provide an overview of the techniques/technologies used, why you used them and how you used them. Refer to the source-code delivered with the project. Describe any problems you encountered.

# Results
Se obtuvieron las siguientes métricas utilizando PySpark:

Tiempo de Pre-procesamiento    : 2 segundos <br>
Tiempo de computo del modelo   :18 segundos <br>                            
Accuracy                       :  0,793     <br>

Si se comparan con las métricas obtenidas utilizando pandas para el pre-procesamiento y SKlearn para el computo de los modelos, se obtiene una mejora de un 96% en la rápidez del pre-procesamiento (con respecto a pandas) y una mejora de un 97% de la rapidez de computo con respecto a SKlearn.

# Conclusion
PySpark disminuye el tiempo de computo del modeloen un 97% con respecto a SkLearn, se mantiene un accuracy similar al de Sklearn. PySpark mantiene un accuracy similar al de Sklearn
El pre-procesamiento de datos con PySpark es más rapido que con Pandas. Además, no requiere mayor utilización de líneas de código para su implementación.
Si es que no se dispone de tiempo o computadores con buena capacidad de procesamiento, utilizar Spark puede ayudar a cumplir ciertas tareas, aunque con restricciones en la variedad de herramientas para la implementación de estos modelos, como la cusmomización de los mismos. 

# Appendix
TODO: You can use this for key code snippets that you don't want to clutter the main text.
