from flask import Flask,jsonify, make_response,Response,json
from flask import request
from flask_cors import CORS
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import jsonify 

app = Flask(__name__)
CORS(app)
clf = pickle.load(open('lyrics_classifier.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl','rb'))

@app.route('/predict',methods=['GET','POST'])
def hello_world(**data):
    data = request.get_json(force=True)
    lyrics = data['lyrics']
    x_train = vectorizer.transform(pd.Series(lyrics))
    genre = clf.predict(x_train)
    probs = clf.predict_proba(x_train)
    print(type(probs[0]))
    print(type(genre[0]))
    print(genre[0],probs[0])
    #resp = (genre[0],probs[0])
    #d = jsonify(dict(genre=genre[0],probabilities=probs[0]))
    #return make_response(jsonify(d),200)
    #return Response(d,content_type="application/json; charset=utf-8" )
    #data = {'name': 'davidism'}
    #return jsonify(data)
    headers = {"Content-Type": "application/octet-stream","Content-Disposition": "attachment; filename=foobar.json"}
    return (json.dumps({"genre": genre[0],"probabilities":list(probs[0])}), 200, headers)

app.run(debug=True)
