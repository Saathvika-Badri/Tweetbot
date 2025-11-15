import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# -----------------------------------
# 1️⃣ Load environment variables
# -----------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -----------------------------------
# 2️⃣ Streamlit UI
# -----------------------------------
st.set_page_config(page_title="TweetBot", page_icon="🐦")
st.title("🐦 TweetBot - Gemini Powered Tweet Generator")

st.write("Generate creative, catchy, and hashtag-ready tweets instantly using Gemini AI!")

# User input
topic = st.text_input("Enter the topic for your tweets:")
num_tweets = st.number_input("Number of tweets to generate:", min_value=1, max_value=10, value=3)

# -----------------------------------
# 3️⃣ Generate Tweets
# -----------------------------------
if st.button("Generate Tweets"):
    if not topic:
        st.warning("⚠️ Please enter a topic first!")
    else:
        with st.spinner("✨ Crafting tweet magic..."):
            prompt = f"""
            Generate {num_tweets} short, catchy, and well-formatted tweets about {topic}.
            Each tweet should:
            - Be under 280 characters
            - Feel natural and human-like
            - Include emojis where appropriate
            - Include 1–3 relevant hashtags at the end
            - Be separated clearly by blank lines
            - Avoid numbering (no Tweet 1, Tweet 2, etc.)
            -number the tweets before starting the tweet and the tweet should begin immedietly(1.,2.,3.)
            Example format:

            Life isn’t about waiting for the storm to pass — it’s about learning to dance in the rain. 🌧️💃
            #Motivation #Positivity

            Now generate the tweets:
            """

            # Use the correct Gemini model
            model = genai.GenerativeModel("models/gemini-2.5-flash")
            response = model.generate_content(prompt)
            tweets = response.text.strip().split("\n\n")

            st.success("✅ Tweets generated successfully!")

            # Display each tweet normally (no boxes)
            for tweet in tweets:
                st.markdown(f"{tweet.strip()}\n")

st.caption("Built using Streamlit & Gemini API 💡")
