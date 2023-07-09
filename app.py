from flask import Flask
from flask_smorest import Api
# from resources.business import blp as BusinessBlueprint
from controller.business import blp as BusinessBlueprint
from controller.bankAccs import blp as BankAccsBlueprint
import db

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"]      = True
app.config["API_TITLE"]                 = "Business RESP API"
app.config["API_VERSION"]               = "v1"
app.config["OPENAPI_VERSION"]           = "3.0.3"
app.config["OPENAPI_URL_PREFIX"]        = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"]   = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"]    = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(BusinessBlueprint)
api.register_blueprint(BankAccsBlueprint)

db.Base.metadata.create_all(db.engine)
db.session = db.Session()
db.conn = db.engine.connect()
