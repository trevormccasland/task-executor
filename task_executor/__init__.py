from flask import Flask
from flask_login import LoginManager
from flask_seeder import FlaskSeeder
from flask_sqlalchemy import SQLAlchemy
from task_executor.db.models import Base

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://task_executor:secret@localhost:5432/task-executor"
)


repository = SQLAlchemy(app, model_class=Base)
seeder = FlaskSeeder()
seeder.init_app(app, repository)
login_manager = LoginManager()
login_manager.init_app(app)
