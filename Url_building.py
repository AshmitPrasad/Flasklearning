from flask import Flask,redirect,url_for
import time
app=Flask(__name__)

@app.route("/")
@app.route(("/home"))
def Home():
    return "<h1><center>Welcome to the Hmraaaaaa Page</center></h1>"

@app.route("/pass/<naam>/<int:marks>")
def passed(naam,marks):
    return f"<h1>Congrats {naam.title()} You have passed {marks}</h1>"

@app.route("/fail/<naam>/<int:marks>")
def failed(naam,marks):
  return f"<h1> {marks} aaya!!!! Padhlo Madarchod {naam.title()} </h1>"

    




@app.route("/score/<name>/<int:per>")
def score(name,per):
    if per>60:
        return redirect(url_for("passed",naam=name,marks=per))
    else:
        return redirect(url_for("failed",naam=name,marks=per))

@app.route("/Score")
def scoree():
    return "<h1><center>Naam or percentage kon batayega</center></h1>"

if __name__== "__main__":
    app.run(debug=True )

