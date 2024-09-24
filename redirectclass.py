import time
from flask import Flask, redirect, url_for

gap = Flask(__name__)

@gap.route("/")
@gap.route("/home")
def home():
    return "<h1>Welcome to the Hmra Redirecton page page!</h1>"


@gap.route("/pass")
def passed():
    return "<h1>Congratz, you've passed!</h1>"


@gap.route("/fail")
def failed():
    return "<h1>Sorry, you've failed!</h1>"


@gap.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        time.sleep(1)
        #redirect (user to page 'fail'
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
         #redirect user to page 'pass'
        return redirect(url_for("passed"))



if __name__ == "__main__":
    gap.run(debug=True)