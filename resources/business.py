import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import business
from schemas import BusinessSchema

blp = Blueprint("business", __name__, description="Database business registred")


@blp.route("/business")
class BusinessList(MethodView):
    def get(self):
        return {"business": list(business.values())}
    
    @blp.arguments(BusinessSchema)
    def post(self, business_data):

        for item in business_data.values():
            if business_data["businessName"] == item["businessName"]:
                abort(400, message="Business name provided already exists.")
        business_id = uuid.uuid4().hex
        newBusiness = {**business_data, "id": business_id}
        business[business_id] = newBusiness
        return newBusiness, 201


@blp.route("/business/<string:business_id>")
class Business(MethodView):
    def get(self, business_id):
        try:
            return business[business_id]
        except KeyError:
            abort(404, message="Business not found.")

    def delete(self, business_id):
        try:
            del business[business_id]
            return {"message": "Business deleted."}
        except KeyError:
            abort(404, message="Business not found.")