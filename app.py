from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from models import db

# Import Blueprints
from routes.tasks_routes import tasks_bp
from routes.calendar_routes import calendar_bp
from routes.notes_routes import notes_bp
from routes.health_routes import health_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lifeos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    app.register_blueprint(calendar_bp, url_prefix='/calendar')
    app.register_blueprint(notes_bp, url_prefix='/notes')
    app.register_blueprint(health_bp, url_prefix='/health')

    # Serve OpenAPI schema
    @app.route("/openapi.json")
    def openapi():
        return send_from_directory(".", "openapi.json", mimetype="application/json")

    # Serve Claude plugin manifest
    @app.route("/.well-known/ai-plugin.json")
    def serve_manifest():
        return send_from_directory(".well-known", "ai-plugin.json", mimetype="application/json")

    # Serve static files like logo
    @app.route('/static/<path:filename>')
    def serve_static(filename):
        return send_from_directory('static', filename)

    # Optional: Serve legal info page
    @app.route("/legal")
    def legal():
        return "<h1>LifeOS Legal</h1><p>This is a sample legal page.</p>"

    return app


if __name__ == "__main__":
    app = create_app()

    # Create DB tables safely on startup
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=8000)
