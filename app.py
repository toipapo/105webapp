from flask import Flask, render_template, request, redirect, url_for
import joblib
import math

app = Flask(__name__)

model_regression = 'ml model/regression_model.aiml'
loaded_model_regression = joblib.load(model_regression)

def BMI(height, weight):
    return round((weight / height**2),2)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        children = float(request.form['children'])
        smoker = float(request.form['smoker'])

        bmi = BMI(height, weight)

        values = [[age, sex, bmi, children, smoker]]
        prediction = loaded_model_regression.predict(values)

        prediction_cost = '{:,}'.format(math.ceil(prediction * 100) / 100)

        return render_template('home.html', data = prediction_cost)

    else:   
        return render_template('home.html')

# @app.route('/predict', methods = ['POST'])
# def prediction():

#     if request.method == 'POST':
#         age = float(request.form['age'])
#         sex = float(request.form['sex'])
#         bmi = float(request.form['bmi'])
#         children = float(request.form['children'])
#         smoker = float(request.form['smoker'])

#         values = [[age, sex, bmi, children, smoker]]
#         prediction = loaded_model_regression.predict(values)

#         prediction_cost = math.ceil(prediction * 100) / 100

#         return redirect(render_template, data = prediction_cost)

if __name__ == "__main__":
    app.run(debug = True)