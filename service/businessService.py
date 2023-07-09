from db import session
from models.businessModel import BusinessModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_smorest import abort

class BusinessService():
    def getBusinessList(self):
        return session.query(BusinessModel).all()

    def createNewBusiness(self, business_data):
        businessItem = BusinessModel(**business_data)
        try:
            session.add(businessItem)
            session.commit()
        except IntegrityError:
            session.rollback()
            abort(
                400,
                message="Business name provided already exists."
            )
        except SQLAlchemyError:
            session.rollback()
            abort(500, message="An error occurred creating a new Business. Please contact our Support Channel")

        return businessItem
    
    def getBusinessById(self, id):
        return BusinessModel.query.get_or_404(id)
    
    def deleteBusiness(self, id):
        businessItem = session.query(BusinessModel).get(id)
        session.delete(businessItem)
        session.commit()
        return {"message": "Business deleted"}, 200