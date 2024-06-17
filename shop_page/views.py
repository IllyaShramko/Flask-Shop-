import flask, flask_login
from project.settings import DATABASE
from registration_page.models import User
from .models import Product

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
def render_shop_page():
    global value_tf, value
    is_admin = False
    if flask.request.method == "POST":
        value += 1
        if not value_tf:
            value_tf = True
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
        template_name_or_list= "shop.html",
        user = flask_login.current_user.login,
        value1 = value,
        valuetf = value_tf,
        products = Product.query.all(),
        int = int,
        is_admin = is_admin
    )