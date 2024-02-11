from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

def train_model(data):
    spark = SparkSession.builder \
        .appName("RecommendationModelTraining") \
        .getOrCreate()
    
    spark_df = spark.createDataFrame(data)
    
    train_data, test_data = spark_df.randomSplit([0.8, 0.2], seed=42)
    feature_cols = [col for col in spark_df.columns if col != 'target']
    assembler = VectorAssembler(inputCols=feature_cols, outputCol='features')
    lr = LogisticRegression(featuresCol='features', labelCol='target')
    
    pipeline = Pipeline(stages=[assembler, lr])
    model = pipeline.fit(train_data)
    
    evaluation = model.transform(test_data)
    accuracy = evaluation.filter(evaluation.target == evaluation.prediction).count() / evaluation.count()
    spark.stop()
    
    return model, accuracy
