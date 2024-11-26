# spark_app.py
from pyspark.sql import SparkSession

# Criar uma sessão Spark
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

# Código de exemplo: contar números de 1 a 100
data = range(1, 101)
distData = spark.sparkContext.parallelize(data)
count = distData.count()

print(f"Total count: {count}")

# Finalizar a sessão Spark
spark.stop()
