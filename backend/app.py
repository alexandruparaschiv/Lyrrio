from flask import Flask,jsonify, make_response,Response,json
from flask import request
from flask_cors import CORS
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import jsonify
import os

app = Flask(__name__)
CORS(app)
port = int(os.environ.get("PORT",5000))
clf = pickle.load(open('lyrics_classifier.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl','rb'))

@app.route('/predict',methods=['GET','POST'])
def hello_world(**data):
    data = request.get_json(force=True)
    lyrics = data['lyrics']
    if not lyrics:
        return None;
    song_lyrics = vectorizer.transform(pd.Series(lyrics))
    genre = clf.predict(song_lyrics)
    probs = clf.predict_proba(song_lyrics)
    headers = {"Content-Type": "application/octet-stream","Content-Disposition": "attachment; filename=foobar.json"}
    return (json.dumps({"genre": genre[0],"probabilities":list(probs[0])}), 200, headers)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=port)
