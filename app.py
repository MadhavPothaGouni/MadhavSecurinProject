from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname="recipes_db",
        user="postgres",
        password="your_password",  # change this
        host="localhost",
        port="5432"
    )
    return conn


# Root endpoint
@app.route("/")
def home():
    return jsonify({"message": "Recipe API is running"})


# Get all recipes (with pagination, search, sort)
@app.route("/recipes", methods=["GET"])
def get_recipes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    search = request.args.get("search", "")
    sort = request.args.get("sort", "id")

    offset = (page - 1) * limit

    conn = get_db_connection()
    cur = conn.cursor()

    query = f"""
        SELECT id, cuisine, title, rating, total_time, serves
        FROM recipes
        WHERE title ILIKE %s OR cuisine ILIKE %s
        ORDER BY {sort}
        LIMIT %s OFFSET %s
    """
    cur.execute(query, (f"%{search}%", f"%{search}%", limit, offset))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    recipes = []
    for r in rows:
        recipes.append({
            "id": r[0],
            "cuisine": r[1],
            "title": r[2],
            "rating": r[3],
            "total_time": r[4],
            "serves": r[5]
        })

    return jsonify(recipes)


# Get a single recipe by ID
@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row is None:
        return jsonify({"error": "Recipe not found"}), 404

    recipe = {
        "id": row[0],
        "cuisine": row[1],
        "title": row[2],
        "rating": row[3],
        "prep_time": row[4],
        "cook_time": row[5],
        "total_time": row[6],
        "description": row[7],
        "nutrients": row[8],
        "serves": row[9]
    }
    return jsonify(recipe)


if __name__ == "__main__":
    app.run(debug=True)
