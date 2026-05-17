import pandas as pd
import random
import os  # Built-in library to handle file paths safely

def recommend_outfit(current_temp: int, condition: str):
    """
    Act as an AI Stylist: Read the wardrobe, filter by temperature, 
    and generate an outfit combination along with fashion advice.
    """
    print(f"🧠 Stylist is thinking... (Temp: {current_temp}°C, Weather: {condition})")
    
    try:
        # Magic Fix: Dynamically locate wardrobe.csv relative to this file's location
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, "wardrobe.csv")
        
        # Open the digital wardrobe using the absolute path
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        return "Error: wardrobe.csv not found. Please check your folder.", ""

    # 2. Filter clothes based on the current temperature
    suitable_clothes = df[(df['min_temp'] <= current_temp) & (df['max_temp'] >= current_temp)]

    # 3. Categorize available clothes
    tops = suitable_clothes[suitable_clothes['category'] == 'Tops']
    bottoms = suitable_clothes[suitable_clothes['category'] == 'Bottoms']
    outerwear = suitable_clothes[suitable_clothes['category'] == 'Outerwear']
    shoes = suitable_clothes[suitable_clothes['category'] == 'Shoes']

    # 4. Apply Fashion Rules & Select Items
    outfit = {}
    
    if not tops.empty:
        outfit['Top'] = tops.sample(1).iloc[0]
    if not bottoms.empty:
        outfit['Bottom'] = bottoms.sample(1).iloc[0]
    if not shoes.empty:
        outfit['Shoes'] = shoes.sample(1).iloc[0]

    # Fashion Rule: Only suggest outerwear if the temperature is below 20°C
    if current_temp < 20 and not outerwear.empty:
        outfit['Outerwear'] = outerwear.sample(1).iloc[0]

    # 5. Generate Fashion Advice based on weather conditions
    advice = "Keep it simple and confident today!"
    
    if current_temp < 10:
        advice = "Layering is key today! Mix textures like wool and cotton to stay warm but stylish."
    elif "rain" in condition.lower() or "shower" in condition.lower():
        advice = "Rainy day! Darker bottoms are recommended to avoid visible splashes. Don't forget your umbrella!"
    elif current_temp > 25:
        advice = "It's hot! Keep it light and breathable. Light colors will help reflect the sun."

    return outfit, advice

# --- Test Block ---
if __name__ == "__main__":
    test_temp = 12
    test_condition = "Cloudy"
    
    my_outfit, my_advice = recommend_outfit(test_temp, test_condition)
    
    print("\n👗 --- YOUR OUTFIT OF THE DAY --- 👖")
    if isinstance(my_outfit, str):
        print(my_outfit)
    else:
        for item_type, item_data in my_outfit.items():
            print(f"- {item_type}: {item_data['color']} {item_data['sub_category']}")
        print(f"\n💡 Stylist Tip: {my_advice}")