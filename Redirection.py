from flask import Flask,redirect,url_for
import time
app=Flask(__name__)

@app.route("/")
@app.route(("/home"))
def Home():
    return "<h1><center>Welcome to the Hmraaaaaa Page</center></h1>"

@app.route("/pass")
def passed():
    return "<h1>Congrats You have passed </h1>"

@app.route("/fail")
def Fail():
    return "<h2><center> Padhlo Madarchod </center></h>"

@app.route("/score/<name>/<int:per>")
def score(name,per):
    if per>60:
        time.sleep(1)
        return redirect(url_for("passed"))
    else:
        time.sleep(1)
        return redirect(url_for("Fail"))

@app.route("/Score")
def scoree():
    return "<h1><center>Naam or percentage kon batayega</center></h1>"

if __name__== "__main__":
    app.run(debug=True )
    