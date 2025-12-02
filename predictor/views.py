from django.shortcuts import render
from django.conf import settings
from .forms import DepressionPredictionForm
import joblib
import pandas as pd
import os
from datetime import datetime

# Load the model once when the module is loaded
MODEL_PATH = os.path.join(settings.BASE_DIR, "depression_detection_model.pkl")
model_pipeline = joblib.load(MODEL_PATH)

# Define label encoder classes (from notebook - order: Mild, Mod-Severe, Moderate, None, Severe)
LABEL_CLASSES = ["Mild", "Mod-Severe", "Moderate", "None", "Severe"]


def preprocess_input(form_data):
    """
    Preprocess user input to match the exact format expected by the model.
    This replicates the preprocessing steps from the notebook.
    """

    # 1. Map Likert scale responses to numeric (1-4)
    likert_map = {
        "Not at all": 1,
        "Several days": 2,
        "More than half the days": 3,
        "Nearly every day": 4,
    }

    # 2. Map sleep duration to numeric
    sleep_duration_map = {
        "Less than 2 hours": 1,
        "2–4 hours": 2,
        "4–6 hours": 3,
        "6–8 hours": 4,
        "More than 8 hours": 5,
    }

    # 3. Map study hours to numeric
    study_hours_map = {
        "Less than 2 hours": 1,
        "2–4 hours": 2,
        "4–6 hours": 3,
        "More than 6 hours": 4,
    }

    # 4. Map work stress to numeric
    work_stress_map = {"Never": 1, "Rarely": 2, "Sometimes": 3, "Often": 4, "Always": 5}

    # 5. Map financial stress to numeric
    financial_stress_map = {
        "Not at all": 1,
        "Rarely": 2,
        "Sometimes": 3,
        "Often": 4,
        "Always": 5,
    }

    # Apply mappings to PHQ-9 questions
    phq_questions = [
        "q1_interest",
        "q2_depressed",
        "q3_sleep",
        "q4_energy",
        "q5_appetite",
        "q6_selfworth",
        "q7_focus",
        "q8_activity",
        "q9_suicidal",
    ]

    processed_data = {}

    for q in phq_questions:
        processed_data[q] = likert_map[form_data[q]]

    # Apply numeric mappings
    processed_data["age"] = int(form_data["age"])
    processed_data["sleep_duration"] = sleep_duration_map[form_data["sleep_duration"]]
    processed_data["study_hours"] = study_hours_map[form_data["study_hours"]]
    processed_data["work_stress"] = work_stress_map[form_data["work_stress"]]
    processed_data["financial_stress"] = financial_stress_map[
        form_data["financial_stress"]
    ]

    # Categorical features remain as strings (will be one-hot encoded by the pipeline)
    processed_data["gender"] = form_data["gender"]
    processed_data["employment_status"] = form_data["employment_status"]
    processed_data["job_satisfaction"] = form_data["job_satisfaction"]
    processed_data["diet_quality"] = form_data["diet_quality"]
    processed_data["family_history"] = form_data["family_history"]
    processed_data["selfharm_history"] = form_data["selfharm_history"]

    # Create DataFrame with the exact column order expected by the model
    # Order from notebook: age, gender, q1-q9, employment_status, work_stress, job_satisfaction,
    # sleep_duration, diet_quality, study_hours, financial_stress, family_history, selfharm_history

    df = pd.DataFrame(
        [
            {
                "age": processed_data["age"],
                "gender": processed_data["gender"],
                "q1_interest": processed_data["q1_interest"],
                "q2_depressed": processed_data["q2_depressed"],
                "q3_sleep": processed_data["q3_sleep"],
                "q4_energy": processed_data["q4_energy"],
                "q5_appetite": processed_data["q5_appetite"],
                "q6_selfworth": processed_data["q6_selfworth"],
                "q7_focus": processed_data["q7_focus"],
                "q8_activity": processed_data["q8_activity"],
                "q9_suicidal": processed_data["q9_suicidal"],
                "employment_status": processed_data["employment_status"],
                "work_stress": processed_data["work_stress"],
                "job_satisfaction": processed_data["job_satisfaction"],
                "sleep_duration": processed_data["sleep_duration"],
                "diet_quality": processed_data["diet_quality"],
                "study_hours": processed_data["study_hours"],
                "financial_stress": processed_data["financial_stress"],
                "family_history": processed_data["family_history"],
                "selfharm_history": processed_data["selfharm_history"],
            }
        ]
    )

    return df


def home(request):
    """
    Display the input form for depression prediction.
    """
    if request.method == "POST":
        form = DepressionPredictionForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            form_data = form.cleaned_data

            # Preprocess the input
            input_df = preprocess_input(form_data)

            # Make prediction
            prediction_encoded = model_pipeline.predict(input_df)[0]
            prediction_proba = model_pipeline.predict_proba(input_df)[0]

            # Decode prediction to human-readable label
            prediction_label = LABEL_CLASSES[prediction_encoded]

            # Get confidence score for predicted class
            confidence = prediction_proba[prediction_encoded] * 100

            # Calculate PHQ-9 total score for reference
            likert_map = {
                "Not at all": 1,
                "Several days": 2,
                "More than half the days": 3,
                "Nearly every day": 4,
            }
            phq_questions = [
                "q1_interest",
                "q2_depressed",
                "q3_sleep",
                "q4_energy",
                "q5_appetite",
                "q6_selfworth",
                "q7_focus",
                "q8_activity",
                "q9_suicidal",
            ]
            phq_total = sum(likert_map[form_data[q]] for q in phq_questions)

            # Prepare context for result page
            context = {
                "prediction": prediction_label,
                "confidence": round(confidence, 2),
                "phq_total": phq_total,
                "form_data": form_data,
                "assessment_date": datetime.now().strftime("%B %d, %Y"),
            }

            return render(request, "predictor/result.html", context)
    else:
        form = DepressionPredictionForm()

    return render(request, "predictor/home.html", {"form": form})


def result(request):
    """
    Display prediction results (handled via POST redirect from home).
    """
    return render(request, "predictor/result.html")
