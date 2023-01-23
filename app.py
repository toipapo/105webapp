from flask import Flask, render_template, request, redirect, url_for
import joblib
import math

app = Flask(__name__)

model_regression = 'ml model/regression_model.aiml'
loaded_model_regression = joblib.load(model_regression)

model_classification = 'ml model/classification_model.aiml'
loaded_model_classification = joblib.load(model_classification)
predictiondicts = {1 : "Unacceptable", 2 : "Acceptable",3 : "Good", 4 : "Very Good"}

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

@app.route('/predict', methods = ['POST', 'GET'])
def prediction():

    if request.method == 'POST':
        buying = float(request.form['buying'])
        maint = float(request.form['maint'])
        doors = float(request.form['doors'])
        persons = float(request.form['persons'])
        lug_boot = float(request.form['lug_boot'])
        safety = float(request.form['safety'])

        values = [[buying, maint, doors, persons, lug_boot, safety]]
        prediction_class = loaded_model_classification.predict(values)
        prediction_class = predictiondicts[prediction_class[0]]


        return render_template('classification_predict.html', data = prediction_class)
    
    else:   
        return render_template('classification_predict.html')

if __name__ == "__main__":
    app.run(debug = True)