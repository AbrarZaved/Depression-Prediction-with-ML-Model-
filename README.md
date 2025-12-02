# Depression Detection Web Application

A Django-based web application for depression screening using a machine learning model trained on PHQ-9 questionnaire data and lifestyle factors.

## 📋 Overview

This application implements a depression detection system based on:
- **PHQ-9 Depression Questionnaire** (9 questions with Likert scale responses)
- **Demographic Information** (Age, Gender)
- **Employment & Work Factors** (Employment status, job satisfaction, work hours, work stress)
- **Lifestyle Factors** (Sleep duration, diet quality, financial stress)
- **Medical History** (Family history, self-harm history)

The model uses the same preprocessing pipeline as the Jupyter notebook (`Ari_Final_Depressioncode.ipynb`) to ensure consistency between training and prediction.

## 🎯 Features

- Clean, Bootstrap-based user interface
- Form validation for all inputs
- Real-time prediction using the trained model
- Depression severity classification: None, Mild, Moderate, Mod-Severe, Severe
- PHQ-9 score calculation
- Confidence score display
- Personalized recommendations based on severity
- Crisis resources for severe cases

## 📁 Project Structure

```
Depression_Detection/
├── depression_project/          # Django project configuration
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py
├── predictor/                  # Django app for prediction
│   ├── forms.py               # Form definitions with all input fields
│   ├── views.py               # View logic with model loading & preprocessing
│   ├── urls.py                # App URL routing
│   └── templates/
│       └── predictor/
│           ├── home.html      # Input form page
│           └── result.html    # Results display page
├── venv/                      # Virtual environment
├── depression_detection_model.pkl  # Trained ML model
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Navigate to the project directory**
   ```powershell
   cd "e:\Code Arena\Programming\Python\Django\Depression_Detection"
   ```

2. **Activate the virtual environment**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies (if not already installed)**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```powershell
   python manage.py migrate
   ```

5. **Run the development server**
   ```powershell
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## 🔍 How It Works

### Data Flow

1. **User Input**: User fills out the form with PHQ-9 questions and lifestyle factors
2. **Preprocessing**: 
   - Likert scale responses mapped to numeric values (1-4)
   - Sleep duration mapped to numeric values (1-5)
   - Study hours mapped to numeric values (1-4)
   - Work stress mapped to numeric values (1-5)
   - Financial stress mapped to numeric values (1-5)
   - Categorical features kept as strings for one-hot encoding
3. **Model Prediction**: Processed data passed through the trained pipeline
4. **Result Display**: Depression severity and recommendations shown to user

### Feature Engineering (Matches Notebook)

**Numeric Features** (scaled using StandardScaler):
- `age`: Integer (10-100)
- `sleep_duration`: Mapped 1-5
- `study_hours`: Mapped 1-4
- `work_stress`: Mapped 1-5
- `financial_stress`: Mapped 1-5

**Categorical Features** (one-hot encoded):
- `gender`: Male, Female, Other
- `employment_status`: Student, Employed, Unemployed, Self-employed, Retired
- `job_satisfaction`: Very dissatisfied to Very satisfied
- `diet_quality`: Poor to Excellent
- `family_history`: Yes, No, Not sure
- `selfharm_history`: Yes, No

**PHQ-9 Questions** (Likert scale 1-4):
- q1_interest, q2_depressed, q3_sleep, q4_energy, q5_appetite
- q6_selfworth, q7_focus, q8_activity, q9_suicidal

### Model Details

- **Model Type**: Logistic Regression (best performing in cross-validation)
- **Preprocessing**: ColumnTransformer with StandardScaler and OneHotEncoder
- **Target Variable**: Depression severity (5 classes)
- **Label Encoding**: ['Mild', 'Mod-Severe', 'Moderate', 'None', 'Severe']

## 📊 Example Usage

### Sample Input:
```
Age: 25
Gender: Female
PHQ-9 Questions: Mix of "Several days" and "Not at all" responses
Employment: Student
Sleep Duration: 4-6 hours
Work Stress: Often
etc.
```

### Sample Output:
```
Depression Severity: Moderate
PHQ-9 Score: 18/36
Model Confidence: 87.5%
Recommendations: Consult with mental health professional, maintain regular sleep schedule, etc.
```

## ⚠️ Important Notes

1. **Model File Location**: The model file `depression_detection_model.pkl` must be in the project root directory
2. **Feature Order**: The code maintains the exact feature order expected by the trained model
3. **Preprocessing Consistency**: All mappings match those used in the training notebook
4. **Not a Diagnostic Tool**: This is a screening tool only and should not replace professional medical advice

## 🔧 Troubleshooting

### Issue: Model file not found
**Solution**: Ensure `depression_detection_model.pkl` is in the project root directory

### Issue: Import errors
**Solution**: Make sure you're in the virtual environment and all dependencies are installed:
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue: Database errors
**Solution**: Run migrations:
```powershell
python manage.py migrate
```

## 📝 Technical Details

### Mappings Used (Must Match Notebook)

```python
# Likert Scale (PHQ-9)
likert_map = {
    "Not at all": 1,
    "Several days": 2,
    "More than half the days": 3,
    "Nearly every day": 4
}

# Sleep Duration
sleep_duration_map = {
    'Less than 2 hours': 1,
    '2–4 hours': 2,
    '4–6 hours': 3,
    '6–8 hours': 4,
    'More than 8 hours': 5
}

# Study Hours
study_hours_map = {
    'Less than 2 hours': 1,
    '2–4 hours': 2,
    '4–6 hours': 3,
    'More than 6 hours': 4
}

# Work Stress & Financial Stress
stress_map = {
    'Never/Not at all': 1,
    'Rarely': 2,
    'Sometimes': 3,
    'Often': 4,
    'Always': 5
}
```

## 🛡️ Security Considerations

- Debug mode is ON for development (set `DEBUG = False` in production)
- Secret key is exposed in settings.py (generate a new one for production)
- No authentication required (add if needed for production)
- CSRF protection enabled by default

## 📄 License

This project is for educational and screening purposes only.

## 👥 Support

For issues or questions:
1. Check this README
2. Review the Jupyter notebook for model training details
3. Verify all mappings match between notebook and Django app

## 🎓 Credits

Model trained using PHQ-9 questionnaire data and lifestyle factors as documented in `Ari_Final_Depressioncode.ipynb`.
