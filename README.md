# MLflow with DAGsHub Integration Project - Calories Burn Predictor

This project demonstrates the integration of MLflow with DAGsHub for experiment tracking and model management in machine learning workflows.

## 🚀 Features

- MLflow experiment tracking
- Remote tracking with DAGsHub
- Model versioning and management
- Metrics and parameter logging
- Artifact storage and management

## 📋 Prerequisites

- Python 3.11+
- Git
- DAGsHub account
- Required Python packages:
  ```bash
  pip install mlflow scikit-learn numpy
  ```

## 🔧 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Supratim0406/Calories-Burn-Predictor-MLflow-FastAPI-DagsHubIntegration.git
   cd Calories-Burn-Predictor-MLflow-FastAPI-DagsHubIntegration
   ```

2. Set up DAGsHub credentials in Git Bash:
   ```bash
   export MLFLOW_TRACKING_URI=https://dagshub.com/<username>/<repo-name>.mlflow
   export MLFLOW_TRACKING_USERNAME=<your-dagshub-username>
   export MLFLOW_TRACKING_PASSWORD=<your-dagshub-token>
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running the Project

1. Run the MLflow project:
   ```bash
    python -m uvicorn app:app --reload
   ```

2. View results in DAGsHub:
   - Go to your DAGsHub repository
   - Navigate to the "Experiments" tab
   - View metrics, parameters, and artifacts

## 📊 Project Structure

```
dagshub-mlflow-dvc-project/
├── app.py                 # Fast API application
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── mlruns/               # Local MLflow tracking directory

```

## 🔍 What's Included

- Experiment tracking with MLflow
- Model training and evaluation
- Parameter logging
- Metric tracking (accuracy, precision, recall, F1-score)
- Model artifact storage
- Remote tracking with DAGsHub

## 📈 MLflow Features Used

- Experiment Management
- Parameter Tracking
- Metric Logging
- Model Versioning
- Artifact Storage
- Remote Tracking

## 🔐 Environment Variables

The following environment variables need to be set:

- `MLFLOW_TRACKING_URI`: Your DAGsHub MLflow tracking URI
- `MLFLOW_TRACKING_USERNAME`: Your DAGsHub username
- `MLFLOW_TRACKING_PASSWORD`: Your DAGsHub token

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🎥 Demo

[▶️ Watch Demo Video](https://github.com/user-attachments/assets/e4c34b2d-2f4a-4c2f-b482-927054a6396e)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Supratim Saha

## 🙏 Acknowledgments

- MLflow team for the amazing experiment tracking tool
- DAGsHub for providing the remote tracking infrastructure 

## Screenshot
<img width="1611" height="955" alt="image" src="https://github.com/user-attachments/assets/febf49c2-a108-499b-96b6-dc905a1f3e15" />

## Swagger -
<img width="1601" height="858" alt="image" src="https://github.com/user-attachments/assets/9a376e58-e61f-420e-af9c-f825b38d790d" />

<img width="1619" height="797" alt="image" src="https://github.com/user-attachments/assets/8a695402-0efb-422a-b7b0-5b1d499ba04c" />


