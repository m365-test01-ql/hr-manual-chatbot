import os
import logging
from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name=None):
    """Application factory function"""
    
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Setup logging
    logging.basicConfig(level=app.config['LOG_LEVEL'])
    
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Enable CORS
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Register blueprints
    from routes.documents import documents_bp
    from routes.chat import chat_bp
    from routes.health import health_bp
    
    app.register_blueprint(health_bp)
    app.register_blueprint(documents_bp, url_prefix='/api/documents')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')
    
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)