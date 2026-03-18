import streamlit as st
from PyPDF2 import PdfReader
import io
import os
from openai import AzureOpenAI
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------
load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")

STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

# -----------------------------
# CLIENTS
# -----------------------------
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# -----------------------------
# BLOB FUNCTIONS
# -----------------------------
def upload_to_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.name)
    blob_client.upload_blob(file, overwrite=True)

def read_from_blob(file_name):
    blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file_name)
    return blob_client.download_blob().readall()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="AI Medical Assistant", page_icon="🩺", layout="wide")

# -----------------------------
# UI STYLING
# -----------------------------
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #e3f2fd, #fce4ec); }
.header { text-align: center; padding: 10px; }
.chat-user { background-color: #c8e6c9; padding: 10px; border-radius: 10px; margin: 5px; }
.chat-bot { background-color: #ffcdd2; padding: 10px; border-radius: 10px; margin: 5px; }
.card { background: white; padding: 15px; border-radius: 10px; box-shadow: 0px 2px 8px gray; margin-bottom: 10px; }
.footer { position: fixed; bottom: 0; width: 100%; background-color: #fff3cd; text-align: center; padding: 8px; font-size: 13px; border-top: 1px solid #ccc; }
.block-container { padding-bottom: 80px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class='header'>
    <img src="https://cdn-icons-png.flaticon.com/512/2966/2966486.png" width="70">
    <h2 style='color:#0d47a1;'>AI Medical Report Assistant</h2>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# INFO CARDS
# -----------------------------
st.markdown("""
<div style='display:flex; gap:15px;'>
<div class='card'><h4>📄 Upload Reports</h4><p>Securely upload your medical reports</p></div>
<div class='card'><h4>🤖 AI Analysis</h4><p>Get instant health insights</p></div>
<div class='card'><h4>🩺 Doctor Support</h4><p>Consult specialists when needed</p></div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# FILE UPLOAD SECTION
# -----------------------------
st.markdown("## 📄 Upload & Analysis")
uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state: st.session_state.messages = []
if "last_file" not in st.session_state: st.session_state.last_file = None

# -----------------------------
# PROCESS FILE
# -----------------------------
if uploaded_file:
    if st.session_state.last_file != uploaded_file.name:
        st.session_state.messages = []
        st.session_state.last_file = uploaded_file.name

    upload_to_blob(uploaded_file)
    file_data = read_from_blob(uploaded_file.name)

    if uploaded_file.type == "text/plain":
        report_text = file_data.decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf = PdfReader(io.BytesIO(file_data))
        report_text = "".join([page.extract_text() or "" for page in pdf.pages])

    st.success("✅ File uploaded successfully!")

    # -----------------------------
    # CHAT SECTION
    # -----------------------------
    st.markdown("## 💬 Medical Chat")
    user_input = st.chat_input("Ask your medical question...")

    if user_input:
        st.session_state.messages.append(("user", user_input))

        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[{
                "role": "user",
                "content": f"""
                Analyze the medical report.
                Detect diseases, risks, precautions.
                Report:
                {report_text}
                Question:
                {user_input}
                """
            }],
            temperature=0.3
        )

        answer = response.choices[0].message.content
        st.session_state.messages.append(("bot", answer))

        if any(word in answer.lower() for word in ["high", "low", "risk"]):
            st.error("🚨 Health Risk Detected! Consult a doctor.")

        if "diabetes" in answer.lower():
            st.info("🩺 Suggested: Endocrinologist")
        elif "heart" in answer.lower():
            st.info("❤️ Suggested: Cardiologist")

    # DISPLAY CHAT
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(f"<div class='chat-user'>👤 {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bot'>🤖 {msg}</div>", unsafe_allow_html=True)

# -----------------------------
# DOCTOR CONSULT SECTION
# -----------------------------
st.markdown("## 🩺 Need Doctor Help?")
if "show_doctors" not in st.session_state: st.session_state.show_doctors = False

if st.button("👨‍⚕️ Consult Specialist"):
    st.session_state.show_doctors = not st.session_state.show_doctors

if st.session_state.show_doctors:
    st.markdown("""
    <div class='card'>
    <h4>🏥 Available Doctors</h4>
    <p><b>Dr. Tushar Roy</b> - Cardiologist<br>📍 Andheri | 📞 9876543210</p>
    <p><b>Dr. Vijay Sharma</b> - General Physician<br>📍 Bandra | 📞 9123456780</p>
    <p><b>Dr. Nayan Patel</b> - Endocrinologist<br>📍 Powai | 📞 9988776655</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# MAP SECTION
# -----------------------------
st.markdown("## 📍 Find Nearby Hospitals")
city = st.text_input("Enter your city", "📍")
st.components.v1.iframe(
    f"https://www.google.com/maps?q=hospitals+near+{city}&output=embed",
    height=250
)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<div class='footer'>
⚠️ This is AI-generated medical advice. Please consult a qualified doctor.
</div>
""", unsafe_allow_html=True)