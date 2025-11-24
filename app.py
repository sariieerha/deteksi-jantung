from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['file']
    filepath = os.path.join('static', file.filename)
    file.save(filepath)

    # Tidak ada prediksi
    return render_template(
        'result.html',
        image_path=filepath,
    )

if __name__ == '__main__':
    app.run(debug=True)
