import streamlit as st
import requests

# Streamlit App Title
st.title("📖 Islamic Hadith Search App")

# Hadith Books Mapping (as per API documentation)
books = {
    "Sahih Bukhari": "sahih-bukhari",
    "Sahih Muslim": "sahih-muslim",
    "Jami' Al-Tirmidhi": "al-tirmidhi",
    "Sunan Abu Dawood": "abu-dawood",
    "Sunan Ibn-e-Majah": "ibn-e-majah",
    "Sunan An-Nasa'i": "sunan-nasai",
    "Mishkat Al-Masabih": "mishkat",
    "Musnad Ahmad": "musnad-ahmad",
    "Al-Silsila Sahiha": "al-silsila-sahiha"
}

# User Input: Hadith Book & Hadith Number
book_name = st.selectbox("Hadith Book Select Karein:", list(books.keys()))
hadith_number = st.text_input("Hadith Number Likhein (Jaise: 12):")

# API Key (Directly Injected for Testing - Secure Way: Use Streamlit Secrets)
API_KEY = "$2y$10$hNjBWWuv1uJ78usxn7rtJu1Hv7r7BMRK717pCT9ZCJ5V18FwYuu"

if st.button("🔍 Search Hadith"):
    if hadith_number:
        # API Request URL
        api_url = f"https://hadithapi.com/api/hadiths?apiKey={API_KEY}&book={books[book_name]}&hadithNumber={hadith_number}"
        
        # API Request
        response = requests.get(api_url)
        data = response.json()

        # Debugging: Show Raw API Response (Uncomment if needed)
        # st.write(data)

        # If Hadith is found
        if "data" in data and len(data["data"]) > 0:
            hadith_data = data["data"][0]
            hadith_text = hadith_data.get("hadith", "No text available")
            hadith_status = hadith_data.get("status", "Unknown")
            
            st.success(f"📜 **{book_name} Hadith #{hadith_number}:**")
            st.write(hadith_text)
            st.info(f"📌 Status: {hadith_status}")
        else:
            st.error("⚠️ Hadith nahi mili, sahi number ya kitaab check karein.")
    else:
        st.warning("⚠️ Pehle Hadith Number likhein!")
