from flask import Flask
from .auth import register_auth_routes
from .analytics import register_analytics_routes
from .cart import register_cart_routes
from .checkout import register_checkout_routes
from .orders import register_orders_routes
from .products import register_products_routes
from .promotions import register_promotions_routes
from .reviews import register_reviews_routes
from .support import register_support_routes


def register_controllers(app: Flask):
    register_auth_routes(app)
    register_analytics_routes(app)
    register_cart_routes(app)
    register_checkout_routes(app)
    register_orders_routes(app)
    register_products_routes(app)
    register_promotions_routes(app)
    register_reviews_routes(app)
    register_support_routes(app)