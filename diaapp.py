from flask import Flask, render_template, request

app = Flask(__name__)

# Load your model and imputer here
# model = ...
# fill_values = ...

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
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

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
