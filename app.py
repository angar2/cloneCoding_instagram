from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.campProject

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/comment', methods=['GET'])
def listing():
    comments = list(db.instargramComments.find({}, {'_id': False}))
    return jsonify({'comments':comments})

## API 역할을 하는 부분
@app.route('/comment', methods=['POST'])
def saving():
    userReceive = request.form['userGive']
    commentReceive = request.form['commentGive']

    doc = {
        'user': userReceive,
        'comment': commentReceive
    }
    db.instargramComments.insert_one(doc)

    return jsonify()

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)