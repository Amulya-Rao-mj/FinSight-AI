import streamlit as st
from utils import analyze_news
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="FinSight AI", layout="centered")

st.title("📊 FinSight AI")
st.markdown("### Turning Financial News into Actionable Insights")
st.write("Analyze financial news, understand market sentiment, and get smart insights instantly.")

st.divider()

user_type = st.selectbox(
    "Select User Type",
    ["Beginner Investor", "Intermediate Investor", "Senior Citizen"]
)



if "news_input" not in st.session_state:
    st.session_state.news_input = ""

if st.button("Try Sample News"):
    st.session_state.news_input = """The Reserve Bank of India increased the repo rate by 25 basis points to control inflation. Banking stocks gained while real estate stocks declined due to higher borrowing costs."""

headline = st.text_input("News Headline (optional)")
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
            full_input = f"User Type: {user_type}\nHeadline: {headline}\n\nNews: {news_input}"
            result = analyze_news(full_input, SYSTEM_PROMPT)
            result_lower = result.lower()

        st.divider()

        # Sentiment badge
        if "Positive" in result_lower:
            st.success("Market Sentiment: Positive 📈")
        elif "Negative" in result_lower:
            st.error("Market Sentiment: Negative 📉")
        elif "Neutral" in result_lower:
            st.info("Market Sentiment: Neutral ⚖️")

        st.subheader("📊 Analysis")
        st.markdown(result)