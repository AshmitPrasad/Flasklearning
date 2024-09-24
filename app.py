from flask import Flask
app=Flask(__name__)
@app.route("/")
@app.route(("/home"))
def Home():
    return "<h1>Welcome to the HomePage</h1>"
@app.route("/about")
def About():
    return "<h1> <center>This is My About Page</center><h1>"
@app.route("/Welcome/<myname>")
def name(myname):
    return f"<h1><center> Hi {myname.title()} Welcome to Flask world</center></h1>"
@app.route("/Addition/<int:num>/<int:num2>")
def addition(num,num2):
    return f'<h1><center> Input numer is {num}+{num2} and Output is-{num+num2}</center></h1>'

if __name__== "__main__":
    app.run(debug=True )
    