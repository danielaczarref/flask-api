from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column

class BankAccsModel(Base):
    __tablename__ = "bankAccs"
    
    id = Column(Integer, primary_key=True)
    acc = Column(Integer, nullable=False)
    agency = Column(Integer, nullable=False)
    bank = Column(String(100), nullable=False)
    business_id = mapped_column(ForeignKey("business.id"))
    business = relationship("BusinessModel", back_populates="bankAccs")
    
    def __init__(self, acc, agency, bank, business_id):
        self.acc = acc
        self.agency = agency
        self.bank = bank
        self.business_id = business_id

