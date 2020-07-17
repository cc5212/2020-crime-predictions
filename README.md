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
TODO: Detail the methods used during the project. Provide an overview of the techniques/technologies used, why you used them and how you used them. Refer to the source-code delivered with the project. Describe any problems you encountered.

# Results
Se obtuvieron las siguientes métricas utilizando PySpark:

Tiempo de Pre-procesamiento    : 2 segundos <br>
Tiempo de computo del modelo   :18 segundos <br>                            
Accuracy                       :  0,793     <br>

Si se comparan con las métricas obtenidas utilizando pandas para el pre-procesamiento y SKlearn para el computo de los modelos, se obtiene una mejora de un 96% en la rápidez del pre-procesamiento (con respecto a pandas) y una mejora de un 97% de la rapidez de computo con respecto a SKlearn.

# Conclusion
PySpark disminuye el tiempo de computo del modeloen un 97% con respecto a SkLearn, se mantiene un accuracy similar al de Sklearn.
PySpark mantiene un accuracy similar al de Sklearn
El pre-procesamiento de datos con PySpark no es más engorroso que con pandas. Además, Es más rápido de computar.
Si es que no se dispone de tiempo o computadores con buena capacidad de procesamiento, utilizar Spark puede ayudar

# Appendix
TODO: You can use this for key code snippets that you don't want to clutter the main text.
