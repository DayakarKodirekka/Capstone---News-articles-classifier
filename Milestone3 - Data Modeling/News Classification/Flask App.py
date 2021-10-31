from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_data_from_url import get_data


pipeline = load("text_classification.joblib")


def requestResults(url):
    train_df = get_data(url)
    pred = pipeline.predict(train_df)
    return url +"category is" + str(pred)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        message = request.form['message']
        if message.strip() == "":
            result=["Please Enter a Headline"]
        elif len(message.split()) < 5:
            result=["Please Enter more words"]
        else:
            return redirect(url_for('success', name=message))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)