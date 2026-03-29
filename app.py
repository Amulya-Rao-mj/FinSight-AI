import streamlit as st
from utils import analyze_news
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="FinSight AI", layout="centered")

st.title("📊 FinSight AI")
st.markdown("### Turning Financial News into Actionable Insights")
st.write("Analyze financial news, understand market sentiment, and get smart insights instantly.")

st.divider()

if "news_input" not in st.session_state:
    st.session_state.news_input = ""

if st.button("Try Sample News"):
    st.session_state.news_input = """The Reserve Bank of India increased the repo rate by 25 basis points to control inflation. Banking stocks gained while real estate stocks declined due to higher borrowing costs."""

news_input = st.text_area(
    "Enter Financial News",
    height=200,
    value=st.session_state.news_input
)

if st.button("Analyze"):
    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_news(news_input, SYSTEM_PROMPT)

        st.divider()

        # Sentiment badge
        if "Positive" in result:
            st.success("Market Sentiment: Positive 📈")
        elif "Negative" in result:
            st.error("Market Sentiment: Negative 📉")
        elif "Neutral" in result:
            st.info("Market Sentiment: Neutral ⚖️")

        st.subheader("📊 Analysis")
        st.markdown(result)