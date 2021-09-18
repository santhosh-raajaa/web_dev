from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
db_name="database.db"


def create_app():
	app=Flask(__name__)
	app.config["SECRET_KEY"]="mypp62000"
	app.config['SqlAlchemy_database_URI']=f"sqlite:///{db_name}"
	db.init_app(app)

	from .views import views
	from .auth import auth

	app.register_blueprint(views,url_prefix='/')
	app.register_blueprint(auth,url_prefix='/')
	return app
