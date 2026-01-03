from fastapi import FastAPI, Form, Request  # Form - Reads form input values from HTML  # Request - Required by FastAPI when using Jinja templates
from fastapi.templating import Jinja2Templates  # Allows FastAPI to render HTML pages.
import pandas as pd
from dotenv import load_dotenv
import mlflow
import os


# Load environment variables from .env
load_dotenv()

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")

# Fast API -> Backend web framework
app = FastAPI(title="Calories Burn Prediction")


# Load Production model from the registry
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

pipeline = mlflow.pyfunc.load_model(
    "models:/Calories-Burn-Regressor/Production"
)

print("✅ Model loaded successfully")


# Setup templates folder (Tells FastAPI where your HTML files are)
templates = Jinja2Templates(directory="templates")

# Home Route - Displays the HTML form
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}              # FastAPI + Jinja requires the request object for rendering templates.
    )

# Predict Route - Receives values submitted from HTML form
@app.post("/predict")
def predict(
    request: Request,
    Gender: str = Form(...),
    Age: float = Form(...),
    Height: float = Form(...),
    Weight: float = Form(...),
    Duration: float = Form(...),
    Heart_Rate: float = Form(...),
    Body_Temp: float = Form(...)
):
    input_data = pd.DataFrame({      # Convert Form Data into DataFrame
        "Gender": [Gender],
        "Age": [Age],
        "Height": [Height],
        "Weight": [Weight],
        "Duration": [Duration],
        "Heart_Rate": [Heart_Rate],
        "Body_Temp": [Body_Temp]
    })

    # Make prediction - returns an array
    prediction = pipeline.predict(input_data)[0]

    # Return Result to HTML Page
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "Calories": round(prediction, 2)
        }
    )
