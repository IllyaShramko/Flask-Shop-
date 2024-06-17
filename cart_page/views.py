import flask, flask_login
from registration_page.models import User
count_of_products= None
valuetf= None
def render_cart_page():
    global count_of_products, valuetf
    check_basket = False
    valuetf = True
    if flask.request.cookies:
        try:
            list_id_products = flask.request.cookies.get('products').split(' ')
            list_products = [[]]
            list_same_id = []
            # count_products = [[]]
            for id_product in list_id_products:
                list_products[-1].append(list_id_products.count(id_product))
                if id_product not in list_same_id:
                    if id_product == "1":
                        list_products[-1].append("iPhone")
                    elif id_product == "2":
                        list_products[-1].append("Vivo")
                    list_same_id.append(id_product)
                    list_products.append([])
            check_basket = True
        except:
            list_products = [[0, "None"]]
        # count_of_products= 0
        
        is_admin = flask_login.current_user.is_admin
        return flask.render_template(
            template_name_or_list = "cart.html",
            products = list_products,
            check_basket = check_basket, 
            count_of_products = count_of_products,
            valuetf = valuetf,
            user = flask_login.current_user.login, is_admin = is_admin
        )
    else:
        return flask.render_template(template_name_or_list = "cart.html", check_basket = check_basket)