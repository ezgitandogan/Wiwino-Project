import streamlit as st
from PIL import Image
import PIL.Image
#--7. One of our VIP clients likes Cabernet Sauvignon and would like our top 5 recommendations. Which wines would you recommend to him?

def goster():
    st.title("Top 5 Cabernet Sauvignon Recommendations 🍷") 
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    - Our VIP client has a preference for Cabernet Sauvignon wines and has asked for our top recommendations. To meet their expectations, we have selected the five best-rated Cabernet Sauvignon wines based on user reviews and ratings. These wines are known for their exceptional quality, taste, and popularity among wine enthusiasts.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.image("streamlit/img/7.png")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    ##### 1. **Special Selection Cabernet Sauvignon** 🍇
    - **Average Rating:** 4.7
    - **Ratings Count:** 41,236
    - **Insight:** This wine has the highest average rating among the options and a substantial number of reviews, indicating exceptional quality and widespread consumer approval.
    ---
    ##### 2. **Cabernet Sauvignon** 🍷
    - **Average Rating:** 4.6
    - **Ratings Count:** 157,944
    - **Insight:** With the highest number of reviews, this wine has a strong average rating, reflecting its broad acceptance and consistent quality across a large number of consumers.
    ---
    ##### 3. **Cabernet Sauvignon (Signature)** ✨
    - **Average Rating:** 4.6
    - **Ratings Count:** 13,730
    - **Insight:** This wine has the same high average rating as the general Cabernet Sauvignon but with fewer reviews. It is well-regarded with a significant number of reviews, suggesting a premium quality.
    ---
    ##### 4. **CASK 23 Cabernet Sauvignon** 🏅
    - **Average Rating:** 4.6
    - **Ratings Count:** 9,464
    - **Insight:** Another highly-rated Cabernet Sauvignon with a decent number of reviews, indicating strong consumer satisfaction and quality.
    ---
    ##### 5. **Cabernet Sauvignon** 🌟
    - **Average Rating:** 4.8
    - **Ratings Count:** 2,941
    - **Insight:** Although this wine has the highest average rating, it has fewer reviews compared to the others. This suggests it is highly regarded by those who have reviewed it, making it a top recommendation for those who value high ratings.
    """, unsafe_allow_html=True)
