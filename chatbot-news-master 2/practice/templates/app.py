import json
from urllib.request import urlopen
from random import random, shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = Flask(__name__)

@app.route("/")
# if users vist home page,  
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():

    with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
        html = res.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    item = soup.select("item")
    # If the name selected by the .select (in this case "item") is included the any part of the class and id, they would be reflected

    shuffle(item)
    item[0]
    print (item)

    return json.dumps({
        "content": item.find ("title").string,
        "link" : item.find ("rdf:about")
        })
        
    
if __name__ =="__main__":
    app.run(debug=True, port=5003)