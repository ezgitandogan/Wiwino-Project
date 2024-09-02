#--5. We would like to select wines that are easy to find all over the world. Find the top 3 most common grapes all over the world and for each grape, give us the the 5 best rated wines.

import streamlit as st
from PIL import Image
import PIL.Image


import streamlit as st

def goster():
    st.title("Top 3 Global Grape Varieties and Provides the 5 Best-Rated Wines for Each Variety 🍇") 
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown(""" - We will identify the top three most common grape varieties worldwide and provide the five best-rated wines for each variety. This information will help us understand the global popularity of these grapes and the specific wines that have garnered the highest ratings.
    """)
    st.markdown("<br>", unsafe_allow_html=True)

    # Displaying the primary image
    st.image("streamlit/img/5.png")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(""" 
     **1. Cabernet Sauvignon (4.8 Rating, 2,941 Ratings)**
    - **Highest Rating:** This wine stands out with the highest average rating of 4.8. However, it has a relatively lower number of ratings (2,941), suggesting that it might be a premium or niche wine, highly appreciated by a smaller, selective group of consumers.
    
     **2. Special Selection Cabernet Sauvignon (4.7 Rating, 41,236 Ratings)**
    - **High Popularity and Excellent Quality:** This wine not only has an impressive average rating of 4.7 but also a large number of ratings (41,236). This combination indicates that it is both popular and of high quality, making it a strong candidate for recognition and recommendation.
    
     **3. Cabernet Sauvignon (4.6 Rating, 157,944 Ratings)**
    - **Mass Appeal:** With the highest number of ratings (157,944), this wine has a broad appeal among consumers. While its average rating of 4.6 is slightly lower than the others, the sheer volume of ratings highlights its widespread popularity.
    
     **4. Cabernet Sauvignon (Signature) (4.6 Rating, 13,730 Ratings)**
    - **Consistent Quality:** This wine maintains a solid rating of 4.6 with a substantial number of ratings (13,730), indicating that it is a well-regarded choice, particularly among those who might prefer a signature or specialized variety.
    
     **5. CASK 23 Cabernet Sauvignon (4.6 Rating, 9,464 Ratings)**
    - **Highly Rated with a Loyal Following:** Like the Signature variety, this wine also has a 4.6 rating but with a slightly smaller audience (9,464 ratings). Its name suggests it may be a premium or reserve wine, appealing to a dedicated group of consumers.
    
     **🌟 Conclusion:**
    - **Special Selection Cabernet Sauvignon** emerges as a standout due to its combination of high rating and widespread popularity.
    - **Cabernet Sauvignon** with a 4.8 rating is the highest-rated, making it potentially the best quality option, though it caters to a more niche market.
    - **Mass-market wines** like the Cabernet Sauvignon with 157,944 ratings highlight consumer trust and broad appeal, making them reliable choices for a wide audience.
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line for separation

    st.image("streamlit/img/5.1.png")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(""" 
     **1. Merlot - 4.4 average rating from 1922 reviews.** 
    This wine has a solid reputation with a good number of reviews backing it up.
    
     **2. Calle Merlot Rosso Veronese - 4.4 average rating from 1053 reviews.** 
    It matches the highest rating but has fewer reviews, which might suggest a more niche appeal or a newer entry.
    
     **3. 110 e Lode Merlot - 4.4 average rating from 174 reviews.** 
    Despite having the same rating as the others, it has significantly fewer reviews, which could mean it's less widely known or recently released.
    
     **4. Merlot (Signature) - 4.3 average rating from 2312 reviews.** 
    This wine has a slightly lower average rating but has the highest number of reviews, indicating a well-established reputation among a large number of reviewers.
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line for separation

    st.image("streamlit/img/5.2.png")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(""" 
     **1. Chloe Chardonnay - 4.5 average rating from 458 reviews.** 
    This wine has a high rating with a respectable number of reviews, suggesting it is well-regarded and has a solid following.
    
     **2. Reserve Chardonnay - 4.5 average rating from 396 reviews.** 
    It shares the top rating with Chloe Chardonnay but has slightly fewer reviews. This could indicate it’s either a newer or more niche option.
    
     **3. Bentrock Vineyard Chardonnay - 4.5 average rating from 118 reviews.** 
    This also has a high rating but with the fewest reviews among the top-rated Chardonnays, potentially reflecting a more specialized or less widely distributed wine.
    
     **4. One Sixteen Chardonnay - 4.4 average rating from 1753 reviews.** 
    Although it has a slightly lower rating, it benefits from a large number of reviews, suggesting widespread recognition and a consistent quality that many people appreciate.
    
     **5. Chardonnay - 4.4 average rating from 1031 reviews.** 
    This wine also has a solid rating and a substantial number of reviews, showing it is well-regarded and popular.
    """, unsafe_allow_html=True)
