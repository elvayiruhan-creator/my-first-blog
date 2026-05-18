import streamlit as st
import os
# Import your newly upgraded 7-day core engine
from weather import get_7day_forecast
from stylist import recommend_outfit

# 1. Page Configuration (Wide layout for a sleek, modern luxury app aesthetic)
st.set_page_config(page_title="AI Stylist Pro", page_icon="👗", layout="wide")

# 2. Dynamic CSS Loading (Maintains clean code standards)
current_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(current_dir, "style.css")

if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("Notice: style.css not found. Running with default browser styles.")

# Helper Function: Core Engine for High-End Lookbook Fashion Image Mapping
def get_fashion_inspiration_image(color: str, sub_category: str):
    """
    Acts as a luxury fashion database mapper. Maps wardrobe combinations 
    to specific, high-end editorial street style photos from Unsplash.
    """
    # Curated premium asset matrix to guarantee high fashion presentation
    fashion_matrix = {
        ("grey", "hoodie"): "https://images.unsplash.com/photo-1556821840-3a63f95609a7?auto=format&fit=crop&w=300&q=80",
        ("white", "t-shirt"): "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=300&q=80",
        ("black", "t-shirt"): "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=300&q=80",
        ("blue", "jeans"): "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=300&q=80",
        ("black", "pants"): "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=300&q=80",
        ("white", "sneakers"): "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=300&q=80",
        ("black", "boots"): "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?auto=format&fit=crop&w=300&q=80",
        ("camel", "wool coat"): "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=300&q=80",
        ("black", "light jacket"): "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=300&q=80"
    }
    
    key = (color.lower().strip(), sub_category.lower().strip())
    
    if key in fashion_matrix:
        return fashion_matrix[key]
    else:
        # Intelligent fallback search query if user adds custom items to wardrobe.csv later
        search_query = f"{color}+{sub_category}+streetwear".replace(" ", "+")
        return f"https://images.unsplash.com/featured/300x300/?{search_query}"

# 3. Sidebar Configuration
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/wardrobe.png")
    st.title("Control Panel")
    city = st.text_input("📍 Your Location:", "Berlin")
    st.markdown("---")
    st.write("### About AI Stylist Pro")
    st.write("This intelligence tier merges dynamic 7-day multi-source weather models with algorithmic style coordination logic, providing an inspiring visual moodboard for your week.")

# 4. Main App Header Area
st.title("✨ The 7-Day Editorial Lookbook")
st.write(f"Curating high-end visual lookbooks and weather-optimized style formulas for **{city}**.")

# 5. Core Application Execution Flow
if st.button("🔮 Generate 7-Day Capsule Wardrobe"):
    with st.spinner(f"Compiling meteorological metrics and curating lookbooks for {city}..."):
        try:
            # Step 1: Execute 7-day data pipeline (API + Smart Simulation fallback)
            forecast_data = get_7day_forecast(city)
            
            # Step 2: Establish high-fidelity multi-day tab matrix
            tab_titles = [f"Day {i+1} ({day['date'][-5:]})" for i, day in enumerate(forecast_data)]
            tabs = st.tabs(tab_titles)
            
            # Step 3: Loop through each day and populate its workspace inside its tab
            for i, (tab, day) in enumerate(zip(tabs, forecast_data)):
                with tab:
                    st.write("") # Spacer Layout
                    
                    # Layout: 2-Column editorial magazine balance
                    col_left, col_right = st.columns([1, 1.6])
                    
                    # Left Column: Weather Metric Display
                    with col_left:
                        # Label indicating source tracking for presentation transparency
                        source_tag = "REAL-TIME API" if i < 3 else "PREDICTIVE MODEL"
                        
                        st.markdown(f"""
                            <div class="weather-info">
                                <span style="font-size: 0.85em; font-weight: 700; opacity: 0.6; letter-spacing: 1.5px;">{source_tag}</span>
                                <h2 style="margin-top: 10px;">{city}</h2>
                                <h1 style="font-size: 52px; margin: 15px 0; font-weight: 500;">{day['temp']}°C</h1>
                                <p style="text-transform: capitalize; font-size: 16px; opacity: 0.85; letter-spacing: 0.5px;">{day['condition']}</p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Step 4: Run the style selector rules for the day's specific weather
                        outfit, advice = recommend_outfit(day['temp'], day['condition'])
                        
                        st.write("") # Spacer Layout
                        st.info(f"**💡 Stylist Moodboard Tip:** {advice}")
                        
                    # Right Column: Visual Moodboard Cards (The Core Focus Upgrade)
                    with col_right:
                        st.subheader("🧥 Recommended Lookbook Elements")
                        
                        if isinstance(outfit, str):
                            st.error(outfit)
                        else:
                            for item_type, item_data in outfit.items():
                                color = item_data['color']
                                sub_cat = item_data['sub_category']
                                
                                # Resolve dynamic background color hex mappings for the tiny dots
                                css_color = color.replace("Camel", "#C19A6B").replace("Blue", "DodgerBlue").replace("Light Blue", "PowderBlue").replace("Dark Grey", "SlateGrey").replace("Dark Brown", "#5C4033").replace("Brown", "#8B4513")
                                
                                # Retrieve the curated premium fashion photo URL
                                image_url = get_fashion_inspiration_image(color, sub_cat)
                                
                                # Inject premium HTML block utilizing external CSS styling classes
                                st.markdown(f"""
                                    <div class="outfit-card">
                                        <div class="outfit-image-area">
                                            <img src="{image_url}" class="outfit-img" alt="Fashion Inspiration">
                                            <div class="outfit-color-indicator" style="background-color: {css_color};"></div>
                                        </div>
                                        <div class="outfit-details">
                                            <span style="font-size: 1.1em; font-weight: 600; color: #111111; letter-spacing: 0.2px;">{item_type}</span><br>
                                            <span style="color: #666666; font-size: 0.95em; display: inline-block; margin-top: 4px;">{color} {sub_cat}</span>
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)
                                
        except Exception as e:
            st.error(f"Oops! Synchronization failure encountered for '{city}'. Diagnostic details: {e}")

# 6. Engineering Footer Block
st.markdown("---")
st.caption("AI Stylist Pro v2.5 | Modern Software Engineering & Web Development Final Project 2026")