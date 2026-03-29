import streamlit as st
from utils import analyze_news
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="FinSight AI", layout="centered")

st.title("📊 FinSight AI")
st.divider()
st.markdown("Turning Financial news into actionable insights with AI")

st.write("Analyze financial news, understand market sentiment, and get smart insights instantly.")
news_input = st.text_area("Enter Financial News", height=200)

if st.button("Analyze"):
    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_news(news_input, SYSTEM_PROMPT)

        st.subheader("📊 Analysis")
        st.write(result)