from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

recipes = [
    {
        "id": 1,
        "title": "Spaghetti Carbonara",
        "cuisine": "Italian",
        "description": "Classic pasta with creamy sauce and pancetta.",
        "rating": 4.5,
        "total_time": 30,
        "serves": 2
    },
    {
        "id": 2,
        "title": "Paneer Butter Masala",
        "cuisine": "Indian",
        "description": "Rich, creamy curry with paneer cubes.",
        "rating": 4.8,
        "total_time": 40,
        "serves": 4
    },
    {
        "id": 3,
        "title": "Sushi Roll",
        "cuisine": "Japanese",
        "description": "Rice and seafood wrapped in nori sheets.",
        "rating": 4.7,
        "total_time": 50,
        "serves": 2
    },
    {
        "id": 4,
        "title": "Tacos al Pastor",
        "cuisine": "Mexican",
        "description": "Corn tortillas filled with marinated pork and pineapple.",
        "rating": 4.6,
        "total_time": 35,
        "serves": 3
    },
    {
        "id": 5,
        "title": "Beef Bourguignon",
        "cuisine": "French",
        "description": "Slow-cooked beef stew with red wine and mushrooms.",
        "rating": 4.9,
        "total_time": 180,
        "serves": 4
    },
    {
        "id": 6,
        "title": "Shakshuka",
        "cuisine": "Middle Eastern",
        "description": "Poached eggs in a spicy tomato and pepper sauce.",
        "rating": 4.5,
        "total_time": 25,
        "serves": 2
    },
    {
        "id": 7,
        "title": "Pad Thai",
        "cuisine": "Thai",
        "description": "Stir-fried rice noodles with shrimp, peanuts, and lime.",
        "rating": 4.6,
        "total_time": 30,
        "serves": 2
    },
    {
        "id": 8,
        "title": "Peking Duck",
        "cuisine": "Chinese",
        "description": "Crispy roasted duck served with pancakes and hoisin sauce.",
        "rating": 4.8,
        "total_time": 120,
        "serves": 4
    },
    {
        "id": 9,
        "title": "Greek Moussaka",
        "cuisine": "Greek",
        "description": "Layered eggplant casserole with ground meat and béchamel sauce.",
        "rating": 4.7,
        "total_time": 90,
        "serves": 6
    },
    {
        "id": 10,
        "title": "Falafel Wrap",
        "cuisine": "Lebanese",
        "description": "Crispy chickpea patties wrapped in pita with tahini sauce.",
        "rating": 4.4,
        "total_time": 40,
        "serves": 3
    },
    {
        "id": 11,
        "title": "Fish and Chips",
        "cuisine": "British",
        "description": "Deep-fried fish fillets with crispy potato fries.",
        "rating": 4.3,
        "total_time": 35,
        "serves": 2
    },
    {
        "id": 12,
        "title": "Kimchi Jjigae",
        "cuisine": "Korean",
        "description": "Spicy kimchi stew with pork and tofu.",
        "rating": 4.7,
        "total_time": 45,
        "serves": 4
    },
    {
        "id": 13,
        "title": "Paella",
        "cuisine": "Spanish",
        "description": "Saffron rice with seafood, chicken, and vegetables.",
        "rating": 4.8,
        "total_time": 60,
        "serves": 5
    },
    {
        "id": 14,
        "title": "Tom Yum Soup",
        "cuisine": "Thai",
        "description": "Hot and sour soup with shrimp, lemongrass, and lime.",
        "rating": 4.6,
        "total_time": 30,
        "serves": 3
    },
    {
        "id": 15,
        "title": "Empanadas",
        "cuisine": "Argentinian",
        "description": "Baked or fried pastry filled with beef, onions, and spices.",
        "rating": 4.5,
        "total_time": 50,
        "serves": 4
    },
    {
        "id": 16,
        "title": "Baklava",
        "cuisine": "Turkish",
        "description": "Layered pastry dessert filled with nuts and honey syrup.",
        "rating": 4.9,
        "total_time": 90,
        "serves": 8
    },
    {
        "id": 17,
        "title": "Hamburger",
        "cuisine": "American",
        "description": "Grilled beef patty served in a bun with cheese and veggies.",
        "rating": 4.4,
        "total_time": 20,
        "serves": 1
    },
    {
        "id": 18,
        "title": "Pho",
        "cuisine": "Vietnamese",
        "description": "Beef noodle soup with herbs, lime, and bean sprouts.",
        "rating": 4.8,
        "total_time": 70,
        "serves": 4
    },
    {
        "id": 19,
        "title": "Pierogi",
        "cuisine": "Polish",
        "description": "Dumplings filled with potatoes, cheese, or meat.",
        "rating": 4.5,
        "total_time": 60,
        "serves": 4
    },
    {
        "id": 20,
        "title": "Satay Skewers",
        "cuisine": "Indonesian",
        "description": "Grilled skewers of marinated meat served with peanut sauce.",
        "rating": 4.6,
        "total_time": 40,
        "serves": 3
    },
    {
        "id": 21,
        "title": "Churros",
        "cuisine": "Spanish",
        "description": "Fried dough pastries rolled in sugar and cinnamon.",
        "rating": 4.7,
        "total_time": 25,
        "serves": 4
    },
    {
        "id": 22,
        "title": "Ceviche",
        "cuisine": "Peruvian",
        "description": "Raw fish cured in lime juice with onions and chili.",
        "rating": 4.8,
        "total_time": 30,
        "serves": 2
    }
]


@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)
