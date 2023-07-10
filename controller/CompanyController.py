from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import CompanySchema, CompanyUpdateSchema
from service import CompanyService

blp = Blueprint("Company", "company", description="Operations on companies")


@blp.route("/company")
class CompanyList(MethodView):
    @blp.response(200, CompanySchema(many=True))
    def get(self):
        return CompanyService.getCompanyList(self)

    @blp.arguments(CompanySchema)
    @blp.response(201, CompanySchema)
    def post(self, company_data):
        return CompanyService.createNewCompany(self, company_data)


@blp.route("/company/<int:company_id>")
class Company(MethodView):
    @blp.response(200, CompanySchema)
    def get(self, company_id):
        return CompanyService.getCompanyById(self, company_id)

    def delete(self, company_id):
        return CompanyService.deleteCompany(self, id=company_id)

    @blp.arguments(CompanyUpdateSchema)
    @blp.response(201, CompanySchema)
    def put(self, company_data, company_id):
        return CompanyService.updateCompany(self, company_data, id=company_id)
