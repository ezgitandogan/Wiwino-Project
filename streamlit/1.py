


#1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?

import streamlit as st
from PIL import Image
import PIL.Image
import streamlit as st


def goster():
    # Başlık
    st.title("Top 8 Wines to Increase Sales 🍷")
    st.markdown("<br>", unsafe_allow_html=True)

    # Resimleri Yükle ve Yeniden Boyutlandır
    image_paths = [
        "streamlit/img/carbenet.png",
        "streamlit/img/brut.png",
        "streamlit/img/Sassicaia.png",
        "streamlit/img/opus.png",
        "streamlit/img/unico.png",
        "streamlit/img/sauternes.png",
        "streamlit/img/pomerol.png",
        "streamlit/img/grange.png"
    ]
    
    resized_images = []
    sizes = [(160, 220), (130, 220), (160, 220), (130, 220), (160, 220), (140, 220), (120, 220), (120, 220)]
    
    for path, size in zip(image_paths, sizes):
        image = Image.open(path)
        resized_image = image.resize(size)
        resized_images.append(resized_image)
    
    # İlk Satır için 4 Sütun
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image(resized_images[0], caption="Cabernet Sauvignon")
    with col2:
        st.image(resized_images[1], caption="Brut Champagne")
    with col3:
        st.image(resized_images[2], caption="Sassicaia")
    with col4:
        st.image(resized_images[3], caption="Opus One")
    
    # İkinci Satır için 4 Sütun
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.image(resized_images[4], caption="Unico")
    with col6:
        st.image(resized_images[5], caption="Sauternes")
    with col7:
        st.image(resized_images[6], caption="Pomerol")
    with col8:
        st.image(resized_images[7], caption="Grange")
    
    # Alt Başlık ve Ek Metin
    st.subheader("Why These Wines Stand Out")
    st.markdown("""
    On this page, we showcase eight standout wines that are ideal for boosting sales. These wines are highlighted for their exceptional quality and market appeal. Here's a closer look at each wine and why it deserves a spot in your sales strategy:

    1. **Cabernet Sauvignon** 🍷
       - **Description**: Cabernet Sauvignon is a globally recognized red wine known for its strong flavors and rich profile.
       - **Why It Stands Out**: Its widespread recognition and high-quality standards make it a perfect choice for expanding your customer base. Additionally, its aging potential adds to its appeal.
    ---
    2. **Brut Champagne** 🥂
       - **Description**: Brut Champagne is one of the most popular types of champagne, characterized by its dry and crisp taste.
       - **Why It Stands Out**: As a staple for celebrations and special occasions, Brut Champagne can enhance your market presence with its prestigious reputation.
    ---
    3. **Sassicaia** 🍇
       - **Description**: Sassicaia is a renowned Super Tuscan wine from Italy, known for its complex aromas and deep flavors.
       - **Why It Stands Out**: Its high quality and prestige make it a favorite among wine enthusiasts, making it a powerful addition to boost your sales.
    ---
    4. **Opus One** 🌟
       - **Description**: Opus One is a prestigious wine from California, celebrated for its exceptional quality.
       - **Why It Stands Out**: With high demand among wine lovers, Opus One offers an opportunity to strengthen your brand’s reputation with a top-tier product.
    ---
    5. **Unico** 🍷
       - **Description**: Unico is one of Spain's most esteemed wines, known for its rich and intense flavors.
       - **Why It Stands Out**: Its prestige and quality make it a compelling choice for increasing your sales and attracting discerning customers.
    ---
    6. **Sauternes** 🍯
       - **Description**: Sauternes is a famous sweet white wine from France, renowned for its luscious sweetness and complexity.
       - **Why It Stands Out**: Its unique flavor profile and luxury status make it an excellent candidate for appealing to high-end wine consumers.
    ---
    7. **Pomerol** 🍷
       - **Description**: Pomerol is a prestigious wine from Bordeaux, known for its rich and velvety texture.
       - **Why It Stands Out**: Its esteemed reputation and smooth taste make it a desirable option for enhancing your product offerings.
    ---
    8. **Grange** 🌟
       - **Description**: Grange is a celebrated Australian wine known for its robust flavors and aging potential.
       - **Why It Stands Out**: Its exceptional quality and strong market presence make it a valuable addition to your sales portfolio.
    """,unsafe_allow_html=True)
