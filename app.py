from flask import Flask
from flask_smorest import Api
from controller.CompanyController import blp as CompanyBlueprint
from controller.BankAccsController import blp as BankAccsBlueprint
import db

def createApp():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"]      = True
    app.config["API_TITLE"]                 = "BHub Company RESP API"
    app.config["API_VERSION"]               = "v1"
    app.config["OPENAPI_VERSION"]           = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"]        = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]   = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]    = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    api.register_blueprint(CompanyBlueprint)
    api.register_blueprint(BankAccsBlueprint)

    db.Base.metadata.create_all(db.engine)
    db.session = db.Session()

    return app

if __name__:
    app = createApp()
    app.run(debug=True)