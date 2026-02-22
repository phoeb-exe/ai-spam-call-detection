import streamlit as st
import time
from asr.asr_model import ASRModel
from models.spam_model import SpamModel
import requests

st.set_page_config(page_title="AI Spam Call Detection")

def reset_state():
    st.session_state.analyzed = False
    st.session_state.result = None
    st.rerun()

@st.dialog("Call Analysis Result")
def show_result_dialog(result):
    pred = result["pred"]
    prob = result["prob"]

    if pred == 1:
        st.error(f"### ⚠️ HIGH RISK SPAM CALL\nRisk Confidence: {prob:.2%}")
    else:
        st.success(f"### ✅ LEGITIMATE CALL\nConfidence Level: {(1-prob):.2%}")

    st.write("---")
    st.write("### Transcript Log")
    st.write(result["transcript"])

    if st.button("Close"):
        reset_state()

st.title("Incoming Call Detection Engine")
st.markdown("Upload audio to simulate an incoming phone call.")

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False
if "result" not in st.session_state:
    st.session_state.result = None


uploaded_file = st.file_uploader("Upload audio", type=["wav", "mp3"])


if uploaded_file is not None and not st.session_state.analyzed:

    with st.spinner("Sending to detection engine..."):
        files = {"file": uploaded_file}
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files=files
        )

        result = response.json()

        pred = result["prediction"]
        prob = result["probability"]
        transcript = result["transcript"]

        st.session_state.result = {
            "pred": pred,
            "prob": prob,
            "transcript": transcript
        }

        time.sleep(1)

        st.session_state.analyzed = True
        st.rerun()


if st.session_state.analyzed and st.session_state.result:
    show_result_dialog(st.session_state.result)