##AUTOOEVALUACIOOONn!!!##
import os
from flask import Flask
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# para correr Xampp en ubuntu:
#  sudo /opt/lampp/manager-linux-x64.run

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
#app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
#jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
load_dotenv()

from app.views import views
