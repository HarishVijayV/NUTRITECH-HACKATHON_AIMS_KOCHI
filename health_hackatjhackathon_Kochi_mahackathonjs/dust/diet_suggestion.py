import streamlit as st
from PIL import Image

# Define function for diet suggestions
def show_diet_suggestion():
    st.subheader("Health Information Form")
    with st.form(key='health_form'):
        # Input fields
        weight = st.number_input("Enter your weight (in kg)", min_value=0.0)
        bmi = st.number_input("Enter your BMI", min_value=0.0)
        condition_type = st.selectbox("Is it ulcer-based or chronic-based?", ["Ulcer-based", "Chronic-based"])
        hemoglobin_level = st.number_input("Enter your Hemoglobin level (g/dL)", min_value=0.0)
        albumin_level = st.number_input("Enter your Albumin level (g/dL)", min_value=0.0)
        cdai = st.number_input("Enter your CDAI (Crohn's Disease Activity Index)", min_value=0)
        crp = st.number_input("Enter your CRP level (mg/L)", min_value=0.0)
        gender = st.radio("Select your gender:", ["Male", "Female"])
        diet = st.radio("Diet preference:", ["Veg", "Non-veg"])
        food_allergies = st.text_input("Enter any food allergies (comma-separated):")
        hyper_acidity = st.checkbox("Do you have hyper acidity?")
        diabetes = st.checkbox("Do you have diabetes?")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.subheader("Entered Details:")
        st.write(f"Weight: {weight} kg")
        st.write(f"BMI: {bmi}")
        st.write(f"Condition Type: {condition_type}")
        st.write(f"Hemoglobin Level: {hemoglobin_level} g/dL")
        st.write(f"Albumin Level: {albumin_level} g/dL")
        st.write(f"CDAI: {cdai}")
        st.write(f"CRP Level: {crp} mg/L")
        st.write(f"Gender: {gender}")
        st.write(f"Diet: {diet}")
        st.write(f"Food Allergies: {food_allergies}")
        st.write(f"Hyper Acidity: {'Yes' if hyper_acidity else 'No'}")
        st.write(f"Diabetes: {'Yes' if diabetes else 'No'}")

        # Diet suggestion logic
        st.subheader("Diet Suggestions:")
        if condition_type == "Ulcer-based":
            st.write("For ulcer-based conditions, avoid spicy and acidic foods. Focus on a bland diet.")
        elif condition_type == "Chronic-based":
            st.write("For chronic conditions, a balanced diet with high fiber and low-fat foods is beneficial.")
        
        if hyper_acidity:
            st.write("Avoid foods that trigger acid reflux, such as citrus fruits and caffeine.")
        
        if diabetes:
            st.write("Manage carbohydrate intake and opt for complex carbs like whole grains and legumes.")

        # Load and display the diet image
        try:
            banner_image = Image.open("path_to_your_image.jpg")  # Replace with your image path
            st.image(banner_image, use_column_width=True, caption="Healthy Diet for IBD Management")
        except FileNotFoundError:
            st.warning("Diet image not found. Please add an image at the specified path.")
        
        st.success("Data submitted successfully!")

# Define function for chatbot
def show_chatbot():
    st.header("Chat with our Bot")
    user_input = st.text_input("You:", "")
    if user_input:
        response = get_chatbot_response(user_input)
        st.write(f"Bot: {response}")

def get_chatbot_response(user_input):
    responses = {
        "hello": "Hi! How can I assist you today?",
        "diet": "I can help you with diet suggestions. Please provide your health details.",
        "thanks": "You're welcome! If you have any more questions, feel free to ask.",
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")

# Title of the app
st.title("Health and Diet Management App")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "Diet Suggestion", "Chatbot", "Other Page"])

# Display content based on selected page
if page == "Home":
    st.header("Welcome to the Health and Diet Management App")
    st.write("This app helps you manage your health and diet with personalized recommendations.")
    st.write("Use the sidebar to navigate to different pages.")

elif page == "Diet Suggestion":
    show_diet_suggestion()

elif page == "Chatbot":
    show_chatbot()

elif page == "Other Page":
    st.header("Other Page")
    st.write("This is a placeholder for another page. Add your content or functionality here.")
