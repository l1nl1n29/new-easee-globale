from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import base64
import os

app = Flask(__name__)
model = tf.keras.models.load_model('model/mymodel.h5')

@app.route('/', methods=['GET'])
def index():
    #current_user = get_jwt_identity()
    #return jsonify(logged_in_as=current_user), 200
    return "Hello World this is <SEESEA-GLOBALE> save your word, save your life"

# Route for image prediction
@app.route('/predict', methods=['POST'])
def predict_image():
    image_data = request.json['image_data']

    # Generate image from base64 data
    image = generate_image_from_base64(image_data)

    # Preprocess the image
    img = tf.keras.preprocessing.image.load_img(image, target_size=(150, 150))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    # Make prediction using the model
    predictions = model.predict(images)
    predicted_class = "is a Trash" if predictions[0] > 0.5 else "is a Coral"

    # Clean up the temporary image file
    os.remove(image)

    # Return the prediction result
    return jsonify({'prediction': predicted_class})

def generate_image_from_base64(image_data):
    filename = 'temp_image.jpg'
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(image_data))
    return filename

if __name__ == '__main__':
    app.run(debug=True)
