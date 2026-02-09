import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NutriAI - Instant Nutritional Information",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("NutriAI - Instant Nutritional Information")
st.write("Get instant nutritional insights for foods and dishes")

# ---------------- INPUT ----------------
food_items = st.text_area(
    "Enter Food Items (separate by commas):",
    placeholder="Apple, Banana, Mango"
)

# ---------------- DATA (MOCK AI DATABASE) ----------------
def get_nutrition_data(food_list):
    nutrition_db = {
        "apple": {
            "Calories": "52 kcal",
            "Protein": "0.3 g",
            "Fat": "0.2 g",
            "Carbohydrates": "13.8 g",
            "Fiber": "2.4 g",
            "Vitamins": "Vitamin C, Vitamin K",
            "Minerals": "Potassium"
        },
        "banana": {
            "Calories": "89 kcal",
            "Protein": "1.1 g",
            "Fat": "0.3 g",
            "Carbohydrates": "22.8 g",
            "Fiber": "2.6 g",
            "Vitamins": "Vitamin B6, Vitamin C",
            "Minerals": "Potassium, Magnesium"
        },
        "mango": {
            "Calories": "60 kcal",
            "Protein": "0.8 g",
            "Fat": "0.4 g",
            "Carbohydrates": "15 g",
            "Fiber": "1.6 g",
            "Vitamins": "Vitamin A, Vitamin C",
            "Minerals": "Potassium"
        },
        "butter chicken": {
            "Calories": "350–500 kcal",
            "Protein": "20–30 g",
            "Fat": "25–40 g",
            "Carbohydrates": "15–25 g",
            "Note": "High saturated fat"
        },
        "chole bhature": {
            "Calories": "600–800 kcal",
            "Protein": "15–25 g",
            "Fat": "30–50 g",
            "Carbohydrates": "70–90 g",
            "Note": "High carbs and fat"
        },
        "gulab jamun": {
            "Calories": "200–300 kcal",
            "Protein": "2–4 g",
            "Fat": "10–20 g",
            "Carbohydrates": "30–40 g",
            "Note": "High sugar dessert"
        }
    }

    result = {}
    for food in food_list:
        key = food.strip().lower()
        if key in nutrition_db:
            result[food.strip().title()] = nutrition_db[key]
        else:
            result[food.strip().title()] = "No exact data available (varies by recipe)"

    return result

# ---------------- BUTTON ACTION ----------------
if st.button("Get Nutritional Information"):
    if not food_items.strip():
        st.warning("Please enter food items")
    else:
        with st.spinner("Analyzing nutritional data..."):
            time.sleep(1.5)  # simulate AI processing

            foods = food_items.split(",")
            nutrition_data = get_nutrition_data(foods)

        st.subheader("Nutritional Information:")

        for food, details in nutrition_data.items():
            st.markdown(f"### {food}")

            if isinstance(details, dict):
                for k, v in details.items():
                    st.write(f"• **{k}:** {v}")
            else:
                st.write(details)

            st.markdown("---")

# ---------------- FOOTER ----------------
st.caption(
    "⚠ Nutritional values are approximate. Actual values depend on ingredients, portion size, and preparation method."
)
