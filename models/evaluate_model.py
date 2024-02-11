from pyspark.sql import SparkSession
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

def evaluate_model(model, data):
    spark = SparkSession.builder \
        .appName("ModelEvaluation") \
        .getOrCreate()

    spark_df = spark.createDataFrame(data)
    evaluator = MulticlassClassificationEvaluator(labelCol="target", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(model.transform(spark_df))
    
    spark.stop()
    
    return accuracy
