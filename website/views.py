from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import query
from sqlalchemy.sql.expression import desc
from werkzeug.utils import secure_filename
from .models import Gift, Item, Jewellery, Note, Watch

from . import db
from .static.scripts import database

import json
import hashlib

views = Blueprint('views', __name__)
itypes = ['Luxury Watch', 'Normal Watch',
          'Fashion Jewellery', 'Luxury Jewellery', 'Gifts']


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("index.html", user=current_user, types=itypes)


@views.route('/sales', methods=['GET', 'POST'])
@login_required
def sales():
    return render_template("sales.html", user=current_user, types=itypes)


@views.route('/items', methods=['GET', 'POST'])
@login_required
def items():
    return render_template("items.html", user=current_user, types=itypes)


@views.route('/repairs', methods=['GET', 'POST'])
@login_required
def repairs():
    return render_template("repairs.html", user=current_user, types=itypes)


@views.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    return render_template("search.html", user=current_user, types=itypes)


@views.route('/search_results', methods=['GET', 'POST'])
@login_required
def search_results():
    # if request.method == 'GET':
    #     type = request.form.get('select')
    #     search = request.form.get('search')

    #     if type is not None and search is not None:
    #         db.session.query()
    res = [{'itemid': 'a1', 'title': 'aaa', 'filename': 'aaa'}]

    return render_template("search_results.html", user=current_user, query=query, types=itypes, res=res)


@views.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    return render_template("index.html", user=current_user, types=itypes)


@views.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    return render_template("checkout.html", user=current_user, types=itypes)


@views.route('/postmethod', methods=['POST'])
@login_required
def postmethod():
    jsdata = request.form['data']
    iid = database.db_getDetails(jsdata)
    params = {'itemid': iid}
    return jsonify(params)


# @views.route('/add_to_cart', methods=['GET', 'POST'])
# @login_required
# def add_to_cart():
#     # ask request to return item id and price
#     itemid = request.args.get('itemid')
#     price = request.form['price']

#     prod_id = database.db



#     username = getusername()
#        # usuario no logueado
#        if username == None:
#             print(username)
#             if vacio == False:
#                 print('False')
#                 setcart()
#             movie = database.db_getMovie(movieid)
#             movie.append(price)
#             prod_id = database.db_getProductId(movieid, price)
#             movie.append(prod_id)
#             addcart(movie)
#         # usuario logueado
#         else:
#             prodid = database.db_getProductId(movieid, price)
#             customerid = getcustomerid()
#             database.db_addToCart(customerid, prodid)

#             cart = getcart()
#             if cart != None:
#                 for x in cart:
#                     prodid = x[3]
#                     contador = getcontador()
#                     for i in range(0, contador[prodid]):
#                         database.db_addToCart(customerid, prodid)
#             cleancart()

#         return redirect(url_for('checkout'))


@views.route('/description/', methods=['GET', 'POST'])
@login_required
def description():
    itemid = request.args.get('itemid')

    res = db.session.query(Item).filter(Item.itemid==itemid).all()

    if (res[2] == 'WATL' or res[2] == 'WATN'):
        stock = db.session.query(Watch).filter(Watch.itemid==itemid).one()
    elif (res[2] == 'GIFT'):
        stock = db.session.query(Gift).filter(Gift.itemid==itemid).one()
    elif (res[2] == 'JWLL' or res[2] == 'JWLF'):
        stock = db.session.query(Jewellery).filter(Jewellery.itemid==itemid).one()
    else:
        stock = None

    return render_template("description.html", user=current_user, types=itypes, item=res, stock=stock)


@views.route('/insert', methods=['GET', 'POST'])
@login_required
def insert():
    return render_template("insert.html", user=current_user, types=itypes)

@views.route('/inserted', methods=['GET', 'POST'])
@login_required
def inserted():
    itemid = request.form['itemid']
    name = request.form['name']
    type = request.form['type']
    description = request.form['description']
    buyPrice = request.form['buyPrice']
    sellPrice = request.form['sellPrice']
    discount = request.form['discount']

    imgs = request.files['img']
    imgurls = []
    for img in imgs:
        imgurls.append('images/' + str(hash(img)) + '.png')

    watid = request.form['watid']
    jwlid = request.form['jwlid']
    gftid = request.form['gftid']

    ii = None

    if watid != None: 
        res = db.session.query(Watch).filter(Watch.stockid == watid).count()
        if res == 0:
            stockid = watid
            clockwork = request.form['clockwork']
            calibre = request.form['calibre']
            caseMaterial = request.form['caseMaterial']
            caseShape = request.form['caseShape']
            caseWidth = request.form['caseWidth']
            caseDepth = request.form['caseDepth']
            glassType = request.form['glassType']
            dial = request.form['dial']
            dialColour = request.form['dialColour']
            bracelet = request.form['bracelet']
            clasp = request.form['clasp']
            features = request.form['features']
            batteryCharge = request.form['batteryCharge']
            service = request.form['service']
            diamondNo = request.form['diamondNo']
            diamondCarat = request.form['diamondCarat']
            diamondQuality = request.form['diamondQuality']
            noColoured = request.form['noColoured']
            colours = request.form['colours']
            itemid = itemid
            stockno = 1

            ii = Watch(stockid, clockwork, calibre, caseMaterial, caseShape, caseWidth, caseDepth, glassType, dial, dialColour, bracelet, clasp, features, batteryCharge, service, diamondNo, diamondCarat, diamondQuality, noColoured, colours, itemid)
        else: 
            stockno = res + 1 

    elif jwlid != None:
        res = db.session.query(Jewellery).filter(Jewellery.stockid == jwlid).count()
        if res == 0:
            stockid = jwlid   
            design = request.form['design']
            claspType = request.form['claspType']
            chainLength = request.form['chainLength']
            ringSize = request.form['ringSize']
            ringWidth = request.form['ringWidth']
            colour = request.form['colour']
            clarity = request.form['clarity']
            cut = request.form['cut']
            quality = request.form['quality']
            material = request.form['material']
            materialGroup =request.form['materialGroup']
            alloy = request.form['alloy']
            unitWeight = request.form['unitWeight']
            itemid = itemid
            stockno = 1

            ii = Jewellery(stockid, design, claspType, chainLength, ringSize, ringWidth, colour, clarity, cut, quality, material, materialGroup, alloy, unitWeight, itemid)
        else:
            stockno = res + 1

    elif gftid != None:
        res = db.session.query(Gift).filter(Gift.stockid == jwlid).count()
        if res == 0:
            stockid = gftid
            articleGroup = request.form['articleGroup']
            articleKind = request.form['articleKind']
            brand = request.form['brand']
            productLine = request.form['productLine']
            collection = request.form['collection']
            itemid = itemid
            stockno = 1

            ii = Gift(stockid, articleGroup, articleKind, brand, productLine, collection, itemid)
        else:
            stockno = res + 1

    i = Item(itemid, name, type, description, imgurl, buyPrice, sellPrice, discount, stockno, watid, jwlid, gftid)
    db.session.add(i)
    db.session.commit()

    if ii != None:
        db.session.add(ii)
        db.session.commit()

    return redirect(url_for('index'))


#########################################################

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("index.html", user=current_user, types=itypes)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
