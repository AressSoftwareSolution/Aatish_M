

import streamlit as st
from agents import planner_agent, research_agent, writer_agent
from streamlit_lottie import st_lottie
import requests
import time

st.set_page_config(
    page_title="Travel Agent AI",
    page_icon="✈",
    layout="wide"
)

# ------------------ CSS ------------------
st.markdown("""
<style>

/* background animation */

.stApp {
    background: linear-gradient(-45deg,#00C9FF,#92FE9D,#f5f7fa,#c3cfe2);
    background-size: 400% 400%;
    animation: gradient 12s ease infinite;
}

@keyframes gradient {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* glass card */

.card {
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:15px;
    box-shadow:0 8px 20px rgba(0,0,0,0.1);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
    box-shadow:0 12px 30px rgba(0,0,0,0.2);
}

/* button */

.stButton>button{
background: linear-gradient(90deg,#00C9FF,#92FE9D);
border:none;
color:black;
font-size:18px;
border-radius:12px;
height:3em;
width:100%;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.05);
box-shadow:0 8px 20px rgba(0,0,0,0.3);
}

/* airplane animation */

.plane{
font-size:40px;
position:absolute;
animation:fly 5s linear;
}

@keyframes fly{
0%{left:-100px;}
100%{left:100%;}
}

/* car animation */

.car-container{
width:100%;
height:80px;
overflow:hidden;
position:relative;
}

.car{
position:absolute;
font-size:40px;
animation:drive 4s linear;
}

@keyframes drive{
0%{left:-100px;}
100%{left:100%;}
}

.smoke{
position:absolute;
left:-20px;
animation:smokeMove 1.5s infinite;
}

@keyframes smokeMove{
0%{transform:translateX(0);opacity:1;}
100%{transform:translateX(-40px);opacity:0;}
}

/* search glow */

input:focus{
border:2px solid #00C9FF !important;
box-shadow:0 0 10px #00C9FF;
}

</style>
""", unsafe_allow_html=True)

# ------------------ Lottie ------------------

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

ai_animation = load_lottie(
"https://assets9.lottiefiles.com/packages/lf20_kyu7xb1v.json"
)

# ------------------ HEADER ------------------

col1, col2 = st.columns([2,1])

with col1:

    st.markdown(
    """
    <h1 style='text-align:center;
    background: linear-gradient(90deg,#000428,#004e92);
    -webkit-background-clip:text;
    color:transparent'>
    ✈ Travel Agent AI
    </h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    "<p style='text-align:center;color:gray'>Planner ➜ Researcher ➜ Writer</p>",
    unsafe_allow_html=True
    )

with col2:
    st_lottie(ai_animation,height=160)

st.divider()

# ------------------ INPUT ------------------

task = st.text_input(
"🧳 Enter your travel task",
placeholder="Plan a 5 day trip to Goa with budget hotels"
)

# ------------------ BUTTON ------------------

if st.button("🚀 Run AI Agents"):

    # airplane animation
    st.markdown("""
    <div class="plane">✈</div>
    """,unsafe_allow_html=True)

    # car animation
    st.markdown("""
    <div class="car-container">
    <div class="car">🚗 <span class="smoke">💨</span></div>
    </div>
    """,unsafe_allow_html=True)

    if not task.strip():

        st.warning("⚠ Please enter a task first")

    else:

        progress = st.progress(0)

        with st.spinner("🧠 Planner Agent Thinking..."):
            plan = planner_agent.run(task)
            progress.progress(33)

        with st.spinner("🔎 Research Agent Searching..."):
            research = research_agent.run(plan)
            progress.progress(66)

        with st.spinner("✍ Writer Agent Writing..."):
            report = writer_agent.run(research)
            progress.progress(100)

        st.success("Trip Plan Ready 🎉")

        st.divider()

        col1,col2,col3 = st.columns(3)

        with col1:
            st.markdown("### 🧠 Planner")
            st.markdown(
            f"<div class='card'>{plan}</div>",
            unsafe_allow_html=True
            )

        with col2:
            st.markdown("### 🔎 Research")
            st.markdown(
            f"<div class='card'>{research}</div>",
            unsafe_allow_html=True
            )

        with col3:
            st.markdown("### ✍ Final Conclusion")
            st.markdown(
            f"<div class='card'>{report}</div>",
            unsafe_allow_html=True
            )

# ------------------ DESTINATION CARDS ------------------

st.divider()

st.subheader("🌍 Popular Destinations")

col1,col2,col3 = st.columns(3)

with col1:
    st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    caption="Goa Beaches"
    )

with col2:
    st.image(
    "https://images.unsplash.com/photo-1548013146-72479768bada",
    caption="Paris"
    )

with col3:
    st.image(
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    caption="Switzerland"
    )

st.divider()

st.caption("⚡ Powered by Multi-Agent AI (Planner • Researcher • Writer)")