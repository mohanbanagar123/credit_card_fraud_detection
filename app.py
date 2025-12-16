import streamlit as st
import requests

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="auto"
)

def set_background_image():
    css = """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1508780709619-79562169bc64?auto=format&fit=crop&w=1740&q=80");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background_image()

st.markdown("""
    <div style='text-align: center; padding: 1rem; background-color: rgba(0,0,0,0.6); border-radius: 10px;'>
        <h1 style='color: #ffffff;'>💳 Credit Card Fraud Detection System</h1>
        <h4 style='color: red;'>Secure your transactions with AI-powered fraud detection</h4>
    </div>
""", unsafe_allow_html=True)


if "step" not in st.session_state:
    st.session_state.step = "home"


if st.session_state.step == "home":
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910791.png", width=150)
    st.markdown("""
        <h2 style='background-color:#ffffffcc; padding:10px; border-radius:8px;'>🔐 Welcome Admin</h2>
    """, unsafe_allow_html=True)
    st.markdown("<p style='background-color:#ffffffcc; padding:10px; border-radius:8px;'>Click the button below to start the fraud detection system.</p>", unsafe_allow_html=True)

    if st.button("🚀 Start Detection"):
        st.session_state.step = "login"

elif st.session_state.step == "login":
    st.markdown("<h2 style='background-color:#ffffffcc; padding:10px; border-radius:8px;'>🔐 Admin Sign In</h2>", unsafe_allow_html=True)
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>User Email</label>", unsafe_allow_html=True)
    email = st.text_input("", placeholder="admin@example.com", key="login_email")
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Password</label>", unsafe_allow_html=True)
    password = st.text_input("", type="password", placeholder="Enter your password", key="login_password")

    if st.button("🚪 SIGN IN"):
        if email and password:
            st.success(f"Welcome, {email}!")
            st.session_state.step = "create_payment"
        else:
            st.error("⚠️ Please enter your credentials.")

elif st.session_state.step == "create_payment":
    st.markdown("<h2 style='background-color:#ffffffcc; padding:10px; border-radius:8px;'>💸 Create Payment Link</h2>", unsafe_allow_html=True)

    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Amount</label>", unsafe_allow_html=True)
    amount = st.text_input("", placeholder="Enter transaction amount", key="amount")

    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Select Country</label>", unsafe_allow_html=True)
    country = st.selectbox("", ["India", "USA", "UK"], key="country")

    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Enter User Email</label>", unsafe_allow_html=True)
    user_email = st.text_input("", placeholder="user@example.com", key="user_email")

    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Exempt Rules?</label>", unsafe_allow_html=True)
    exempt = st.radio("", ["Yes", "No"], key="exempt")

    if st.button("🔗 CREATE LINK"):
        if amount and user_email:
            st.session_state.payment_info = {
                "amount": amount,
                "country": country,
                "user_email": user_email,
                "exempt": exempt
            }
            st.success("Payment link created successfully!")
            st.session_state.step = "test_card"
        else:
            st.error("⚠️ Please fill all the fields.")

elif st.session_state.step == "test_card":
    st.markdown("<h2 style='background-color:#ffffffcc; padding:10px; border-radius:8px;'>🧪 Credit Card Testing</h2>", unsafe_allow_html=True)

    payment_info = st.session_state.get("payment_info", {})
    if payment_info:
        st.markdown(f"""
            <div style='background-color:#ffffffcc; padding: 10px; border-radius: 10px;'>
                <strong>Payment Details:</strong><br>
                • <b>Amount:</b> {payment_info['amount']}<br>
                • <b>Country:</b> {payment_info['country']}<br>
                • <b>User Email:</b> {payment_info['user_email']}<br>
                • <b>Exempt Rules:</b> {payment_info['exempt']}
            </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h4 style='background-color:#ffffffcc; padding:10px; border-radius:8px;'>👤 Enter Your Personal Details</h4>", unsafe_allow_html=True)

    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Name</label>", unsafe_allow_html=True)
    name = st.text_input("", key="name", placeholder="Enter your name")
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Email Address</label>", unsafe_allow_html=True)
    email = st.text_input("", key="email", placeholder="Enter your email")
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Phone Number</label>", unsafe_allow_html=True)
    phone = st.text_input("", key="phone", placeholder="Enter your phone number")
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Street Address</label>", unsafe_allow_html=True)
    street = st.text_input("", key="street", placeholder="Enter your street address")
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>City</label>", unsafe_allow_html=True)
    city = st.text_input("", key="city", placeholder="Enter your city")
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Zipcode</label>", unsafe_allow_html=True)
    zip_code = st.text_input("", key="zip_code", placeholder="Enter your zipcode")

    st.write("---")
    st.markdown("<h4 style='background-color:#ffffffcc; padding:10px; border-radius:8px;'>🚲 Transaction Features for Prediction</h4>", unsafe_allow_html=True)
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Feature 1</label>", unsafe_allow_html=True)
    feature1 = st.number_input("", min_value=-1000.0, format="%.6f", key="feature1")
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Feature 2</label>", unsafe_allow_html=True)
    feature2 = st.number_input("", min_value=-1000.0, format="%.6f", key="feature2")
    
    st.markdown("<label style='color: red; font-weight: bold; margin-bottom:2px;'>Feature 3</label>", unsafe_allow_html=True)
    feature3 = st.number_input("", min_value=-1000.0, format="%.6f", key="feature3")

    if st.button("🔍 Predict Fraud"):
        if name and email and phone and street and city and zip_code:
            input_data = {
                "feature1": feature1,
                "feature2": feature2,
                "feature3": feature3
            }

            try:
                with st.spinner('🔄 Predicting... Please wait...'):
                    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)

                if response.status_code == 200:
                    result = response.json()
                    pred = result.get("prediction")
                    if pred == 1:
                        st.markdown("""
                            <div style='background-color:#ffcccc; padding:15px; border-radius:10px;'>
                                <h4 style='color:red;'>❗ ALERT: This transaction is <u>FRAUDULENT</u>.</h4>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                            <div style='background-color:#ccffcc; padding:15px; border-radius:10px;'>
                                <h4 style='color:green;'>✅ Good news: This transaction is <u>NOT FRAUD</u>.</h4>
                            </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                else:
                    st.error(f"Error: {response.status_code} - Unable to make prediction.")

            except Exception as e:
                st.error(f"🚫 Request failed: {e}")
        else:
            st.warning("⚠️ Please fill all your personal details before prediction.")