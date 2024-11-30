from fastapi import FastAPI
import ollama

# Create FastAPI app
app = FastAPI()

# Define the endpoint that interacts with the Ollama model
@app.get("/predict")
def predict(text: str):
    try:
        # Use the Ollama model (e.g., "dolphin-llama3")
        response = ollama.chat(model="dolphin-llama3", messages=[text])
        return {"response": response['text']}  # Adjust based on the API response structure
    except Exception as e:
        return {"error": str(e)}

