import dlt

@dlt.table
def transform():
  return spark.range(10)