from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = [
    {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
    {"id": 2, "name": "Bob Johnson", "email": "bob@example.com"}
]

def find_user(user_id):
    return next((user for user in users if user["id"] == user_id), None)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400
    
    if any(u["email"] == data["email"] for u in users):
        return jsonify({"error": "Email already exists"}), 400
    
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if "name" in data:
        user["name"] = data["name"]
    if "email" in data:
        user["email"] = data["email"]
    
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users.remove(user)
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
