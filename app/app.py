from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from endpoints.developers import Developer, Developers, DevQuery
from db import db

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///developer.db'
api.add_resource(Developers, "/developer")
api.add_resource(Developer, "/developer/<string:dev_id>")
api.add_resource(DevQuery, "/developer?<string:query>")

def initialize_app(app):
    """
    Initialize the application server

    Args:
        app -- Flask object

    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///developers.db'
    db.init_app(app)
    db.create_all(app=app)


def main():
    """
    Main function to initialize and run the Flask server
    
    """
    initialize_app(app)
    app.run(debug = True)

if __name__ == '__main__':
    main()