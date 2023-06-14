import pandas as pd
# from cuBERTopic import gpu_BERTopic
from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

subredditName = "womenshealth"
df = pd.read_csv("CommentsInTopPosts_" + subredditName + ".csv")
docs = df['post_comments']

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(docs)


# subredditName = "twoxchromosomes"
# df = pd.read_csv("CommentsInTopPosts_" + subredditName + ".csv")
# df = df['post_comments']
# gpu_topic = BERTopic(vocab_file=df)
# topics_gpu, probs_gpu = gpu_topic.fit_transform(docs)
topic_model.get_topic_info()
topic_model.get_topic(1)
# timestamps = trump.date.to_list()
# tweets = trump.text.to_list()
# topics_over_time = topic_model.topics_over_time(tweets, topics, timestamps, nr_bins=20)
# topic_model.visualize_topics_over_time(topics_over_time, top_n_topics=6)
topic_model.save("model_" + subredditName)
