import streamlit as st
from weather import get_current_weather
from stylist import recommend_outfit

st.set_page_config(page_title="AI Stylist", page_icon="👗", layout="centered")

st.title("👗 AI Stylist")
st.write("Your smart wardrobe powered by real-time weather data.")
st.markdown("---")

city = st.text_input("Enter your city name:", "Berlin")

if st.button("Generate My Outfit"):
    with st.spinner(f"Checking weather in {city} and browsing your wardrobe..."):
        try:
            temp, condition = get_current_weather(city)
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(f"🌍 Weather in {city}")
                st.info(f"🌡️ Temperature: {temp} °C")
                st.info(f"☁️ Condition: {condition}")
            
            with col2:
                outfit, advice = recommend_outfit(temp, condition)
                st.subheader("👚 Today's Outfit")
                if isinstance(outfit, str):
                    st.error(outfit) 
                else:
                    for item_type, item_data in outfit.items():
                        st.success(f"**{item_type}**: {item_data['color']} {item_data['sub_category']}")
            
            st.markdown("---")
            st.warning(f"**💡 Stylist Tip:** {advice}")

        except Exception as e:
            st.error(f"Oops! Could not get data for '{city}'. (Error: {e})")