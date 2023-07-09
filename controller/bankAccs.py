from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import session, conn
from models.businessModel import BusinessModel
from models.bankAccsModel import BankAccsModel
from schemas import BusinessSchema,BankData

blp = Blueprint("Bank Accounts", "bank", description="Operations on bank accounts")

@blp.route("/bank/<int:business_id>")
class BankAccsList(MethodView):
    @blp.response(200, BankData(many=True))
    def get(self, business_id):
        bankAccsData = session.query(BankAccsModel).filter(BankAccsModel.business_id == business_id).all()
        return bankAccsData
    
@blp.route("/bank")
class CreateBankAccs(MethodView):
    @blp.arguments(BankData)
    @blp.response(201, BankData)
    def post(self, bankAcc_data):
        bankAcc_item = BankAccsModel(**bankAcc_data)
        try:
            session.add(bankAcc_item)
            session.commit()
        except IntegrityError:
            session.rollback()
            abort(
                400,
                message="Business id does not exist."
            )
        except SQLAlchemyError:
            session.rollback()
            abort(500, message="An error occurred creating a new Bank Account. Please contact our Support Channel")
        return bankAcc_item
        


@blp.route("/business/<int:business_id>")
class Business(MethodView):
    @blp.response(200, BusinessSchema)
    def get(self, business_id):
        businessItem = BusinessModel.query.get_or_404(business_id)
        return businessItem

    def delete(self, business_id):
        businessItem = BusinessModel.query.get_or_404(business_id)
        session.delete(businessItem)
        session.commit()
        return {"message": "Business deleted"}, 200