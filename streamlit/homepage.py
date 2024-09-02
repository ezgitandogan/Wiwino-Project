import streamlit as st
import importlib

# Dynamically load page modules
chatbot = importlib.import_module("Chatbot")
page1 = importlib.import_module("1")
page2 = importlib.import_module("2")
page3 = importlib.import_module("3")
page4 = importlib.import_module("4")
page5 = importlib.import_module("5")
page6 = importlib.import_module("6")
page7 = importlib.import_module("7")

# Sidebar options for selecting pages
st.sidebar.title("WIWINO 🍷🌟")
selected_page = st.sidebar.selectbox(
    "Select the page you want to visit:", 
    ["Wiwino Insights 🌟", "Top 8 Wines to Increase Sales 🍷", "Marketing Budget Optimization 📊", 
    "Top 3 Wineries Awards 🏆", "Customer Taste Preferences Analysis 👅", 
    "Top 3 Global Grape Varieties and Provides the 5 Best-Rated Wines for Each Variety 🍇", "Vintages Average Rating for Each Country 🍷🌍", 
    "Top 5 Cabernet Sauvignon Recommendations 🍷", "Chatbot"]
)

# Define a simple rule-based chatbot
def simple_chatbot(user_input):
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing well. How can I assist you?",
        "bye": "Goodbye! Have a great day!",
        "help": "Sure, I can help with general questions. Just ask!",
        "okay": "Bravo Not Bad!",
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

# Initialize session state for chatbot
if 'history' not in st.session_state:
    st.session_state.history = []
if 'conversation_started' not in st.session_state:
    st.session_state.conversation_started = False

# Load content based on selected page
if selected_page == "Wiwino Insights 🌟":
    st.image("streamlit/img/logo.png", use_column_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    **Wiwino: The Key to Excellence in the Wine Market** 🍷

    - Wiwino is a leading force in the wine industry with years of dedicated activity. Through the extensive data collected from wine enthusiasts, we have the opportunity to deeply understand the dynamics of the wine market and make strategic decisions based on comprehensive analysis.

    - Our data, gathered from user feedback, regional trends, and wine preferences, provides valuable insights into enhancing our market presence, improving customer satisfaction, and strengthening our position in the industry.

    Currently, we are addressing key questions to make more informed decisions:

    1. **Selecting Wines to Boost Sales** 🍇: Which wines should we highlight to increase sales, and what are the reasons behind these choices?
    ---
    2. **Optimizing Marketing Budget** 💰: With a limited marketing budget, which countries should we prioritize to maximize impact?
    ---
    3. **Recognizing Top Wineries** 🏆: How can we identify the top 3 wineries based on their performance, and what criteria should we use?
    ---
    4. **Analyzing Taste Preferences** 👅: How can we evaluate and identify wines associated with specific taste preferences, such as coffee, toast, green apple, cream, and citrus, ensuring that at least 10 users confirm these preferences?
    ---
    5. **Global Grape Varieties** 🌍: What are the top 3 most common grape varieties worldwide, and which are the 5 best-rated wines for each variety?
    ---
    6. **Country and Vintage Leaderboards** 📊: How can we visualize the average wine ratings by country and vintage year effectively?
    ---
    7. **Cabernet Sauvignon Recommendations** 🍷: What are the top 5 wine recommendations for our VIP client who enjoys Cabernet Sauvignon?
    """, unsafe_allow_html=True)

elif selected_page == "Chatbot":
    # Chatbot UI
    st.title("Chat with SipSage 🍷🤖")

    # Start conversation button
    if st.button("Start Conversation"):
        st.session_state.conversation_started = True
        # Add initial message from the chatbot
        initial_response = "I am not so smart like you, please don't ask me hard questions."
        st.session_state.history.append(f"SipSage: {initial_response}")

    # User input
    if st.session_state.conversation_started:
        user_input = st.text_input("You:", "")
        if user_input:
            response = simple_chatbot(user_input)
            st.session_state.history.append(f"You: {user_input}")
            st.session_state.history.append(f"SipSage: {response}")

    # Display chat history
    for message in st.session_state.history:
        st.write(message)

elif selected_page == "Top 8 Wines to Increase Sales 🍷":
    page1.goster()

elif selected_page == "Marketing Budget Optimization 📊":
    page2.goster()
    
elif selected_page == "Top 3 Wineries Awards 🏆":
    page3.goster()
    
elif selected_page == "Customer Taste Preferences Analysis 👅":
    page4.goster()
    
elif selected_page == "Top 3 Global Grape Varieties and Provides the 5 Best-Rated Wines for Each Variety 🍇":
    page5.goster()
    
elif selected_page == "Vintages Average Rating for Each Country 🍷🌍":
    page6.goster()
    
elif selected_page == "Top 5 Cabernet Sauvignon Recommendations 🍷":
    page7.goster()




st.sidebar.image ("https://media.giphy.com/media/amLKBCjdSLVfYAzwzH/giphy.gif")
st.sidebar.markdown("### Follow Us On Social Media")
st.sidebar.write("[Instagram](https://www.instagram.com)")
st.sidebar.write("[Facebook](https://www.facebook.com)")
st.sidebar.write("[YouTube](https://www.youtube.com)")


st.sidebar.markdown("### Contact Us")
st.sidebar.image("streamlit/img/p1.png", caption="Mehmet Batar", use_column_width=True)


st.sidebar.markdown("""

**Position:** Data Engineer

📧 **Email:** mehmetbatar@gmail.com

📞 **Phone:** +123888723

💼 **LinkedIn:** (https://www.linkedin.com/in/mehmetbatar)


""")

st.sidebar.image("streamlit/img/p2.png", caption="Ezgi Tandogan", use_column_width=True)
st.sidebar.markdown("""      
**Position:** Data Engineer

📧 **Email:** ezgitandogann@outlook.com

📞 **Phone:** +1452785

💼 **LinkedIn:** (https://www.linkedin.com/in/ezgitandogan)


""", unsafe_allow_html=True)

st.sidebar.markdown("### Feedback !")
st.sidebar.text_input("Name")
st.sidebar.text_area("How can we improve our services?")
st.sidebar.button("Send")
st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.image("https://media.giphy.com/media/l0Exq7lE8nhJg027C/giphy.gif")

