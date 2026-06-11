import streamlit as st
from analyzer import analyze_post

st.set_page_config(
    page_title="Social Media Post Analyzer",
    page_icon="📱"
)

st.title("📱 Social Media Post Analyzer")

post = st.text_area(
    "Enter Social Media Post"
)

if st.button("Analyze"):

    if post.strip():

        result = analyze_post(post)

        st.success("Analysis Complete")

        st.subheader("Tone")
        st.write(result["tone"])

        st.subheader("Intent")
        st.write(result["intent"])

        st.subheader("Communication Style")
        st.write(result["communication_style"])

        st.subheader("Summary")
        st.write(result["summary"])

        st.json(result)

    else:
        st.warning("Please enter a post.")