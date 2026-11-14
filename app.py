from pathlib import Path
import pickle

import pandas as pd
import streamlit as st


MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
FEATURE_COLUMNS = [
    "Gender",
    "Age",
    "Family_background",
    "Living_style",
    "Current_semester",
    "CGPA",
    "friend_circle",
    "Health_condition",
    "Cost_without_study",
    "Relationship_status_Complicated",
    "Relationship_status_In a Relationship",
    "Relationship_status_Single",
    "Marital_status_Married",
    "Marital_status_Separated",
    "Marital_status_Unmarried",
]


@st.cache_resource
def load_model():
    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


st.set_page_config(
    page_title="Student Wellbeing | Mindful",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ink: #19332c;
        --muted: #71817a;
        --green: #2f725b;
        --mint: #e8f4ed;
        --line: #e8eeea;
        --paper: #ffffff;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(ellipse at 2% 2%, rgba(213, 237, 222, .58), transparent 31rem),
            #f6f8f6;
        color: var(--ink);
    }
    [data-testid="stHeader"] { background: transparent; }
    .block-container {
        max-width: 1080px;
        padding: 2.4rem 2rem 4rem;
    }
    h1, h2, h3 {
        color: var(--ink);
        font-family: 'Manrope', sans-serif;
        letter-spacing: -.035em;
    }
    .brand-line {
        display: flex;
        align-items: center;
        gap: .55rem;
        margin-bottom: 1.15rem;
        color: #527567;
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .13em;
        text-transform: uppercase;
    }
    .brand-mark {
        display: inline-flex;
        width: 1.7rem;
        height: 1.7rem;
        align-items: center;
        justify-content: center;
        border-radius: .6rem;
        background: #e1f0e6;
        font-size: 1rem;
    }
    .hero {
        position: relative;
        overflow: hidden;
        padding: 2.15rem 2.35rem;
        border: 1px solid rgba(255,255,255,.5);
        border-radius: 1.45rem;
        background: linear-gradient(118deg, #193b32 0%, #285c49 57%, #438267 100%);
        box-shadow: 0 18px 45px rgba(34, 73, 57, .13);
        color: white;
    }
    .hero:after {
        position: absolute;
        top: -6.5rem;
        right: -2rem;
        width: 20rem;
        height: 20rem;
        border: 1px solid rgba(255,255,255,.13);
        border-radius: 50%;
        box-shadow: 0 0 0 2.1rem rgba(255,255,255,.035), 0 0 0 4.3rem rgba(255,255,255,.025);
        content: "";
        pointer-events: none;
    }
    .hero h1 {
        position: relative;
        z-index: 1;
        margin: 0;
        color: white;
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 800;
        line-height: 1.12;
    }
    .hero p {
        position: relative;
        z-index: 1;
        max-width: 39rem;
        margin: .8rem 0 0;
        color: #d7e9dd;
        font-size: 1rem;
        line-height: 1.7;
    }
    .section-intro {
        margin: 2rem 0 1rem;
    }
    .section-intro h2 {
        margin: 0;
        font-size: 1.4rem;
        font-weight: 800;
    }
    .section-intro p {
        margin: .35rem 0 0;
        color: var(--muted);
        font-size: .94rem;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--line);
        border-radius: 1rem;
        background: rgba(255,255,255,.88);
        box-shadow: 0 8px 26px rgba(36, 61, 48, .035);
    }
    .form-heading {
        display: flex;
        align-items: center;
        gap: .7rem;
        margin-bottom: .35rem;
        color: var(--ink);
        font-family: 'Manrope', sans-serif;
        font-size: 1.08rem;
        font-weight: 800;
    }
    .form-heading span {
        display: inline-flex;
        width: 2rem;
        height: 2rem;
        align-items: center;
        justify-content: center;
        border-radius: .7rem;
        background: var(--mint);
        color: var(--green);
        font-family: 'DM Sans', sans-serif;
        font-size: .85rem;
    }
    [data-testid="stWidgetLabel"] p {
        color: #41574d;
        font-size: .88rem;
        font-weight: 600;
    }
    [data-testid="stNumberInput"] input,
    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        border-color: #e4ebe6;
        border-radius: .7rem;
        background-color: #fbfcfb;
    }
    [data-testid="stFormSubmitButton"] button {
        min-height: 3.2rem;
        border: 0;
        border-radius: .8rem;
        background: linear-gradient(100deg, #28664f, #438267);
        box-shadow: 0 8px 18px rgba(45, 106, 79, .19);
        color: white;
        font-family: 'Manrope', sans-serif;
        font-size: 1rem;
        font-weight: 700;
        transition: transform .18s ease, box-shadow .18s ease;
    }
    [data-testid="stFormSubmitButton"] button:hover {
        border: 0;
        box-shadow: 0 11px 22px rgba(45, 106, 79, .27);
        color: white;
        transform: translateY(-1px);
    }
    .notice {
        margin-top: 1.25rem;
        padding: 1rem 1.15rem;
        border: 1px solid #e6ece8;
        border-radius: .85rem;
        background: rgba(255,255,255,.68);
        color: #65756d;
        font-size: .84rem;
        line-height: 1.65;
    }
    .result-card {
        margin-top: 1.6rem;
        padding: 1.45rem 1.6rem;
        border: 1px solid #dfeae2;
        border-radius: 1rem;
        background: linear-gradient(120deg, #edf6ef, #fbfdfb);
    }
    .result-label {
        margin-bottom: .3rem;
        color: #648071;
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .1em;
        text-transform: uppercase;
    }
    .result-value {
        color: var(--ink);
        font-family: 'Manrope', sans-serif;
        font-size: 1.65rem;
        font-weight: 800;
    }
    .result-copy {
        margin-top: .25rem;
        color: #64746c;
        font-size: .9rem;
        line-height: 1.6;
    }
    @media (max-width: 640px) {
        .block-container { padding: 1.2rem 1rem 3rem; }
        .hero { padding: 1.6rem 1.35rem; }
        .hero p { font-size: .93rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="brand-line"><span class="brand-mark">✳</span> Mindful · Student wellbeing</div>
    <section class="hero">
      <h1>A little check-in<br>with yourself.</h1>
      <p>Share a few details to see what the machine-learning model predicts.
      Take your time — this is a private, non-judgmental space.</p>
    </section>
    <div class="section-intro">
      <h2>Tell us a little about you</h2>
      <p>Complete each section, then select “Get my result” when you’re ready.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

try:
    model = load_model()
except FileNotFoundError:
    st.error(f"Could not find the model file at `{MODEL_PATH}`.")
    st.stop()
except (
    ModuleNotFoundError,
    ImportError,
    pickle.UnpicklingError,
    AttributeError,
) as error:
    st.error(
        "The model could not be loaded. Install the packages in "
        "`requirements.txt` and ensure they are compatible with the versions "
        f"used to create `model.pkl`. Details: {error}"
    )
    st.stop()

model_features = getattr(model, "feature_names_in_", None)
if model_features is not None and list(model_features) != FEATURE_COLUMNS:
    st.error(
        "The feature names in `model.pkl` do not match the features expected "
        "by this app. Please check the notebook preprocessing and saved model."
    )
    st.stop()
if getattr(model, "n_features_in_", len(FEATURE_COLUMNS)) != len(FEATURE_COLUMNS):
    st.error(
        f"`model.pkl` expects {model.n_features_in_} features, but the app "
        f"provides {len(FEATURE_COLUMNS)}."
    )
    st.stop()

with st.form("student_information"):
    with st.container(border=True):
        st.markdown(
            '<div class="form-heading"><span>01</span> About you</div>',
            unsafe_allow_html=True,
        )
        identity_left, identity_middle, identity_right = st.columns(3)
        with identity_left:
            gender = st.selectbox("Gender", ["Male", "Female"])
            age = st.number_input("Age", min_value=1, max_value=120, value=20)
        with identity_middle:
            family_background = st.selectbox(
                "Family background",
                ["Lower Middle class", "Middle class", "Rich class"],
            )
            living_style = st.selectbox("Living style", ["Bachelor", "Family"])
        with identity_right:
            relationship_status = st.selectbox(
                "Relationship status",
                ["Single", "Complicated", "In a Relationship"],
            )
            marital_status = st.selectbox(
                "Marital status", ["Unmarried", "Married", "Separated"]
            )

    with st.container(border=True):
        st.markdown(
            '<div class="form-heading"><span>02</span> Study life</div>',
            unsafe_allow_html=True,
        )
        study_left, study_right = st.columns(2)
        with study_left:
            current_semester = st.number_input(
                "Current semester", min_value=0, max_value=20, value=1, step=1
            )
        with study_right:
            cgpa = st.number_input(
                "CGPA", min_value=0.0, max_value=4.0, value=3.0, step=0.01
            )

    with st.container(border=True):
        st.markdown(
            '<div class="form-heading"><span>03</span> Everyday wellbeing</div>',
            unsafe_allow_html=True,
        )
        wellbeing_left, wellbeing_middle, wellbeing_right = st.columns(3)
        with wellbeing_left:
            friend_circle = st.selectbox("Have a friend circle?", ["Yes", "No"])
        with wellbeing_middle:
            health_condition = st.selectbox(
                "Health condition", ["Good", "Normal", "Abnormal", "Critical"]
            )
        with wellbeing_right:
            cost_without_study = st.number_input(
                "Cost without study", min_value=0, value=0, step=500
            )

    submitted = st.form_submit_button(
        "Get my result", type="primary", use_container_width=True
    )

st.markdown(
    """
    <div class="notice">
      <strong>A gentle reminder:</strong> This model’s output is not a diagnosis
      and cannot tell you whether you have depression. If you’re concerned about
      how you’re feeling, please consider talking with someone you trust or a
      qualified mental-health professional.
    </div>
    """,
    unsafe_allow_html=True,
)

if submitted:
    relationship_features = {
        "Relationship_status_Complicated": int(
            relationship_status == "Complicated"
        ),
        "Relationship_status_In a Relationship": int(
            relationship_status == "In a Relationship"
        ),
        "Relationship_status_Single": int(relationship_status == "Single"),
    }
    marital_features = {
        "Marital_status_Married": int(marital_status == "Married"),
        "Marital_status_Separated": int(marital_status == "Separated"),
        "Marital_status_Unmarried": int(marital_status == "Unmarried"),
    }
    input_values = {
        "Gender": {"Male": 0, "Female": 1}[gender],
        "Age": age,
        "Family_background": {
            "Lower Middle class": 1,
            "Middle class": 2,
            "Rich class": 3,
        }[family_background],
        "Living_style": {"Bachelor": 0, "Family": 1}[living_style],
        "Current_semester": current_semester,
        "CGPA": cgpa,
        "friend_circle": {"No": 0, "Yes": 1}[friend_circle],
        "Health_condition": {
            "Good": 3,
            "Normal": 2,
            "Abnormal": 1,
            "Critical": 0,
        }[health_condition],
        "Cost_without_study": cost_without_study,
        **relationship_features,
        **marital_features,
    }
    model_input = pd.DataFrame([input_values], columns=FEATURE_COLUMNS)
    prediction = model.predict(model_input)[0]

    if prediction not in (0, 1):
        st.error(f"The model returned an unexpected class: {prediction!r}.")
        st.stop()

    if prediction == 1:
        result_value = "The model predicted “Yes”"
        result_copy = (
            "This is only the model’s output, not a diagnosis. If you’re "
            "concerned, consider reaching out to a qualified professional."
        )
    else:
        result_value = "The model predicted “No”"
        result_copy = (
            "This is only the model’s output and doesn’t rule out a need for "
            "support. Your feelings are valid either way."
        )
    st.markdown(
        f"""
        <div class="result-card">
          <div class="result-label">Your check-in result</div>
          <div class="result-value">{result_value}</div>
          <div class="result-copy">{result_copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if hasattr(model, "predict_proba"):
        classes = list(model.classes_)
        if 1 in classes:
            probability = model.predict_proba(model_input)[0][classes.index(1)]
            st.caption(
                f"Model score for the “Yes” class: {probability:.1%}. "
                "This is not a clinical risk score."
            )
