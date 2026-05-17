import streamlit as st
import os
# Import your newly upgraded modules
from weather import get_weather_forecast
from stylist import recommend_outfit

# 1. Page Configuration
st.set_page_config(page_title="AI Stylist Pro", page_icon="👗", layout="wide")

# 2. Dynamic External CSS Injection
current_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(current_dir, "style.css")

if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("Notice: style.css not found. Running with default styles.")

# 3. Sidebar Layout
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/wardrobe.png")
    st.title("Control Panel")
    city = st.text_input("📍 Your Location:", "Berlin")
    st.markdown("---")
    st.write("### About AI Stylist Pro")
    st.write("Welcome to your premium 3-Day Capsule Lookbook. We integrate global weather forecasting with automated style rules to plan your week effortlessly.")

# 4. Main App Title Area
st.title("✨ Your 3-Day Capsule Lookbook")
st.write(f"Curating weather-optimized aesthetics for your upcoming days in **{city}**.")

# 5. Core Application Logic
if st.button("🔮 Curate My 3-Day Wardrobe"):
    with st.spinner(f"Synchronizing with meteorological servers for {city}..."):
        try:
            # Step 1: Fetch 3-day weather forecast array
            forecast_data = get_weather_forecast(city)
            
            # Step 2: Create elegant tabs for each day dynamically
            tab_titles = [f"📅 {day['date']}" for day in forecast_data]
            tabs = st.tabs(tab_titles)
            
            # Step 3: Loop through each day and render its custom dashboard inside its tab
            for tab, day in zip(tabs, forecast_data):
                with tab:
                    st.write("") # Spacer
                    
                    # Split each day's tab into a 2-column layout
                    col_left, col_right = st.columns([1, 1.5])
                    
                    # Left Side: Weather Status for that specific day
                    with col_left:
                        st.markdown(f"""
                            <div class="weather-info">
                                <h3>{city}</h3>
                                <h1 style="font-size: 50px; margin: 10px 0;">{day['temp']}°C</h1>
                                <p style="text-transform: capitalize; font-size: 16px; opacity: 0.85; letter-spacing: 1px;">{day['condition']}</p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Generate styling recommendations based on that day's weather
                        outfit, advice = recommend_outfit(day['temp'], day['condition'])
                        
                        st.write("") # Spacer
                        st.info(f"**💡 Stylist Tip:** {advice}")
                        
                    # Right Side: Custom Styled Fashion Cards
                    with col_right:
                        st.subheader("🧥 Recommended Ensemble")
                        
                        if isinstance(outfit, str):
                            st.error(outfit)
                        else:
                            for item_type, item_data in outfit.items():
                                icon = "👔" if item_type == "Top" else "👖" if item_type == "Bottom" else "🧥" if item_type == "Outerwear" else "👟"
                                color = item_data['color']
                                
                                # CSS Hex mapping safety net for premium luxury colors
                                css_color = color.replace("Camel", "#C19A6B").replace("Blue", "DodgerBlue").replace("Light Blue", "PowderBlue").replace("Dark Grey", "SlateGrey").replace("Dark Brown", "#5C4033").replace("Brown", "#8B4513")
                                
                                st.markdown(f"""
                                    <div class="outfit-card">
                                        <div class="outfit-visual-container">
                                            <div class="outfit-color-dot" style="background-color: {css_color};"></div>
                                            <span class="outfit-emoji-large">{icon}</span>
                                        </div>
                                        <div class="outfit-details">
                                            <span style="font-size: 1.1em; font-weight: 600; color: #111111;">{item_type}</span><br>
                                            <span style="color: #666666; font-size: 0.95em;">{color} {item_data['sub_category']}</span>
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)
                                
        except Exception as e:
            st.error(f"Oops! Failed to retrieve the 3-day lookbook for '{city}'. Error details: {e}")

# 6. Footer
st.markdown("---")
st.caption("AI Stylist Pro | Web Development Final Project 2026")