import streamlit as st
import requests

st.set_page_config(page_title="STEM Problem Solver 🤖", layout="centered", page_icon="🧠")

st.markdown("<h1 style='text-align: center;'>📚 STEM Problem Solver 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Enter a math or physics problem, and I'll solve it step by step! 🚀</p>", unsafe_allow_html=True)

problem = st.text_area("📝 Enter your problem:", placeholder="e.g., What is the integral of x?", height=100)

if st.button("🔍 Solve (Text)"):
    if problem.strip():
        with st.spinner("Thinking... 🤔"):
            
            try:
                response = requests.post(
                    "http://backend:2003/solve/",
                    json={"problem": problem}
                )

                if response.status_code == 200:
                    result = response.json()
                    solution_text = result.get("solution", "No solution found")
                    st.success("✅ Solution Found!")

                    st.markdown("### ✨ Solution:")
                    st.markdown(f"<div style='background-color:#222831; padding:15px; border-radius:10px; color:white;'>"
                                f"<p style='font-size:16px;'>{solution_text}</p></div>", unsafe_allow_html=True)
                else:
                    st.error("❌ Something went wrong while solving the problem.")
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid problem.")
