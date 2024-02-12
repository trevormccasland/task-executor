from flask import Flask
from flask_seeder import FlaskSeeder
from flask_sqlalchemy import SQLAlchemy
from task_executor.db_integration.models import base

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://task_executor:secret@localhost:5432/task-executor"


db_integration = SQLAlchemy(app, model_class=base.Base)
seeder = FlaskSeeder()
seeder.init_app(app, db_integration)