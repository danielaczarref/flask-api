from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import BusinessSchema
from service.businessService import BusinessService

blp = Blueprint("Business", "business", description="Operations on business")

@blp.route("/business")
class BusinessList(MethodView):
    @blp.response(200, BusinessSchema(many=True))
    def get(self):
        return BusinessService.getBusinessList(self)
    
    @blp.arguments(BusinessSchema)
    @blp.response(201, BusinessSchema)
    def post(self, business_data):
        return BusinessService.createNewBusiness(self,business_data)
        


@blp.route("/business/<int:business_id>")
class Business(MethodView):
    @blp.response(200, BusinessSchema)
    def get(self, business_id):
        return BusinessService.getBusinessById(self,business_id)

    def delete(self, business_id):
        return BusinessService.deleteBusiness(self, id=business_id)