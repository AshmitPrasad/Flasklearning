from flask import Flask, render_template ,url_for
from employees import employee_data
# Flask app creation
app=Flask(__name__)
#Home Page
@app.route("/")
@app.route(("/home"))
def Home():
    return render_template("home.html", title="HOME")
#About Page
@app.route("/about")
def About():
    return render_template("about.html",title="ABOUT ")

@app.route("/evaluate/<int:num>")
def Evaluate(num):
    return render_template("evaluate.html", number=num)
@app.route("/employees")
def Emp():
    return render_template("employee.html",emp_data=employee_data )

@app.route("/employees/manager")
def manager():
    return render_template("manger.html",emp_data=employee_data )


if __name__=="__main__": 
     app.run(debug=True)    
