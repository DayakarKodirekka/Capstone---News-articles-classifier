import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "news", 1: "entertainment", 2: "sports", 3: "business", 4: "Tech"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
            "title": d.title,
            "summary": d.summary,
            "pub_date": d.pub_date,
            "link": d.link,
            "topic": d.topic,
        }
        for d in data
    ]

    return processed
