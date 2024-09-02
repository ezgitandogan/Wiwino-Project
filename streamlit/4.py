import streamlit as st
from PIL import Image
import PIL.Image


#4. We detected that a big cluster of customers likes a specific combination of tastes. We identified a few keywords that match these tastes: coffee, toast, green apple, cream, and citrus (note that these keywords are case sensitive ⚠️). We would like you to find all the wines that are related to these keywords. Check that at least 10 users confirm those keywords, to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.


def goster():
    st.title("Customer Taste Preferences Analysis 👅") 
    
    # Introduction
    st.markdown(""" - We have identified a significant cluster of customers who share a specific combination of taste preferences. By analyzing user feedback, we have pinpointed the following keywords that match these tastes: **coffee**, **toast**, **green apple**, **cream**, and **citrus**. It is important to note that these keywords are case sensitive and play a crucial role in identifying the wines associated with these preferences.
    """)
    

    # Displaying the primary image
    st.image("streamlit/img/4.png")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""**Taste Preferences Analysis Results:🍷**
                
---

**🥂 Dominant Tastes**

- **Coffee** ☕ (682 wines) and **Cream** 🥛 (648 wines) are the most prevalent flavors, especially within the **non-oak** and **microbio** groups. This highlights a strong consumer preference for these tastes.

- **Citrus** 🍋 (454 wines) and **Green Apple** 🍏 (217 wines) also have significant associations, particularly within the **citrus** and **tree fruit** groups.

---

**🍇 Moderate Tastes**

- **Toast** 🍞 (575 wines) and **Toasted Almond** 🌰 (132 wines) show a solid presence, mainly in the **non-oak** group, appealing to a notable segment of the market.

---

**🌱 Less Frequent Tastes**

- Flavors like **Citrus Blossom** 🌸 and **Hazelnut Cream** 🥥 have fewer associations, suggesting they cater to a smaller, more niche segment of wine consumers.

---

**Conclusion:** The strong association of these tastes with specific wine groups suggests that wines embodying these flavors could be particularly appealing to the identified customer cluster. This insight can guide targeted marketing efforts and product offerings.

---

**🍷 Group Insights**

- **Non-Oak & Microbio Groups:** These groups are strongly associated with **Coffee** ☕ and **Cream** 🥛 flavors, indicating that wines from these groups are likely to be top choices for this cluster.

- **Citrus Fruit & Tree Fruit Groups:** Wines from these groups are linked to **Citrus** 🍋 and **Green Apple** 🍏 tastes, appealing to those who prefer fresh, fruity flavors.

- **Non-Oak Group:** This group also features **Toast** 🍞 and **Toasted Almond** 🌰 notes, suggesting a preference for subtle, toasty flavors.
""", unsafe_allow_html=True)