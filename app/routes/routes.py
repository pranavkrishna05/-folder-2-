"""
Define application routes.
"""

from flask import Blueprint
from auth.controllers import auth_controller
from products.controllers import product_controller
from cart.controllers import cart_controller
from checkout.controllers import checkout_controller
from orders.controllers import order_controller
from reviews.controllers import review_controller
from promotions.controllers import promotion_controller
from analytics.controllers import analytics_controller
from support.controllers import support_controller

routes_bp = Blueprint("routes", __name__)

# Auth routes
routes_bp.add_url_rule("/auth/register", view_func=auth_controller.register, methods=["POST"])
routes_bp.add_url_rule("/auth/login", view_func=auth_controller.login, methods=["POST"])

# Product routes
routes_bp.add_url_rule("/products", view_func=product_controller.get_products, methods=["GET"])
routes_bp.add_url_rule("/products/<int:product_id>", view_func=product_controller.get_product, methods=["GET"])

# Cart routes
routes_bp.add_url_rule("/cart", view_func=cart_controller.get_cart, methods=["GET"])
routes_bp.add_url_rule("/cart/add", view_func=cart_controller.add_to_cart, methods=["POST"])

# Checkout routes
routes_bp.add_url_rule("/checkout", view_func=checkout_controller.process_checkout, methods=["POST"])

# Order routes
routes_bp.add_url_rule("/orders", view_func=order_controller.get_orders, methods=["GET"])
routes_bp.add_url_rule("/orders/<int:order_id>", view_func=order_controller.get_order, methods=["GET"])

# Review routes
routes_bp.add_url_rule("/reviews", view_func=review_controller.get_reviews, methods=["GET"])
routes_bp.add_url_rule("/reviews/add", view_func=review_controller.add_review, methods=["POST"])

# Promotions routes
routes_bp.add_url_rule("/promotions", view_func=promotion_controller.get_promotions, methods=["GET"])

# Analytics routes
routes_bp.add_url_rule("/analytics", view_func=analytics_controller.get_analytics, methods=["GET"])

# Support routes
routes_bp.add_url_rule("/support", view_func=support_controller.get_support_info, methods=["GET"])