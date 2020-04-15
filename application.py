from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://www.mb103.com/lnk.asp?o=17246&c=918273&a=279700&k=ECA558BF696C3C712A8D8B70D50EA035&l=18606", code=302)
