import streamlit as st

# Title of the main app
st.title("Health and Diet Management App")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "Diet Suggestion", "Other Page"])

# Display content based on selected page
if page == "Home":
    st.header("Welcome to the Health and Diet Management App")
    st.write("This app helps you manage your health and diet with personalized recommendations.")
    st.write("Use the sidebar to navigate to different pages.")

elif page == "Diet Suggestion":
    st.header("Diet Suggestion for Inflammatory Bowel Disease")
    st.write("Provide your health information to get personalized diet suggestions.")
    st.write("Click the button below to access the Diet Suggestion Form.")
    if st.button("Go to Diet Suggestion Form"):
        st.write("You can find the Diet Suggestion Form on the Diet Suggestion page.")

elif page == "Other Page":
    st.header("Other Page")
    st.write("This is a placeholder for another page. Add your content or functionality here.")
