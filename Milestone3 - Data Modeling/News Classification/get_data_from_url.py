# Get Details from the URL provided in UI
import requests
import time
import json
import pandas as pd


#url = "https://free-news.p.rapidapi.com/v1/search"

#querystring = {"q":"entertainment","lang":"en"}

#headers = {
#    'x-rapidapi-host': "free-news.p.rapidapi.com",
 #   'x-rapidapi-key': "b593c9a319msh312e606d9a8f636p1ac2a1jsn57d0059e91f6"
 #   }

#response = requests.request("GET", url, headers=headers, params=querystring)

def get_data(url):

    try:
        querystring = {"q":"","lang":"en"}
        headers = {
            'x-rapidapi-host': "free-news.p.rapidapi.com",
            'x-rapidapi-key': "b593c9a319msh312e606d9a8f636p1ac2a1jsn57d0059e91f6"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
         
        json_string = response.text
        stud_obj = json.loads(json_string)

        news = []
        for item in stud_obj['articles']:
            item_title = {}
            item_title['title'] = item['title']
            item_title['link'] = item['link']
            item_title['topic'] = item['topic']
            item_title['pub_date'] = item['published_date']
            item_title['summary'] = item['summary']
            item_title['author'] = item['author']
            news.append(item_title)
            
            df = pd.DataFrame(news,columns=['title','summary','link','pub_date','topic','author'])
            #train_df = spark.createDataFrame(df)
            return df
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)