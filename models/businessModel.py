from db import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class BusinessModel(Base):
    __tablename__ = "business"

    id = Column(Integer, primary_key = True, autoincrement=True)
    businessName = Column(String(300), unique=True, nullable=False)
    phone = Column(String(20), unique=False, nullable=True)
    address = Column(String(300), unique=False, nullable=True)
    registrationDate = Column(Date, nullable=False)
    billing = Column(String(25), unique=False, nullable=False)
    bankAccs = relationship("BankAccsModel", back_populates="business",lazy="dynamic")

    def __init__(self, businessName, phone, 
                address, registrationDate, 
                billing, bankAccs):
        self.businessName = businessName
        self.phone = phone
        self.address = address
        self.registrationDate = registrationDate
        self.billing = billing
        self.bankAccs = bankAccs


    

