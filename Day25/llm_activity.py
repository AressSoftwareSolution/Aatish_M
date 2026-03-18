import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import re

# Page configuration
st.set_page_config(page_title="AI Quiz Master", page_icon="⚛")

st.title("🤖 AI Quiz Master")
st.write("Generate MCQs and test your knowledge!")

# Load environment variables
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# =========================
# 🎯 QUIZ GENERATION
# =========================

st.header("🎯 Generate MCQ Quiz")

topic = st.text_input("Enter topic:")

custom_instruction = st.text_area(
    "Optional: Add extra instructions",
    placeholder="Example: Make questions difficult and scenario-based."
)

if st.button("Generate Quiz"):

    prompt = f"""
    Create 5 multiple choice questions about {topic}.
    Format strictly as:

    Q1: Question
    A. Option
    B. Option
    C. Option
    D. Option
    Answer: Correct Option Letter

    Repeat for 5 questions.
    """

    if custom_instruction:
        prompt += f"\nAdditional Instructions: {custom_instruction}"

    with st.spinner("Generating quiz..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

    st.session_state.quiz = response.choices[0].message.content


# =========================
# 📊 PARSE QUIZ FUNCTION
# =========================

def parse_quiz(text):
    questions = []
    blocks = re.split(r"\n(?=Q\d+:)", text)

    for block in blocks:
        q_match = re.search(r"Q\d+:\s*(.*)", block)
        options = re.findall(r"[A-D]\.\s*(.*)", block)
        answer = re.search(r"Answer:\s*([A-D])", block)

        if q_match and options and answer:
            questions.append({
                "question": q_match.group(1),
                "options": options,
                "answer": answer.group(1)
            })

    return questions


# =========================
# 📝 DISPLAY QUIZ + SCORING
# =========================

if "quiz" in st.session_state:
    st.header("📝 Answer the Questions")

    quiz_data = parse_quiz(st.session_state.quiz)

    score = 0
    user_answers = {}

    for i, q in enumerate(quiz_data):
        st.write(f"**Q{i+1}: {q['question']}**")

        choice = st.radio(
            "Select an option:",
            q["options"],
            key=f"q{i}"
        )

        user_answers[i] = choice

    if st.button("Submit Quiz"):
        for i, q in enumerate(quiz_data):
            correct_index = ord(q["answer"]) - 65
            correct_answer = q["options"][correct_index]

            if user_answers[i] == correct_answer:
                score += 1

        st.success(f"🎉 Your Score: {score} / {len(quiz_data)}")

        if score == len(quiz_data):
            st.balloons()