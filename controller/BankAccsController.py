from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import BankAccSchema, BankAccUpdateSchema
from service.BankAccsService import BankAccsService

blp = Blueprint("Bank Accounts", "bank", description="Operations on bank accounts")

@blp.route("/bank/<int:company_id>")
class BankAccsList(MethodView):
    @blp.response(200, BankAccSchema(many=True))
    def get(self, company_id):
        return BankAccsService.getBankAccsList(self, company_id)
    
    
@blp.route("/bank/<int:company_id>/bank-acc/<int:bankacc_id>")
class GetBankAccount(MethodView):
    @blp.response(200, BankAccSchema)
    def get(self, company_id, bankacc_id):
        return BankAccsService.getBankAccById(self, company_id, id=bankacc_id)

    def delete(self, company_id, bankacc_id):
        return BankAccsService.deleteBankAcc(self, company_id, id=bankacc_id)

    @blp.arguments(BankAccUpdateSchema)
    @blp.response(201, BankAccSchema)
    def put(self, bankacc_data, company_id, bankacc_id):
        return BankAccsService.updateBankAcc(self, bankacc_data, company_id, id=bankacc_id)



@blp.route("/bank")
class CreateBankAccs(MethodView):
    @blp.arguments(BankAccSchema)
    @blp.response(201, BankAccSchema)
    def post(self, bankAcc_data):
        return BankAccsService.createBankAcc(self, bankAcc_data)
