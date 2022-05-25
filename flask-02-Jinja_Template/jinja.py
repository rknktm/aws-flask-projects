from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1=77, number2=99)
@app.route('/mult')
def number():
    var1, var2 = 30, 70
    return render_template('body.html', num1=var1, num2=var2, mul=var1*var2)

@app.route('/sum')
def number1():

    x=15
    y=20
    return render_template('sum.html', num1=x, num2=y, sum=x+y)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)