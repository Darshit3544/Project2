from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

# For the purpose of this example, we'll simulate emotion detection
def detect_emotion(image):
    # Simulate emotion detection by returning a static result
    emotion_label = "happiness"
    emotion_probability = 0.85
    return emotion_label, emotion_probability
@app.route('/')
def index():
    return render_template('index.html')
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
