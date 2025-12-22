from typing import Optional
from app.models.shopping_cart import ShoppingCart, ShoppingCartItem
from app.repositories.shopping_cart_repository import ShoppingCartRepository
from app.repositories.product_repository import ProductRepository

class ShoppingCartService:
    """
    Service class for managing shopping cart operations.
    """
    
    def __init__(self, shopping_cart_repository: ShoppingCartRepository, product_repository: ProductRepository) -> None:
        self.shopping_cart_repository = shopping_cart_repository
        self.product_repository = product_repository
    
    def add_product(self, user_id: Optional[int], product_id: int, quantity: int) -> ShoppingCart:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        shopping_cart = self._get_or_create_cart(user_id)

        cart_item = next((item for item in shopping_cart.items if item.product_id == product_id), None)
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = ShoppingCartItem(shopping_cart_id=shopping_cart.id, product_id=product_id, quantity=quantity)
            self.shopping_cart_repository.save_item(cart_item)
        
        return shopping_cart
    
    def remove_product(self, user_id: Optional[int], product_id: int) -> ShoppingCart:
        shopping_cart = self.shopping_cart_repository.find_by_user_id(user_id)
        if not shopping_cart:
            raise ValueError("Shopping cart not found")
        
        cart_item = next((item for item in shopping_cart.items if item.product_id == product_id), None)
        if not cart_item:
            raise ValueError("Product not found in shopping cart")
        
        self.shopping_cart_repository.delete_item(cart_item)
        return shopping_cart
    
    def modify_quantity(self, user_id: Optional[int], product_id: int, quantity: int) -> ShoppingCart:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        shopping_cart = self.shopping_cart_repository.find_by_user_id(user_id)
        if not shopping_cart:
            raise ValueError("Shopping cart not found")
        
        cart_item = next((item for item in shopping_cart.items if item.product_id == product_id), None)
        if not cart_item:
            raise ValueError("Product not found in shopping cart")
        
        cart_item.quantity = quantity
        self.shopping_cart_repository.save_item(cart_item)
        return shopping_cart
    
    def _get_or_create_cart(self, user_id: Optional[int]) -> ShoppingCart:
        shopping_cart = self.shopping_cart_repository.find_by_user_id(user_id)
        if not shopping_cart:
            shopping_cart = ShoppingCart(user_id=user_id)
            self.shopping_cart_repository.save(shopping_cart)
        return shopping_cart