# ========================================
# MUMBAI HOUSE PRICE PREDICTOR
# Streamlit Application - Dark Theme
# ========================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="Mumbai House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================================
# DARK THEME STYLING
# ========================================
st.markdown("""
    <style>
    /* Dark theme - Black background, white text */
    :root {
        --background-color: #000000;
        --secondary-background-color: #1a1a1a;
        --text-color: #ffffff;
        --font: "Source Sans Pro", sans-serif;
    }
    
    /* Main app background - BLACK */
    .stApp {
        background-color: #000000 !important;
    }
    
    /* Main container */
    .main .block-container {
        background-color: #000000 !important;
        padding-top: 2rem !important;
    }
    
    /* Headers - WHITE */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    h1 {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 2.5em !important;
        text-shadow: 2px 2px 4px rgba(102, 126, 234, 0.3) !important;
    }
    
    h3 {
        color: #e0e0e0 !important;
        font-weight: 600 !important;
    }
    
    h4 {
        color: #d0d0d0 !important;
        font-weight: 600 !important;
    }
    
    /* Number input - Dark with white text */
    .stNumberInput > div > div > input {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 2px solid #444444 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Selectbox dropdown - Dark */
    .stSelectbox > div > div {
        background-color: #1a1a1a !important;
    }
    
    .stSelectbox > div > div > div {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 2px solid #444444 !important;
        border-radius: 8px !important;
    }
    
    .stSelectbox [data-baseweb="select"] {
        background-color: #1a1a1a !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 2px solid #444444 !important;
    }
    
    /* Dropdown menu items - Dark */
    [data-baseweb="menu"] {
        background-color: #1a1a1a !important;
    }
    
    [data-baseweb="menu"] li {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background-color: #333333 !important;
    }
    
    /* Labels - WHITE */
    label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        margin-bottom: 8px !important;
    }
    
    /* Slider - Dark */
    .stSlider > div > div > div {
        background-color: #1a1a1a !important;
        border-radius: 8px !important;
        padding: 15px !important;
        border: 2px solid #444444 !important;
    }
    
    .stSlider > div > div > div > div {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    .stSlider [data-baseweb="slider"] {
        background-color: #444444 !important;
    }
    
    .stSlider [aria-valuenow] {
        background-color: #667eea !important;
    }
    
    /* Radio buttons - Dark */
    .stRadio > div {
        background-color: #1a1a1a !important;
        padding: 15px !important;
        border-radius: 8px !important;
        border: 2px solid #444444 !important;
    }
    
    .stRadio label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    .stRadio > div > label > div {
        color: #ffffff !important;
    }
    
    /* Checkboxes - Dark */
    .stCheckbox {
        background-color: #1a1a1a !important;
        padding: 12px !important;
        border-radius: 8px !important;
        border: 1px solid #444444 !important;
        margin: 5px 0 !important;
    }
    
    .stCheckbox label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    .stCheckbox span {
        color: #ffffff !important;
    }
    
    /* Predict button - Gradient */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        height: 3.5em !important;
        border-radius: 12px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.5) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 30px rgba(102, 126, 234, 0.7) !important;
        background: linear-gradient(135deg, #7b93f7 0%, #8a5bb7 100%) !important;
    }
    
    /* Prediction box */
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
        margin: 30px 0;
    }
    
    .prediction-box h1 {
        color: white !important;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3) !important;
    }
    
    .prediction-box p {
        color: white !important;
    }
    
    /* Metric cards - Dark */
    .metric-card {
        background-color: #1a1a1a;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        text-align: center;
        border: 2px solid #333333;
        transition: transform 0.2s;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        border-color: #667eea;
    }
    
    .metric-card h2 {
        color: #667eea !important;
    }
    
    .metric-card p {
        color: #cccccc !important;
    }
    
    /* Info boxes - Dark */
    .info-box {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #667eea;
        margin: 15px 0;
    }
    
    .info-box strong {
        color: #ffffff !important;
    }
    
    .info-box span {
        color: #667eea !important;
    }
    
    .info-box small {
        color: #cccccc !important;
    }
    
    /* Dividers - Gradient */
    hr {
        margin: 30px 0 !important;
        border: none !important;
        height: 2px !important;
        background: linear-gradient(to right, #667eea, #764ba2) !important;
    }
    
    /* Streamlit alerts - Dark */
    .stAlert {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #444444 !important;
    }
    
    .stInfo {
        background-color: #1a2332 !important;
        border-left: 4px solid #2196f3 !important;
        color: #ffffff !important;
    }
    
    .stSuccess {
        background-color: #1a2e1a !important;
        border-left: 4px solid #4caf50 !important;
        color: #ffffff !important;
    }
    
    .stWarning {
        background-color: #332a1a !important;
        border-left: 4px solid #ff9800 !important;
        color: #ffffff !important;
    }
    
    .stError {
        background-color: #331a1a !important;
        border-left: 4px solid #f44336 !important;
        color: #ffffff !important;
    }
    
    /* Alert text */
    .stAlert > div {
        color: #ffffff !important;
    }
    
    /* Markdown - WHITE text */
    .stMarkdown {
        color: #ffffff !important;
    }
    
    p {
        color: #e0e0e0 !important;
    }
    
    strong {
        color: #ffffff !important;
    }
    
    /* Sidebar - Dark */
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
        border-right: 1px solid #333333 !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #667eea !important;
    }
    
    /* Sidebar info boxes */
    [data-testid="stSidebar"] .stAlert {
        background-color: #1a1a1a !important;
        border: 1px solid #333333 !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Write text */
    .stWrite {
        color: #ffffff !important;
    }
    
    /* Footer box */
    .footer-box {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333333;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ========================================
# LOAD MODEL AND ENCODINGS
# ========================================
@st.cache_resource
def load_model_files():
    """Load trained model, scaler, and location encodings"""
    try:
        with open('house_price_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        
        with open('location_encodings.pkl', 'rb') as f:
            location_encodings = pickle.load(f)
        
        return model, scaler, location_encodings
    except FileNotFoundError as e:
        st.error(f"⚠️ Error: Model files not found!\n\n{str(e)}")
        return None, None, None
    except Exception as e:
        st.error(f"⚠️ Error loading model: {str(e)}")
        return None, None, None

# Load models
model, scaler, location_encodings = load_model_files()

# ========================================
# MAIN APPLICATION
# ========================================

# Header
st.title("🏠 Mumbai House Price Predictor")
st.markdown("### Predict property prices in Mumbai using Advanced Machine Learning")
st.markdown("---")

if model is not None and location_encodings is not None:
    
    # Extract location data
    locations_list = sorted(location_encodings['location_price_mean'].keys())
    
    # ========================================
    # INPUT SECTION
    # ========================================
    
    # Create two columns
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 🏢 Property Details")
        st.write("")
        
        # Area input
        area = st.number_input(
            "📐 Carpet Area (sq ft)",
            min_value=200,
            max_value=10000,
            value=1050,
            step=50,
            help="Enter the carpet area in square feet"
        )
        
        st.write("")
        
        # Location dropdown
        location = st.selectbox(
            "📍 Location",
            options=locations_list,
            index=locations_list.index("Andheri East") if "Andheri East" in locations_list else 0,
            help="Select Mumbai location"
        )
        
        st.write("")
        
        # Bedrooms slider
        bedrooms = st.slider(
            "🛏️ Number of Bedrooms",
            min_value=1,
            max_value=7,
            value=2,
            help="Select number of bedrooms"
        )
        
        st.write("")
        
        # Property type
        st.markdown("**🏷️ Property Type**")
        resale = st.radio(
            "property_type_radio",
            options=["New Property", "Resale Property"],
            horizontal=True,
            label_visibility="collapsed"
        )
        resale_value = 1 if resale == "Resale Property" else 0
        
        st.write("")
        
        # Location info
        location_avg_price = location_encodings['location_price_mean'].get(location, 0)
        if location_avg_price > 0:
            st.info(f"📊 Average price in {location}: ₹{location_avg_price:,.0f}")
    
    with col2:
        st.markdown("### 🎯 Amenities & Features")
        st.write("")
        
        # Community Amenities
        st.markdown("#### 🏘️ Community Amenities")
        col2_1, col2_2 = st.columns(2)
        
        with col2_1:
            gymnasium = st.checkbox("🏋️ Gymnasium", value=False)
            swimming_pool = st.checkbox("🏊 Swimming Pool", value=False)
            car_parking = st.checkbox("🚗 Car Parking", value=True)
            lift_available = st.checkbox("🛗 Lift Available", value=True)
        
        with col2_2:
            security_247 = st.checkbox("🔒 24x7 Security", value=True)
            maintenance_staff = st.checkbox("👷 Maintenance Staff", value=True)
            landscaped_gardens = st.checkbox("🌳 Landscaped Gardens", value=False)
            jogging_track = st.checkbox("🏃 Jogging Track", value=False)
        
        st.write("")
        
        # Furnishing
        st.markdown("#### 🛋️ Furnishing")
        col2_3, col2_4 = st.columns(2)
        
        with col2_3:
            washing_machine = st.checkbox("🧺 Washing Machine", value=False)
            gas_connection = st.checkbox("🔥 Gas Connection", value=True)
            ac = st.checkbox("❄️ Air Conditioner", value=False)
        
        with col2_4:
            wifi = st.checkbox("📶 WiFi", value=False)
            microwave = st.checkbox("📻 Microwave", value=False)
            refrigerator = st.checkbox("🧊 Refrigerator", value=False)
    
    # Calculate features
    total_amenities = sum([
        int(maintenance_staff), int(gymnasium), int(swimming_pool),
        int(landscaped_gardens), int(jogging_track), int(security_247),
        int(car_parking), int(lift_available)
    ])
    
    furnishing_score = sum([
        int(washing_machine), int(gas_connection), int(ac),
        int(wifi), int(microwave), int(refrigerator)
    ])
    
    st.markdown("---")
    
    # ========================================
    # PREDICTION BUTTON
    # ========================================
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        predict_button = st.button("🔮 Predict House Price", use_container_width=True)
    
    if predict_button:
        with st.spinner('🔄 Calculating price...'):
            
            # Get encodings
            location_price_mean = location_encodings['location_price_mean'].get(location, 0)
            location_frequency = location_encodings['location_frequency'].get(location, 1)
            
            # Prepare features
            features = np.array([[
                area,
                location_price_mean,
                location_frequency,
                bedrooms,
                resale_value,
                total_amenities,
                furnishing_score,
                int(gymnasium),
                int(swimming_pool),
                int(security_247),
                int(car_parking),
                int(lift_available)
            ]])
            
            try:
                # Predict
                log_prediction = model.predict(features)[0]
                predicted_price = np.expm1(log_prediction)
                
                # Display result
                st.markdown("---")
                st.markdown("## 💰 Predicted Property Price")
                
                st.markdown(f"""
                    <div class="prediction-box">
                        <h1 style="color: white !important; margin: 0; font-size: 3.5em;">₹ {predicted_price:,.0f}</h1>
                        <p style="color: white !important; margin-top: 15px; font-size: 1.3em;">Estimated Property Value</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Metrics
                st.markdown("---")
                col_m1, col_m2, col_m3, col_m4 = st.columns(4)
                
                with col_m1:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h2 style="color: #667eea !important; margin: 0; font-size: 2em;">₹{predicted_price/area:,.0f}</h2>
                            <p style="color: #cccccc !important; margin: 10px 0 0 0;">Price per sq ft</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col_m2:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h2 style="color: #667eea !important; margin: 0; font-size: 2em;">{total_amenities}</h2>
                            <p style="color: #cccccc !important; margin: 10px 0 0 0;">Total Amenities</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col_m3:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h2 style="color: #667eea !important; margin: 0; font-size: 2em;">{furnishing_score}/6</h2>
                            <p style="color: #cccccc !important; margin: 10px 0 0 0;">Furnishing Score</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col_m4:
                    property_type_display = "Resale" if resale_value == 1 else "New"
                    st.markdown(f"""
                        <div class="metric-card">
                            <h2 style="color: #667eea !important; margin: 0; font-size: 2em;">{property_type_display}</h2>
                            <p style="color: #cccccc !important; margin: 10px 0 0 0;">Property Type</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                # Price breakdown
                st.markdown("---")
                st.markdown("### 📊 Price Breakdown")
                
                price_col1, price_col2 = st.columns(2)
                
                with price_col1:
                    st.markdown(f"""
                        <div class="info-box">
                            <strong style="color: #ffffff !important;">📍 Base Value</strong><br>
                            <span style="font-size: 1.5em; font-weight: bold; color: #667eea !important;">₹{predicted_price * 0.65:,.0f}</span><br>
                            <small style="color: #cccccc !important;">Based on {area} sq ft in {location}</small>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <div class="info-box">
                            <strong style="color: #ffffff !important;">🎯 Amenities Value</strong><br>
                            <span style="font-size: 1.5em; font-weight: bold; color: #667eea !important;">₹{predicted_price * 0.25:,.0f}</span><br>
                            <small style="color: #cccccc !important;">From {total_amenities} amenities</small>
                        </div>
                    """, unsafe_allow_html=True)
                
                with price_col2:
                    st.markdown(f"""
                        <div class="info-box">
                            <strong style="color: #ffffff !important;">🛋️ Furnishing Value</strong><br>
                            <span style="font-size: 1.5em; font-weight: bold; color: #667eea !important;">₹{predicted_price * 0.10:,.0f}</span><br>
                            <small style="color: #cccccc !important;">Score: {furnishing_score}/6</small>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    location_premium = ((location_price_mean / 10000000) - 1) * 100 if location_price_mean > 0 else 0
                    st.markdown(f"""
                        <div class="info-box">
                            <strong style="color: #ffffff !important;">📈 Location Factor</strong><br>
                            <span style="font-size: 1.5em; font-weight: bold; color: #667eea !important;">{location_premium:+.1f}%</span><br>
                            <small style="color: #cccccc !important;">{location} premium</small>
                        </div>
                    """, unsafe_allow_html=True)
                
                # Summary
                st.markdown("---")
                st.markdown("### 🏠 Summary")
                
                sum_col1, sum_col2, sum_col3 = st.columns(3)
                
                with sum_col1:
                    st.markdown(f"**Area:** {area} sq ft")
                    st.markdown(f"**Bedrooms:** {bedrooms} BHK")
                    st.markdown(f"**Type:** {property_type_display}")
                
                with sum_col2:
                    st.markdown(f"**Location:** {location}")
                    st.markdown(f"**Amenities:** {total_amenities}")
                    st.markdown(f"**Furnished:** {furnishing_score}/6")
                
                with sum_col3:
                    st.markdown(f"**Price/sqft:** ₹{predicted_price/area:,.0f}")
                    st.markdown(f"**Total:** ₹{predicted_price:,.0f}")
                    st.markdown(f"**Confidence:** 91%")
                
                # Disclaimer
                st.markdown("---")
                st.info("ℹ️ **Disclaimer:** ML prediction with 91% accuracy. Actual prices may vary ±₹22 lakhs.")
                st.success("✅ **Model:** XGBoost | R² Score: 0.91 | 7,719 properties trained")
                
            except Exception as e:
                st.error(f"❌ Prediction error: {str(e)}")

else:
    st.error("❌ Model files not found. Please ensure all .pkl files are in the directory.")

# ========================================
# SIDEBAR
# ========================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/real-estate.png", width=100)
    
    st.markdown("### 📖 About")
    st.info("""
        **XGBoost ML Model**
        - R² Score: 0.91
        - Error: ±₹22L
        - Properties: 7,719
        - Locations: 413
    """)
    
    st.markdown("### 🎯 Features")
    st.markdown("""
    - 📐 Area pricing
    - 📍 413 locations
    - 🛏️ Bedrooms
    - 🎯 16+ amenities
    - 🛋️ Furnishing
    - 🏷️ New/Resale
    """)
    
    st.markdown("### 🚀 Tech Stack")
    st.success("""
    - XGBoost
    - Streamlit
    - Python 3.8+
    - Scikit-learn
    """)
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("**Student Project**")
    st.markdown("ML Portfolio")
    st.markdown("*October 2025*")

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer-box">
        <p style="color: #ffffff !important; font-size: 1.1em; margin: 5px;"><strong>Mumbai House Price Predictor v1.0</strong></p>
        <p style="color: #cccccc !important; margin: 5px;">Powered by XGBoost & Streamlit</p>
        <p style="color: #999999 !important; font-size: 0.9em; margin: 5px;">© 2025 | Educational Project</p>
    </div>
""", unsafe_allow_html=True)
