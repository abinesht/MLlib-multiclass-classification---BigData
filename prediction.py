from pyspark.ml import Pipeline # pipeline to transform data
from pyspark.sql import SparkSession # to initiate spark
from pyspark.ml.feature import RegexTokenizer, StopWordsRemover,Word2Vec
from pyspark.ml import PipelineModel
from pyspark.ml.classification import LogisticRegressionModel

spark = SparkSession.builder.appName("song_classfier")\
                            .getOrCreate()

# regexTokenizer = RegexTokenizer(inputCol="lyrics", outputCol="words", pattern="\\W")
# # to remove stop words like is, the, in, etc.
# stopwords_remover = StopWordsRemover(inputCol="words", outputCol="stopwords_remove")
# # bag of words count
# word2Vec = Word2Vec(vectorSize=100, minCount=0, inputCol="stopwords_remove", outputCol="features")

loaded_pipeline = PipelineModel.load("./pipeline")
# pipeline = Pipeline(stages=[regexTokenizer, stopwords_remover, word2Vec])

model = LogisticRegressionModel.load("./model")

# Now you can use the loaded model for predictions

def predict_genre(lyrics):
    genres = ['Pop', 'Blue', 'Chill', 'Jazz', 'Hip hop', 'Country', 'Rock', 'Soul']
    new_df = spark.createDataFrame([(lyrics,)], ["lyrics"])

    pipe_new = loaded_pipeline.transform(new_df)
    predictions = model.transform(pipe_new)
    # Make predictions
    probabilities = predictions['probability']
    predicted_genre = genres[int(predictions['prediction'])]
    return predicted_genre, probabilities
