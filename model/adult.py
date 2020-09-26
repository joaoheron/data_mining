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
        return "<Orders(order_id='%s', created_at='%s', discount='%s', product_id='%s', quantity='%s', subtotal='%s', tax='%s', total='%s', user_id='%s')>" % (
            self.order_id, self.created_at, self.discount, self.product_id, self.quantity, self.subtotal, self.tax, self.total, self.user_id)


# age: continuous.
# workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
# fnlwgt: continuous.
# education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# education-num: continuous.
# marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
# occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
# relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
# race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
# sex: Female, Male.
# capital-gain: continuous.
# capital-loss: continuous.
# hours-per-week: continuous.
# native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
# class: >50K, <=50K