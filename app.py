from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def results():
    meal_cost = request.form['meal_cost']
    tip_percentage = request.form['tip_percentage']
    total_cost = tip_calculator(meal_cost, tip_percentage)
    return render_template('results.html', total_cost=total_cost)


def tip_calculator(meal_cost, tip_percentage):
    meal_cost = float(meal_cost)
    tip_percentage = float(tip_percentage)
    tip_cost = meal_cost * (tip_percentage/100)
    return meal_cost + tip_cost

if __name__ == '__main__':
    app.run(debug=True)
