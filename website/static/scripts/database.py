import os
import hashlib
import random

from sqlalchemy import create_engine, func, exc
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select

from ... import db

#######################################
#         Basic insert queries        #
#######################################
insertItem = """INSERT INTO items_table """
insertWatch = """INSERT INTO """
insertJewellery = """INSERT INTO """
insertGift = """INSERT INTO """


#######################################
#         Basic select queries        #
#######################################
selectItem = """SELECT * FROM items WHERE itemid=%s"""

# Queries
def db_getDetails(stockid):
    try:
        item = []

        db_conn = None
        db_conn = db.connect()

        resul = db_conn.execute(selectItem, (stockid,))

        db_conn.close()

        return resul

    except exc.SQLAlchemyError as error:
        if db_conn is not None:
            db_conn.close()
            print ('************ Error in items table *****************')
            print (error)
            return None

