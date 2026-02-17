from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
    from app.routes import bp as main_bp
    
    app.register_blueprint(main_bp)
    
    return app
