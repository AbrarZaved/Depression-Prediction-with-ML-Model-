from django import forms


class DepressionPredictionForm(forms.Form):
    """
    Form for depression detection based on PHQ-9 questionnaire and lifestyle factors.
    All fields match the preprocessing in the Jupyter notebook.
    """

    # PHQ-9 Questions (Likert scale)
    LIKERT_CHOICES = [
        ("Not at all", "Not at all"),
        ("Several days", "Several days"),
        ("More than half the days", "More than half the days"),
        ("Nearly every day", "Nearly every day"),
    ]

    q1_interest = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Over the last two weeks, how often have you had little interest or pleasure in doing things you usually enjoy?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q2_depressed = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Over the last two weeks, how often have you felt down, depressed, or hopeless?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q3_sleep = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Over the last two weeks, have you had trouble falling asleep, staying asleep, or sleeping too much?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q4_energy = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="During this time, have you been feeling tired or lacking energy even after rest?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q5_appetite = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Have you noticed a decrease in appetite or have you been overeating?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q6_selfworth = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Have you been feeling bad about yourself — such as feeling like a failure or that you've let others down?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q7_focus = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Have you had difficulty concentrating on things, like reading or watching television?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q8_activity = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Have you been moving or speaking noticeably slower than usual, or the opposite — being unusually fidgety or restless?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    q9_suicidal = forms.ChoiceField(
        choices=LIKERT_CHOICES,
        label="Have you had thoughts that you would be better off dead or of harming yourself in some way?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    # Demographic & Lifestyle Features
    age = forms.IntegerField(
        label="Age",
        min_value=10,
        max_value=100,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter your age"}
        ),
    )

    gender = forms.ChoiceField(
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other"),
        ],
        label="Gender",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    employment_status = forms.ChoiceField(
        choices=[
            ("Student", "Student"),
            ("Employed", "Employed"),
            ("Unemployed", "Unemployed"),
            ("Self-employed", "Self-employed"),
            ("Retired", "Retired"),
        ],
        label="What best describes your current employment status?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    job_satisfaction = forms.ChoiceField(
        choices=[
            ("Very dissatisfied", "Very dissatisfied"),
            ("Dissatisfied", "Dissatisfied"),
            ("Neutral", "Neutral"),
            ("Satisfied", "Satisfied"),
            ("Very satisfied", "Very satisfied"),
        ],
        label="How satisfied are you with your current job or academic situation?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    sleep_duration = forms.ChoiceField(
        choices=[
            ("Less than 2 hours", "Less than 2 hours"),
            ("2–4 hours", "2–4 hours"),
            ("4–6 hours", "4–6 hours"),
            ("6–8 hours", "6–8 hours"),
            ("More than 8 hours", "More than 8 hours"),
        ],
        label="On average, how many hours do you sleep each night?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    diet_quality = forms.ChoiceField(
        choices=[
            ("Poor", "Poor"),
            ("Fair", "Fair"),
            ("Good", "Good"),
            ("Very good", "Very good"),
            ("Excellent", "Excellent"),
        ],
        label="How would you rate your current dietary habits?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    study_hours = forms.ChoiceField(
        choices=[
            ("Less than 2 hours", "Less than 2 hours"),
            ("2–4 hours", "2–4 hours"),
            ("4–6 hours", "4–6 hours"),
            ("More than 6 hours", "More than 6 hours"),
        ],
        label="On average, how many hours per day do you spend working or studying?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    work_stress = forms.ChoiceField(
        choices=[
            ("Never", "Never"),
            ("Rarely", "Rarely"),
            ("Sometimes", "Sometimes"),
            ("Often", "Often"),
            ("Always", "Always"),
        ],
        label="How frequently do you experience stress or pressure due to your work or studies?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    financial_stress = forms.ChoiceField(
        choices=[
            ("Not at all", "Not at all"),
            ("Rarely", "Rarely"),
            ("Sometimes", "Sometimes"),
            ("Often", "Often"),
            ("Always", "Always"),
        ],
        label="How often do you feel stressed about your financial or mental well-being?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    family_history = forms.ChoiceField(
        choices=[
            ("Yes", "Yes"),
            ("No", "No"),
            ("Not sure", "Not sure"),
        ],
        label="Does your family have a known history of mental health conditions?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    selfharm_history = forms.ChoiceField(
        choices=[
            ("Yes", "Yes"),
            ("No", "No"),
        ],
        label="Have you ever experienced thoughts of self-harm or suicide?",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
