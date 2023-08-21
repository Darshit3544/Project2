document.addEventListener("DOMContentLoaded", () => {
    const imageInput = document.getElementById("imageInput");
    const processButton = document.getElementById("processButton");
    const outputText = document.getElementById("outputText");

    processButton.addEventListener("click", async () => {
        const file = imageInput.files[0];

        if (file) {
            const reader = new FileReader();
            reader.onload = async function(event) {
                const imageBlob = event.target.result;
                const formData = new FormData();
                formData.append("image", file);

                const apiUrl = "/process_emotion";  // Assuming the server runs on the same domain

                try {
                    const response = await fetch(apiUrl, {
                        method: "POST",
                        body: formData
                    });

                    if (response.ok) {
                        const data = await response.json();
                        const emotionLabel = data.emotion_label;
                        const emotionProbability = data.emotion_probability;
                        
                        outputText.innerText = `Emotion: ${emotionLabel}\nProbability: ${emotionProbability}`;
                    } else {
                        console.error("API request failed");
                    }
                } catch (error) {
                    console.error("Error sending API request:", error);
                }
            };
            reader.readAsDataURL(file);
        }
    });
});
