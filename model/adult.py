from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Adult(Base):
    __tablename__ = 'adult'

    age = Column("age", Integer) # primary_key=True
    workclass = Column("Created At", String)
    fnlwgt = Column("Discount", String)
    education = Column("Product ID", String)
    education_num = Column("Quantity", String)
    marital_status = Column("Subtotal", String)
    occupation = Column("Tax", String)
    relationship = Column("Total", String)
    race = Column("User ID", String)
    sex = Column("User ID", String)
    capital_gain = Column("User ID", String)
    capital_loss = Column("User ID", String)
    hours_per_week = Column("User ID", String)
    native_countr = Column("User ID", String)

    def __repr__(self):
        return "<Adult(age='%s', workclass='%s', fnlwgt='%s', education='%s', education_num='%s', marital_status='%s', occupation='%s', relationship='%s', race='%s', sex='%s', capital_gain='%s', capital_loss='%s', hours_per_week='%s', native_countr='%s' )>" % (
            self.age, self.workclass, self.fnlwgt, self.education, self.education_num, self.marital_status, self.occupation, self.relationship, self.race, self.sex, self.capital_gain, self.capital_loss, self.hours_per_week, self.native_countr)
