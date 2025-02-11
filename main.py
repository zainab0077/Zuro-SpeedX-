from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
    conn.commit()
    conn.close()

@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.json
    name, score = data['name'], data['score']

    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Score saved!"})

@app.route('/get_scores', methods=['GET'])
def get_scores():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 5")
    scores = cursor.fetchall()
    conn.close()

    return jsonify(scores)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
