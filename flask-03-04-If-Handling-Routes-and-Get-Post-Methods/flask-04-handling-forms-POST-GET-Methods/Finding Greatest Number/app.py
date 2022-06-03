# Import Flask modules
from flask import Flask, render_template, request
from functools import reduce

# Create an object named app
app = Flask(__name__)


# create a function named "lcm" which calculates a least common multiple values of two numbers. 
def greatest(num1,num2,num3,num4,num5):
    return reduce(max , [num1,num2,num3,num4,num5])  




# Create a function named `index` which uses template file named `index.html` 
# send two numbers as template variable to the app.py and assign route of no path ('/') 
@app.route("/")
def index():
    return render_template("index.html", methods=["GET"])




# calculate sum of them using "lcm" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file
@app.route("/calc", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        num3 = request.form.get("number3")
        num4 = request.form.get("number4")
        num5 = request.form.get("number5")
        return render_template("result.html", number1 = num1, number2 = num2, number3 = num3, number4 = num4, number5 = num5,  greatest = greatest(int(num1),int(num2),int(num3),int(num4),int(num5)), developer_name = 'Erkan')


# Add a statement to run the Flask application which can be debugged.
if __name__== "__main__":
    app.run(debug=True)



