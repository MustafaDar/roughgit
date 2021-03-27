from ..app import app
from flask_sqlalchemy import SQLAlchemy


# configuration
# NEVER HARDCODE YOUR CONFIGURATION IN YOUR CODE
# INSTEAD CREATE A .env FILE AND STORE IN IT
if app:
    # This is secret key for use in project
    app.config['SECRET_KEY'] = "thisisyoursecretkey"
    # Database configration with postgresql
    app.config['SQLALCHEMY_DATABASE_URI'] = ""
    # Database track modification
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # Create sqlalchemy object
    db = SQLAlchemy(app)