from flask import Flask, request, jsonify,  render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler
filename = 'predictor_model.sav'
predictor = pickle.load(open(filename, 'rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        predictive_input = [
            float(request.form['PLU 4046']),
            float(request.form['PLU 4225']),
            float(request.form['PLU 4770']),
            float(request.form['Small Bags']),
            float(request.form['Large Bags']),
            float(request.form['XLarge Bags']),
            float(request.form['Year']),
        ]

        predictive_input_array = np.asarray(predictive_input).reshape(1, -1)
        prediction = predictor.predict(predictive_input_array)
        prediction = '{:.2f}$'.format(prediction[0])

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
