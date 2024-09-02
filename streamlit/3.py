import streamlit as st

#--3. We would like to give awards to the best wineries. Come up with 3 relevant ones. Which wineries should we choose and why?

def goster():
    st.title("Top 3 Wineries Awards 🏆") 
    
    # Introduction
    st.markdown(""" - We will identify the top three wineries based on their performance and explain the reasons behind their selection. By recognizing these wineries, we aim to highlight their excellence and celebrate their achievements in the wine market.
    """)

    # Displaying the primary image
    st.image("streamlit/img/3.png")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        ## 🏆 Best Wineries Awards 🏆
    
        Based on our analysis, we recommend awarding the following three wineries for their outstanding performance:

        ### 1. **Unico** 🍷
        - **Rating Average:** 4.7 ⭐
        - **Ratings Count:** 45,140
        - **Why:** Unico stands out with the highest number of ratings and a perfect average rating of 4.7. This suggests a high level of customer satisfaction and a strong reputation in the wine industry. The sheer volume of ratings further confirms its popularity and consistent quality.

        ### 2. **Sauternes** 🍾
        - **Rating Average:** 4.7 ⭐
        - **Ratings Count:** 44,126
        - **Why:** Sauternes also achieves a top average rating of 4.7, supported by a substantial number of ratings. This indicates a well-regarded winery with a broad customer base that appreciates its offerings. The consistent high rating reflects its excellence and customer loyalty.

        ### 3. **Special Selection Cabernet Sauvignon** 🍇
        - **Rating Average:** 4.7 ⭐
        - **Ratings Count:** 41,236
        - **Why:** The Special Selection Cabernet Sauvignon maintains a high average rating of 4.7 across a significant number of reviews. This winery’s strong performance in ratings highlights its exceptional quality and the positive reception it has received from wine enthusiasts.

        **Summary:** All three wineries have demonstrated exceptional quality and customer satisfaction, making them worthy recipients of our best winery awards. Their high average ratings and substantial number of reviews reflect their excellence and popularity in the wine market.
    """, unsafe_allow_html=True)
