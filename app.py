import streamlit as st
from utils import analyze_news
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="AI News Money Mentor", layout="centered")

st.title("💸 AI News-to-Action Money Mentor")

st.write("Paste a financial news article and get insights instantly.")

news_input = st.text_area("Enter Financial News", height=200)

if st.button("Analyze"):
    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_news(news_input, SYSTEM_PROMPT)

        st.subheader("📊 Analysis")
        st.write(result)