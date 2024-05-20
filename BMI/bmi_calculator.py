import streamlit as st

def calculate_bmi(weight, height, unit='metric'):
    """
    Calculate BMI given weight and height.
    """
    if unit == 'metric':
        # Calculate BMI using weight in kilograms and height in meters
        bmi = weight / ((height / 100) ** 2)
    else:
        # Calculate BMI using weight in pounds and height in inches
        bmi = (weight / (height ** 2)) * 703
    return bmi

def bmi_category(bmi):
    """
    Determine BMI category based on BMI value.
    """
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal (Healthy)'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

def main():
    st.title('BMI Calculator')
    
    # Set background color
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(135deg, #c7eafd 0%, #fdf6f6 100%);
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set background image
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("C:/Users/techn/Downloads/BMI-gauge-Large.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Input weight in kilograms
    weight = st.number_input('Enter your weight (kg)', min_value=0.0)
    
    # Select unit for height
    unit = st.radio('Select unit for height:', ['Metric (cm)', 'Imperial (inches)'])
    
    if unit == 'Metric (cm)':
        # Input height in centimeters
        height = st.number_input('Enter your height (cm)', min_value=0.0)
    else:
        # Input height in inches
        height = st.number_input('Enter your height (in)', min_value=0.0)
    
    # Calculate BMI
    if st.button('Calculate BMI'):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height, unit='metric' if unit == 'Metric (cm)' else 'imperial')
            bmi_msg = bmi_category(bmi)
            st.write('Your BMI:', bmi)
            st.write('BMI Category:', bmi_msg)
            if bmi_msg == 'Normal (Healthy)':
                st.success("You are Healthy!")
                st.balloons()
            else:
                st.warning("Please consult a healthcare professional.")
        else:
            st.write('Please enter valid weight and height.')

if __name__ == '__main__':
    main()
