
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("AI Study Assistant")
st.write("Learn BCA topics with your AI tutor.")

topic = st.text_input("Enter a topic to study")

level = st.selectbox(
    "Your learning level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Generate Notes"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        try:
            client = genai.Client(
                api_key=st.secrets["GEMINI_API_KEY"]
            )

            prompt = f"""
            Explain {topic} to a BCA student.
            Level: {level}

            Include:
            1. Simple explanation
            2. Five key points
            3. One code or real-life example
            4. Three quiz questions with answers
            Use clear English.
            """

            with st.spinner("Preparing your notes..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.subheader("Study Notes")
            st.markdown(response.text)

        except Exception as e:
    st.error(f"Error details: {e}")
          
