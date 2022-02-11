import pyspark
import numpy as np
import pandas as pd

spark = pyspark.sql.SparkSession.builder.getOrCreate()

data = np.array('python', 'sql', 'c', 'c#', 'java', 'machine langauge', 'html', 'css')
languages = pd.DataFrame(data, columns = ['Languages'])

df = spark.createDataFrame(languages)
df