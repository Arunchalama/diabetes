from flask import Flask, render_template, request
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load your data and perform preprocessing here
data = pd.read_csv('diabetes.csv')
feature_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = data[feature_columns].values

# Use SimpleImputer to fill missing values with the mean
fill_values = SimpleImputer(missing_values=0, strategy='mean')
X_filled = fill_values.fit_transform(X)

# Load your model here
model = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=1)
Y = data['Outcome'].values
model.fit(X_filled, Y)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None

    if request.method == 'POST':
        try:
            pregnancies = float(request.form['pregnancies'])
            glucose = float(request.form['glucose'])
            blood_pressure = float(request.form['blood_pressure'])
            skin_thickness = float(request.form['skin_thickness'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
            age = float(request.form['age'])

            x_demo = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
            x_demo_filled = fill_values.transform(x_demo)
            prediction = model.predict(x_demo_filled)

            if prediction == 0:
                result = "Person is likely to NOT have diabetes"
            else:
                result = "Person is likely to have diabetes"

        except Exception as e:
            error_message = str(e)

    return render_template('index.html', result=result, error_message=error_message)

if __name__ == '__main__':
    app.run()
