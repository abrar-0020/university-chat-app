from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS
import sqlite3
import bcrypt
import os

print("✅ University Chat App - Loading with THREADING mode (NO eventlet)")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "supersecretkey")

# Enable CORS for all routes and origins
CORS(app)
# Enable CORS for Socket.IO with threading support for better deployment compatibility
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# ======================
# Database setup
# ======================
messages = []  # Simple in-memory storage for messages

def init_db():
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        username TEXT UNIQUE,
        password_hash TEXT
    )
    """)
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

def register_user(email, username, password):
    if not email.endswith("@university.edu"):
        return False, "❌ Only university emails allowed."
    
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    try:
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (email, username, password_hash) VALUES (?, ?, ?)", 
                       (email, username, password_hash))
        conn.commit()
        return True, "✅ Registration successful."
    except sqlite3.IntegrityError:
        return False, "❌ Email or Username already exists."
    finally:
        conn.close()

def login_user(email, password):
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, username FROM users WHERE email=?", (email,))
    row = cursor.fetchone()
    conn.close()
    
    if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
        return True, row[1] # Return success and username
    return False, "❌ Invalid email or password."

# ======================
# API Routes (for JSON)
# ======================
@app.route("/")
def index():
    return send_from_directory('templates', 'index.html')

@app.route("/app")
def app_page():
    return send_from_directory('templates', 'index.html')

@app.route("/test")
def test():
    return jsonify({"message": "Backend is accessible!", "timestamp": "2025-09-03"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing email or password"}), 400

    email = data["email"]
    password = data["password"]
    
    success, result = login_user(email, password)
    if success:
        # On success, send back the username
        return jsonify({"username": result}), 200 
    else:
        # On failure, send back the error message
        return jsonify({"error": result}), 401

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400

    email = data["email"]
    username = data["username"]
    password = data["password"]

    success, msg = register_user(email, username, password)
    if success:
        return jsonify({"message": msg}), 201
    else:
        return jsonify({"error": msg}), 400

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify({"messages": messages}), 200

@app.route("/messages", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data or not data.get('message') or not data.get('username'):
        return jsonify({"error": "Missing message or username"}), 400
    
    message = {
        "user": data["username"],
        "msg": data["message"]
    }
    messages.append(message)
    
    # Emit the message to all connected clients via Socket.IO
    socketio.emit('receive_message', message, broadcast=True)
    
    return jsonify({"success": True}), 201

# ======================
# Socket.IO Events
# ======================
@socketio.on("connect")
def handle_connect():
    print(f"Client connected: {request.sid}")
    emit("connection_status", {"status": "connected", "sid": request.sid})

@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client disconnected: {request.sid}")

@socketio.on("send_message")
def handle_message(data):
    print(f"Received message: {data}")
    if data and data.get('msg') and data.get('username'):
        message = {
            "user": data["username"],
            "msg": data["msg"]
        }
        messages.append(message)
        # Broadcast the message to all connected clients
        emit("receive_message", message, broadcast=True)
    else:
        emit("error", {"message": "Invalid message format"})

@socketio.on("join_chat")
def handle_join_chat(data):
    username = data.get('username')
    if username:
        join_room("chat_room")
        emit("user_joined", {"username": username}, room="chat_room")
        print(f"User {username} joined the chat")

@socketio.on("leave_chat")
def handle_leave_chat(data):
    username = data.get('username')
    if username:
        leave_room("chat_room")
        emit("user_left", {"username": username}, room="chat_room")
        print(f"User {username} left the chat")

# ======================
# Run the application
# ======================
if __name__ == "__main__":
    print("🚀 Starting University Chat App with direct Python execution")
    print("📡 Using Flask-SocketIO with threading mode (NOT eventlet)")
    print("🚫 NO gunicorn, NO eventlet, NO gevent")
    
    port = int(os.environ.get('PORT', 5000))
    print(f"🌐 Binding to host=0.0.0.0, port={port}")
    
    socketio.run(app, host="0.0.0.0", port=port, debug=False)
