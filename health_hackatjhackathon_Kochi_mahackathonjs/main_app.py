import streamlit as st
import pandas as pd

# Title of the app
st.title("Happy Gut")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "Health Inputs", "Chatbot"])

# Initialize session state for chat history if not already set
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Initialize session state for storing input data if not already set
if 'input_data' not in st.session_state:
    st.session_state.input_data = {}

# Function to handle user input and generate a simple response
def get_chatbot_response(user_input):
    # Placeholder response for now
    return "Hello Harish"

# Function to generate a report
def generate_report():
    # Collecting all data
    input_data = st.session_state.input_data
    
    # Combine all data into a DataFrame
    df = pd.DataFrame([input_data])
    
    # Convert DataFrame to CSV
    csv = df.to_csv(index=False)
    
    return csv

# Display content based on selected page
if page == "Home":
    st.header("Welcome to the Health and Diet Management App")
    st.write("This app provides a range of features to assist with health and diet management.")
    st.write("Use the sidebar to navigate to different pages.")

elif page == "Health Inputs":
    st.header("Health Inputs")

    # Input fields from Doctor
    st.subheader("Doctor's Inputs")
    weight = st.number_input("Enter your weight (in kg)", min_value=0.0)
    bmi = st.number_input("Enter your BMI", min_value=0.0)
    condition_type = st.selectbox("Is it ulcerative coitis or crohn's disease?", ["ulcerative coitis", "crohn's disease"])
    hemoglobin_level = st.number_input("Enter your Hemoglobin level (g/dL)", min_value=0.0)
    albumin_level = st.number_input("Enter your Albumin level (g/dL)", min_value=0.0)
    cdai = st.number_input("Enter your CDAI (Crohn's Disease Activity Index)", min_value=0)
    crp = st.number_input("Enter your CRP level (mg/L)", min_value=0.0)
    gender = st.radio("Select your gender:", ["Male", "Female"])
    diet = st.radio("Diet preference:", ["Veg", "Non-veg"])
    food_allergies = st.text_input("Enter any food allergies (comma-separated):")
    hyper_acidity = st.checkbox("Do you have hyper acidity?")
    diabetes = st.checkbox("Do you have diabetes?")

    # Additional Input fields
    st.subheader("Additional Inputs")
    stress_level = st.number_input("Enter patients stress level (1-10)", min_value=1, max_value=10)
    role = st.text_input("State")

    # Submit button to store all data
    if st.button("Submit"):
        # Store the input data in session state
        st.session_state.input_data = {
            "weight": weight,
            "bmi": bmi,
            "condition_type": condition_type,
            "hemoglobin_level": hemoglobin_level,
            "albumin_level": albumin_level,
            "cdai": cdai,
            "crp": crp,
            "stress_level": stress_level,
            "workplace": workplace,
            "role": role,
            "gender": gender,
            "diet": diet,
            "food_allergies": food_allergies,
            "hyper_acidity": hyper_acidity,
            "diabetes": diabetes,
            "salary": salary
        }
        st.success("Data has been submitted and stored successfully!")

        # Generate and display the download button
        report_csv = generate_report()
        st.download_button(
            label="Download Report",
            data=report_csv,
            file_name="report.csv",
            mime="text/csv"
        )

elif page == "Chatbot":
    st.header("Chat with our Bot")

    # Container for the chat history
    chat_container = st.container()

    # Text input for the user with a form to manage submission
    with st.form(key='user_input_form', clear_on_submit=True):
        user_input = st.text_input("You:", key="user_input_key")
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"sender": "User", "message": user_input})
        
        # Get bot response
        response = get_chatbot_response(user_input)
        
        # Add bot response to chat history
        st.session_state.chat_history.append({"sender": "Bot", "message": response})

    # Display chat history in the container
    with chat_container:
        for entry in st.session_state.chat_history:
            if entry["sender"] == "Bot":
                st.markdown(f"**Bot:** *{entry['message']}*")
            else:
                st.markdown(f"**You:** {entry['message']}")

    # Ensure the chat history container remains scrollable
    st.markdown(
        """
        <style>
        .css-1l02m5g {
            overflow-y: auto;
            height: 500px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
