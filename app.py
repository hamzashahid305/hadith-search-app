import streamlit as st
import requests

# App ka Title
st.title("📖 Islamic Hadith Search App")

# User Input: Hadith Book & Hadith Number
book_name = st.selectbox("Hadith Book Select Karein:", [
    "Bukhari", "Muslim", "Tirmidhi", "Abu Dawood",
    "Ibn Majah", "Nasa'i", "Muwatta Malik", "Musnad Ahmad", "Darimi"
])
hadith_number = st.text_input("Hadith Number Likhein (Jaise: 12):")

if st.button("🔍 Search Hadith"):
    if hadith_number:
        # API Key (Directly likh di, jo secure nahi hai)
        api_key = "$2y$10$hNjBWWuv1uJ78usxn7rtJu1Hv7r7BMRK717pCT9ZCJ5V18FwYuu"
        
        # API Request URL
        api_url = f"https://hadithapi.com/api/hadiths?book={book_name}&hadith_number={hadith_number}&apiKey={api_key}"
        
        # API Request bhejna
        response = requests.get(api_url)
        data = response.json()

        # Agar hadees mili to show karo
        if "data" in data and len(data["data"]) > 0:
            hadith = data["data"][0]["hadith"]
            status = data["data"][0].get("status", "Unknown")  # Hadith Sahih hai ya Da'eef
            st.success(f"📜 **{book_name} Hadith #{hadith_number}:**")
            st.write(hadith)
            st.info(f"📌 Hadith Status: {status}")
        else:
            st.error("⚠️ Hadith nahi mili, sahi number ya kitaab check karein.")
    else:
        st.warning("⚠️ Pehle Hadith Number likhein!")
