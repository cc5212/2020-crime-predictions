# 2020-crime-predictions

# Overview
Se quiere correr un modelo de Aprendizaje Automático (Decision Tree) para predecir crímenes en San Francisco (~870.000 registros).

Primero, se utiliza python, con su librería pandas para el pre-procesamiento de la data, y luego, SKlearn para computar un modelo de machine learning (decision tree). 

Para esto, se confecciona un modelo acorde al problema y se utiliza un computador intel core i7 8700 3600 Mhz, con 6 núcleos físicos y 12 virtuales. Se obtuvieron las siguientes métricas:
Tiempo de Pre-procesamiento    : 52 segundos <br>
Tiempo de computo del modelo   : 10 minutos, 13 segundos
Accuracy                       : 0,8

El proyecto consiste en responder la pregunta: ¿Esto se podría hacer más rápido considerando lo aprendido en este curso?
Para lo anterior, se pre-procesará la data y se computará el mismo modelo con PySpark

# Data
Contenido                        : Registros de crímenes en San Francisco, US
Formato                          : Texto separado por comas (.csv) 
Cantidad de Registros            : 878.050, cada registro representa un crímen ocurrido      
Cantidad de Atributos            : 13. 
Atributos                        : id, categoría, descripción, día de la semana, distrito, dirección, latitudes, longitudes, fecha, resolución.

# Methods
TODO: Detail the methods used during the project. Provide an overview of the techniques/technologies used, why you used them and how you used them. Refer to the source-code delivered with the project. Describe any problems you encountered.

# Results
TODO: Detail the results of the project. Different projects will have different types of results; e.g., run-times or result sizes, evaluation of the methods you're comparing, the interface of the system you've built, and/or some of the results of the data analysis you conducted.

# Conclusion
TODO: Summarise main lessons learnt. What was easy? What was difficult? What could have been done better or more efficiently?

# Appendix
TODO: You can use this for key code snippets that you don't want to clutter the main text.
