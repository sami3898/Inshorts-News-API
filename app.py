#Coded by Sumanjay on 29th Feb 2020
from flask import Flask, request, jsonify
from inshorts import getNews
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"
CORS(app)

@app.route('/')
def home():
    return 'News API is UP!<br><br>A part of <a href="https://t.me/sjprojects">Sj Projects</a>'

@app.route('/news')
def news():
    if request.method == 'GET':
        category = request.args.get("category")
        limit = request.args.get("max_limit")
        if not category:
            return jsonify({
                "error": "please add category in query params"
            }), 404
        return jsonify(getNews(category, limit)), 200

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=9000,use_reloader=True)
