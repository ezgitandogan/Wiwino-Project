#--6. We would like to create a country leaderboard. Come up with a visual that shows the average wine rating for each country. Do the same for the vintages.

import streamlit as st
from PIL import Image
import PIL.Image

def goster():
    st.title("Vintages Average Rating for Each Country 🍷🌍")
    st.markdown("<br>", unsafe_allow_html=True)
    # Displaying the primary image
    st.image("streamlit/img/6.png")
    st.markdown("<br>", unsafe_allow_html=True)
    
    
    st.markdown("""
    ##### **1. États-Unis (US)**
    - **Average Rating:** 4.49
    - **Insight:** The U.S. stands out with the highest number of ratings and a very high average rating, indicating a strong and diverse wine market with broad consumer feedback.
    -----
    ##### **2. Chili (CL)**
    - **Average Rating:** 4.43
    - **Insight:** Despite having a slightly lower average rating than the U.S., Chile has the highest number of ratings. This suggests that Chilean wines are widely consumed and highly rated across a broad range of consumers.
    -----
    ##### **3. Argentine (AR)**
    - **Average Rating:** 4.42
    - **Insight:** Argentina also has a high number of ratings and a strong average rating, reflecting its significant presence in the wine market and consumer appreciation.
    -----
    ##### **4. Moldavie (MD)**
    - **Average Rating:** 4.48
    - **Insight:** Moldovan wines have a high average rating with a considerable number of reviews, indicating that they are well-regarded and appreciated by many consumers.
    -----
    ##### **5. Australie (AU)**
    - **Average Rating:** 4.46
    - **Insight:** Australian wines have a strong average rating with a large volume of ratings, showing consistent quality and a substantial following.
    -----
    ##### **6. Portugal (PT)**
    - **Average Rating:** 4.44
    - **Insight:** Portugal maintains a solid rating and has a considerable number of reviews, suggesting both quality and popularity.
    -----
    ##### **7. Espagne (ES)**
    - **Average Rating:** 4.44
    - **Insight:** Spanish wines have a good average rating with a decent number of reviews, reflecting their solid reputation and consumer base.
    -----
    ##### **8. Hongrie (HU)**
    - **Average Rating:** 4.47
    - **Insight:** Hungarian wines have a high average rating but fewer reviews compared to some other countries, which could imply niche appeal or emerging popularity.
    -----
    ##### **9. Allemagne (DE)**
    - **Average Rating:** 4.50
    - **Insight:** German wines have a high average rating with a moderate number of reviews, suggesting they are highly regarded by those familiar with them.
    -----
    ##### **10. Israël (IL)**
    - **Average Rating:** 4.50
    - **Insight:** Israeli wines have the same high average rating as Germany but with fewer reviews, indicating a more niche market.
    -----
    ##### **11. Grèce (GR):** 
    - **Average rating** of 4.4 and fewer reviews, indicating less widespread recognition.
    -----
    ##### **12. Suisse (CH):** 
    - **Average rating** of 4.35, with lower review counts, suggesting less global presence.
    -----
    ##### **13. Croatie (HR):** 
    - **Average rating** of 4.3, showing a good rating but with fewer reviews.
    -----

    """, unsafe_allow_html=True)

    st.title("Wines Average Rating for Each Country 🍷🌍")
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("streamlit/img/6.1.png")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""

    ##### **1. Roumanie (RO)**
    - **Average Rating:** 4.5
    - **Ratings Count:** 31
    - **Insight:** Roumanian wines have a high average rating but with a very limited number of reviews, indicating strong positive feedback from a small group of reviewers.
    -----
    ##### **2. Croatie (HR)**
    - **Average Rating:** 4.4
    - **Ratings Count:** 234
    - **Insight:** Croatian wines also have a high average rating with a moderate number of reviews, suggesting a good reputation among a reasonable number of consumers.
    -----
    ##### **3. Argentine (AR)**
    - **Average Rating:** 4.32
    - **Ratings Count:** 872
    - **Insight:** Argentine wines have a solid average rating and a decent number of reviews, indicating consistent quality and a relatively strong presence.
    -----
    ##### **4. Chili (CL)**
    - **Average Rating:** 4.12
    - **Ratings Count:** 1,037
    - **Insight:** Chilean wines have a good average rating with a substantial number of reviews, reflecting a broad consumer base and positive feedback.
    -----
    ##### **5. Portugal (PT)**
    - **Average Rating:** 3.93
    - **Ratings Count:** 302
    - **Insight:** Portuguese wines have a lower average rating but a moderate number of reviews, suggesting room for improvement in quality or varying consumer opinions.
    -----
    ##### **6. Moldavie (MD)**
    - **Average Rating:** 3.87
    - **Ratings Count:** 2,031
    - **Insight:** Moldovan wines have a lower average rating but a significant number of reviews, indicating that while the overall feedback is less favorable, it is based on a larger sample size.
    -----
    ##### **7. États-Unis (US)**
    - **Average Rating:** 3.70
    - **Ratings Count:** 299
    - **Insight:** U.S. wines have a relatively lower average rating with a decent number of reviews, suggesting that while there are many reviews, the overall rating is not as high.
    -----
    ##### **8. Afrique du Sud (ZA)**
    - **Average Rating:** 3.66
    - **Ratings Count:** 95
    - **Insight:** South African wines have a lower rating and a smaller number of reviews, indicating limited consumer feedback and lower average quality.
    -----
    ##### **9. Italie (IT)**
    - **Average Rating:** 3.63
    - **Ratings Count:** 580
    - **Insight:** Italian wines have a low average rating with a reasonable number of reviews, suggesting issues with quality or consumer satisfaction.
    -----
    ##### **10. Espagne (ES)**
    - **Average Rating:** 3.38
    - **Ratings Count:** 212
    - **Insight:** Spanish wines have a lower average rating and a moderate number of reviews, reflecting a less favorable perception among reviewers.
    -----
    ##### **11. Hongrie (HU):** 
    - **Average rating** of 3.17 from 154 reviews.
    -----
    ##### **12. France (FR):** 
    - **Average rating** of 3.07 from 876 reviews.
    -----
    ##### **13. Australie (AU):**
    - **Average rating** of 2.83 from 509 reviews.
    -----
    ##### **14. Grèce (GR):** 
    - **verage rating** of 2.3 from 62 reviews.
    -----
    ##### **15. Suisse (CH):**
    - **Average rating** of 2.2 from 162 reviews.
    -----
    ##### **16. Allemagne (DE):**
    - **Average rating** of 1.70 from 2 reviews.
    -----
    ##### **17. Israël (IL):** 
    - **Average rating** of 0.0 from 1 review.
    """, unsafe_allow_html=True)
