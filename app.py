from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# For the purpose of this example, we'll simulate emotion detection
def detect_emotion(image):
    emotion_labels = ['happiness',  'sadness', 'neutral']
    threshold = 0.5
    # Simulate emotion detection by returning a static result
    pred = model.predict(image)

    label_prob = np.max(pred)
    if label_prob < threshold:
        label = 2  # set the label to 'neutral'
    else:
        label = np.argmax(pred)
    text = emotion_labels[label]
    return text, threshold

# Load your emotion detection model
def load_emotion_model():
    BS=32
    INIT_LR = 1e-4
    EPOCHS = 10
    # model = tf.keras.models.load_model('../Downloads/CloseOrOpenEye-2.model', compile=False)
    model = tf.keras.models.load_model('../Downloads/model-5.h5', compile=False)
    # imagemodel = tf.keras.models.load_model('../Downloads/CloseOrOpenEye-2.model', compile=False)

    # Define the optimizer
    optimizer = tf.keras.optimizers.Nadam(learning_rate=0.001)
    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)

    # Compile the model with the specified optimizer
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return None

emotion_model = load_emotion_model()

@app.route('/process_emotion', methods=['POST'])
def process_emotion():
    try:
        image_data = request.files['image'].read()
        image_np = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        
        # You can apply pre-processing steps to the image here
        
        emotion_label, emotion_probability = detect_emotion(image)
        
        response = {
            "emotion_label": emotion_label,
            "emotion_probability": emotion_probability
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
