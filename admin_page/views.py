import flask, flask_login, os
from project.settings import DATABASE
from registration_page.models import User
from shop_page.models import Product

# products1 = [
#     {
#         "name":"iPhone 15 Pro Max 256GB Natural Titanium",
#         "price": 49999,
#         "discount": 10,
#         "capacity1": "256 Гб",
#         "capacity2": "512 Гб",
#         "capacity3": "1 Тб"
#     },
#     {
#         "name": "SmartPhone Vivo V9 2018 Cup",
#         "price": 4999,
#         "discount": 20,
#         "capacity1": "64 Гб",
#         "capacity2": "128 Гб",
#         "capacity3": "256 Гб"
#     }
# ]

value = 0
value_tf = False
def render_admin_page():
    if flask.request.method == "POST":
        try:
            if flask.request.form.get('del'):
                product_id = int(flask.request.form['del'])
                print(product_id)
                product_del = Product.query.get(product_id)

                if Product.query.get(product_id) != None:
                    DATABASE.session.delete(product_del)
                    DATABASE.session.commit() 
                    os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/imgs/{product_del.name}.png")) 
            elif flask.request.form.get('submit-change'):
                #
                list_values = flask.request.form.get('submit-change').split('-')
                print(list_values)
                product_name = Product.query.get(int(list_values[1]))
                #
                if list_values[0] == 'image':
                    os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/imgs/{product_name.name}.png"))
                    image_save = flask.request.files['image']
                    image_save.save(os.path.abspath(__file__ + f"/../../shop_page/static/imgs/{product_name.name}.png"))
                #    
                elif list_values[0] == 'name':
                    get_name = flask.request.form.get('name')
                    
                    absolute_path = os.path.abspath(__file__ + f'/../../shop_page/static/imgs') 
                    os.rename(src= absolute_path + f'/{product_name.name}.png', dst= absolute_path + f'/{get_name}.png')
                    product_name.name = get_name
                    DATABASE.session.commit()   
                elif list_values[0] == 'price':
                    get_price = flask.request.form.get('price')
                    product_name.price = get_price
                    DATABASE.session.commit()   
                elif list_values[0] == 'discount':
                    get_discount = flask.request.form.get('discount')
                    product_name.discount = get_discount
                    DATABASE.session.commit()
                elif list_values[0] == "newProduct":
                    next = True
                    for product in Product.query.all():
                        if product.name == flask.request.form['newProductName']:
                            if product.price == int(flask.request.form['newProductPrice']):
                                if product.discount == int(flask.request.form['newProductDiscount']):
                                    next = False
                    if next:
                        new_product = Product(
                            name = flask.request.form['newProductName'],
                            price = int(flask.request.form['newProductPrice']),
                            discount = int(flask.request.form['newProductDiscount']),
                            capacity1 =  "128 Гб",
                            capacity2 =  "256 Гб",
                            capacity3 =  "512 Гб"
                        )
                        DATABASE.session.add(new_product)
                        DATABASE.session.commit()
                        print(flask.request.files['newProductImage'])
                        image_save = flask.request.files['newProductImage']
                        
                        image_save.save(os.path.abspath(__file__ + f"/../../shop_page/static/imgs/{new_product.name}.png"))
        except Exception as e:
            print(e)
            print(flask.request.form)

    # if len(Product.query.all()) == 0:
    #     for product_data in products1:
    #         product = Product(
    #             name = product_data['name'],
    #             price = product_data['price'],
    #             discount = product_data['discount'],
    #             capacity1 = product_data['capacity1'],
    #             capacity2 = product_data['capacity2'],
    #             capacity3 = product_data['capacity3']
    #         )
    #         DATABASE.session.add(product)
    #     DATABASE.session.commit()
    is_admin = flask_login.current_user.is_admin

    return flask.render_template(
        template_name_or_list= "admin.html",
        user = flask_login.current_user.login,
        products = Product.query.all(),
        int = int, is_admin = is_admin
    )
