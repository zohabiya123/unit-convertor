import streamlit as st  # type: ignore
st.markdown(
    """
    <style>
    body{
        background-color: #1e1e2f;
        color: white:
    }
    .stApp {
        background-color: linear-gradient(135deg, #bcbcbc, cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }
        .head{
            background: linear-gradient(90deg, #ff66c4, #3ef3ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0px 0px 10px rgba(255, 102, 196, 0.6);
            text-align: center;
            font-size: 40px;
            
    }
        input[type="number"]{
            font-size: 25px;
            height: 50px !important;
    }
        div[data-baseweb="select"] > div {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 50px !important;
        font-size: 30px;
    }
        .stButton>button{
            background: #2a2d3e;
            color: white;
            font-size: 24px !important; 
            border-radius: 10px;
            border: 2px solid #3ef3ff;
            transition: all 0.3s ease-in-out;
            box-shadow: 0px 0px 10px #3ef3ff;
            width: 100%;
            margin-top: 40px;
            height: 60px !important;
    }
         div.stButton > button p {
        font-size: 30px !important;
        
    }
        .stButton>button:hover{
            transform: scale(1.05);
            background: linear-gradient(90deg, #3ef3ff, #ff66c4);
            box-shadow: 0px 0px 10px #3ef3ff, 0px 0px 20px #ff66c4;
            color: white;
    }
        .result-box{
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3); 
    }
        .footer{
            background: linear-gradient(90deg, #ff66c4, #3ef3ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0px 0px 10px rgba(255, 102, 196, 0.6);
            text-align: center;
            margin-top: 50px;
            font-size: 30px;
            font-weight: bold;
            
    }
    </style>
    """,
    unsafe_allow_html = True
)
# Title and description 
st.markdown("<h1 class = 'head'> Unit Converter using Python and Streamlit </h1>", unsafe_allow_html=True)

# sidebar menu

conversion_type = st.columns(1)[0].selectbox("Select the type of conversion", ["Length","Temperature", "Weight"])
value = st.number_input("Enter value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Milimeter", "Miles", "Yards", "Feet", "Inches"])
    with col2: 
        to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Milimeter", "Miles", "Yards", "Feet", "Inches"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])

# conversion logic


def length_convertor(value, from_unit, to_unit):
    length_units = {
        "Meter": 1.0,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Milimeter": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return round(((value / length_units[from_unit]) * length_units[to_unit]), 2)

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1.0,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274,
    }
    return round((value / weight_units[from_unit] * weight_units[to_unit]), 2)

def temperature_convertor(value, from_unit, to_unit):
    temperature_units = {
        "Celsius": 1.0,
        "Fahrenheit": 1.8,
        "Kelvin": 1.0,
    }
    return round((value + 273.15) if from_unit == "Celsius" and to_unit == "Kelvin" else (value * 1.8 + 32) if from_unit == "Celsius" and to_unit == "Fahrenheit" else (value - 273.15) if from_unit == "Kelvin" and to_unit == "Celsius" else (value - 32) / 1.8 if from_unit == "Fahrenheit" and to_unit == "Celsius" else value, 2)

if st.button("Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{result} {to_unit}</div>", unsafe_allow_html=True)
    
st.markdown(f"<div class='footer'> Developed by syed Basit </a></div>", unsafe_allow_html=True)

        