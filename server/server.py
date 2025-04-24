from flask import Flask, request, jsonify
import util

app = Flask (__name__)

@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    MEGABYTE = (2 ** 10) ** 2
    app.config['MAX_CONTENT_LENGTH'] = None
    # Max number of fields in a multi part form (I don't send more than one file)
    # app.config['MAX_FORM_PARTS'] = ...
    app.config['MAX_FORM_MEMORY_SIZE'] = 50 * MEGABYTE
    app.run(port=5000)
