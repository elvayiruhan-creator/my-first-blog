import streamlit as st
import os
# Import your custom modules
from weather import get_current_weather
from stylist import recommend_outfit

# 1. Page Configuration (Wide layout for a modern dashboard look)
st.set_page_config(page_title="AI Stylist Pro", page_icon="👗", layout="wide")

# 2. Dynamic CSS Injection (Clean Code Principle: separating styles from logic)
current_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(current_dir, "style.css")

if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("Notice: style.css not found. Running with default styles.")

# 3. Sidebar Layout (For inputs and settings)
with st.sidebar:
    # A beautiful placeholder icon for the wardrobe
    st.image("https://img.icons8.com/clouds/200/000000/wardrobe.png")
    st.title("Control Panel")
    city = st.text_input("📍 Your Location:", "Berlin")
    st.markdown("---")
    st.write("### About AI Stylist")
    st.write("This app leverages live weather APIs and applies algorithmic fashion rules to curate the perfect daily outfit from your personal wardrobe.")

# 4. Main App Title Area
st.title("✨ Your Daily Fashion Curator")
st.write(f"Personalized, weather-optimized styling for your day in **{city}**.")

# 5. Core Application Logic (Triggered on button click)
if st.button("👗 Generate My Look of the Day"):
    with st.spinner(f"Analyzing weather patterns in {city}..."):
        try:
            # Step 1: Fetch live weather data
            temp, condition = get_current_weather(city)
            
            # Step 2: Create a 2-column layout for results
            col_left, col_right = st.columns([1, 1.5])
            
            # Left Column: Weather Display Card
            with col_left:
                st.markdown(f"""
                    <div class="weather-info">
                        <h2>{city}</h2>
                        <h1 style="font-size: 55px; margin: 10px 0;">{temp}°C</h1>
                        <p style="text-transform: capitalize; font-size: 18px; opacity: 0.9;">{condition}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Step 3: Fetch styling recommendation and advice
                outfit, advice = recommend_outfit(temp, condition)
                
                st.write("") # Spacer
                st.info(f"**💡 Stylist Tip:** {advice}")
                
            # Right Column: Visual Outfit Recommendation Cards
            with col_right:
                st.subheader("🧥 Recommended Ensemble")
                
                if isinstance(outfit, str):
                    # Display path error if wardrobe.csv is completely missing
                    st.error(outfit)
                else:
                    # Dynamically render elegant cards based on chosen clothing items
                    for item_type, item_data in outfit.items():
                        # 1. Map categories toaesthetic emojis
                        icon = "👔" if item_type == "Top" else "👖" if item_type == "Bottom" else "🧥" if item_type == "Outerwear" else "👟"
                        
                        # 2. Extract the color to use as a dynamic placeholder background
                        color = item_data['color']
                        
                        # 3. Handle specific colors (like Camel) that might not be CSS named colors
                        # Let's map unique colors or provide a general safety net
                        css_color = color.replace("Camel", "#C19A6B").replace("Blue", "DodgerBlue").replace("Light Blue", "PowderBlue").replace("Dark Grey", "SlateGrey").replace("Dark Brown", "#654321").replace("Brown", "#8B4513")

                        # 4. Generate the enhanced outfit card with dynamic color visual
                        st.markdown(f"""
                            <div class="outfit-card">
                                <div class="outfit-visual-container">
                                    <div class="outfit-color-dot" style="background-color: {css_color};"></div>
                                    <span class="outfit-emoji-large">{icon}</span>
                                </div>
                                <div class="outfit-details">
                                    <span style="font-size: 1.15em; font-weight: bold;">{item_type}</span><br>
                                    <span style="color: #555555; font-size: 0.95em;">{color} {item_data['sub_category']}</span>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        
        except Exception as e:
            st.error(f"Oops! Failed to synchronize data for '{city}'. Please verify the spelling or check your connection. (Error: {e})")

# 6. Footer (Professional touch for school projects)
st.markdown("---")
st.caption("AI Stylist Project | Web Development Final Project 2026")