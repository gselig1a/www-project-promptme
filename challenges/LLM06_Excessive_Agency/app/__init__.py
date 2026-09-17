from flask import Flask
app = Flask(__name__)
app.secret_key = "llm06-demo-secret-key"  # demo-only, needed for session-based admin auth
from app import routes
