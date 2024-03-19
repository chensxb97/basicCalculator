from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html',result="")

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
    except Exception:
        return render_template('calculator.html', result='Err')
    return render_template('calculator.html', result=str(result))

if __name__ == '__main__':
    app.run(debug=True)
