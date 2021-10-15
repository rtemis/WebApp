from sqlalchemy.orm import backref
from sqlalchemy.sql.expression import true
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


############################################################
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    type = db.Column(db.String(15))
    notes = db.relationship('Note')
##############################################################


class Employee(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    position = db.Column(db.String(150))
    hireDate = db.Column(db.DateTime(timezone=True), default=func.now())
    # One employee many sales
    sales = db.relationship('Sale')

    def __init__(self, email, password, firstname, lastname, position):
        self.email = email
        self.password = password
        self.firstName = firstname
        self.lastName = lastname
        self.position = position



class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    document = db.Column(db.String(150), unique=True)
    birthday = db.Column(db.DateTime(timezone=True), default=func.now())
    clientSince = db.Column(db.DateTime(timezone=True), default=func.now())
    # One client many sales 
    history = db.relationship('Sale')
    repairs = db.relationship('Repair')


class Item(db.Model):

    itemid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    type = db.Column(db.String(4))
    description = db.Column(db.String(1000))
    imgurl = db.Column(db.String(1000))
    buyPrice = db.Column(db.Float)
    sellPrice = db.Column(db.Float)
    discount = db.Column(db.Float)
    inStock = db.Column(db.Integer)

    watid = db.Column(db.Integer, db.ForeignKey('watch.stockid'), nullable=True)
    jwlid = db.Column(db.Integer, db.ForeignKey('jewellery.stockid'), nullable=True)
    gftid = db.Column(db.Integer, db.ForeignKey('gift.stockid'), nullable=True)


# class ItemType(db.Model):
#     __tablename__ = 'itemtypes'
    
#     typeid = db.Column(db.Integer, primary_key=True)
#     itemtype = db.Column(db.String(4))
#     stock_id = db.Column(db.Integer, db.ForeignKey('Item.stockid'))
    
    
class Watch(db.Model):
    stockid = db.Column(db.Integer, primary_key=True)
    
    clockwork = db.Column(db.String(150))
    calibre = db.Column(db.String(150))
    caseMaterial = db.Column(db.String(150))
    caseShape = db.Column(db.String(150))
    caseWidth = db.Column(db.String(150))
    caseDepth = db.Column(db.String(150))
    glassType = db.Column(db.String(150))
    dial = db.Column(db.String(150))
    dialColour = db.Column(db.String(150))
    bracelet = db.Column(db.String(150))
    clasp = db.Column(db.String(150))
    features = db.Column(db.String(150))
    batteryCharge = db.Column(db.String(150))
    service = db.Column(db.String(150))
    diamondNo = db.Column(db.String(150))
    diamondCarat = db.Column(db.String(150))
    diamondQuality = db.Column(db.String(150))
    noColoured = db.Column(db.String(150))
    colours = db.Column(db.String(150))
    
    itemid = db.relationship('Item')



class Jewellery(db.Model):
    stockid = db.Column(db.Integer, primary_key=True)
    
    design = db.Column(db.String(150))
    claspType = db.Column(db.String(150))
    chainLength = db.Column(db.String(150))
    ringSize = db.Column(db.String(150))
    ringWidth = db.Column(db.String(150))
    colour = db.Column(db.String(150))
    clarity = db.Column(db.String(150))
    cut = db.Column(db.String(150))
    quality = db.Column(db.String(150))
    material = db.Column(db.String(150))
    materialGroup = db.Column(db.String(150))
    alloy = db.Column(db.String(150))
    unitWeight = db.Column(db.Float)

    itemid = db.relationship('Item')


class Gift(db.Model):
    stockid = db.Column(db.Integer, primary_key=True)

    articleGroup = db.Column(db.String(150))
    articleKind = db.Column(db.String(150))
    brand = db.Column(db.String(150))
    productLine = db.Column(db.String(150))
    collection = db.Column(db.String(150))

    itemid = db.relationship('Item')


class Repair(db.Model):
    __tablename__ = 'repairs'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))
    repairImgs = db.Column(db.String(1000))
    status = db.Column(db.Integer)
    inDate = db.Column(db.DateTime(timezone=True), default=func.now())
    dueDate = db.Column(db.DateTime(timezone=True), default=func.now())
    client_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    itemid = db.Column(db.Integer, db.ForeignKey('item.itemid'))


class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    description = db.Column(db.String(1000))
    itemid = db.Column(db.Integer, db.ForeignKey('item.itemid'))
    client_id = db.Column(db.Integer, db.ForeignKey('customer.id'))


class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    sale_date = db.Column(db.DateTime(timezone=True), default=func.now())
    client_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    itemid = db.Column(db.Integer, db.ForeignKey('item.itemid'))

# # -- Item type codes --
# # --- WAT - luxury watches
# # --- WATN - normal watches
# # --- JWLL - fine jewellery
# # --- JWLF - fashion jewellery
# # --- GIFT - gifts


