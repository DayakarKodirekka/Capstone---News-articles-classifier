from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_data_from_url import get_data, get_article_summary


clf = load("text_classification_svc.joblib")
tfidf = load("transformer.joblib")

def requestResults(url):
    url=url.strip()
    if "http" in url and len(url.split()) <2:
        text=get_article_summary(url)
    else:
        text=url
    print(text)
    pred = clf.predict(tfidf.transform([text]))
    
    print(pred)
    return "category is" + str(pred)


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