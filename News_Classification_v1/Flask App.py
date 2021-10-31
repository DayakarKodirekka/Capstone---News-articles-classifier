from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_data_from_url import get_data


clf = load("d:\\PG_IIIT-HYD\\Capstone\\Capstone---News-articles-classifier\\News_Classification_v1\\text_classification_svc.joblib")
tfidf = load("d:\\PG_IIIT-HYD\\Capstone\\Capstone---News-articles-classifier\\News_Classification_v1\\transformer.joblib")

def requestResults(url):
    #train_df = get_data(url)
    #print(train_df.head())
    train_df = [url]
    print(train_df)
    pred = clf.predict(tfidf.transform(train_df))
    return url +"category is" + str(pred)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST', 'GET'])
def get_data_UI():
    if request.method == 'POST':
        print("Hellow World..................")
        message = request.form['message']
        print(message)
        if message.strip() == "":
            return "<xmp>" + "Enter valid URL" + " </xmp> "
        #elif len(message.split()) < 5:
            #result=["Please Enter more words"]
        else:
            print(message)
            return "<xmp>" + str(requestResults(message)) + " </xmp> "
            


#@app.route('/success/<name>')
#def success(name):
 #   return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)