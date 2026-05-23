from sqlalchemy import select
from sqlalchemy.orm import Session

from models.cart import Cart
from models.order import Order
from models.order_items import OrderItems
from models.product import Product
from services.cart_items import return_cart
from services.cart_items import delete_item_from_cart
from utils.exceptions import OrderProcessError


def checkout(session: Session, user_id: int):
    try:
        session.add(Order(user_id=user_id, status="Pending", total_prices=0.0))
        session.commit()

        order = session.execute(select(Order).where(Order.user_id == user_id)).scalars().first()
        cart = session.execute(select(Cart).where(Cart.user_id == user_id)).scalars().first()
        cart_items = return_cart(session, cart_id=cart.cart_id)

        for item in cart_items:
            product = session.execute(select(Product).where(Product.product_id == item.product_id)).scalars().first()
            order.total_prices += product.price * item.quantity
            session.add(OrderItems(order_id=order.order_id, product_id=item.product_id, quantity=item.quantity,
                                   unit_price=product.price))
            delete_item_from_cart(item.cart_id, item.cart_items_id, session)

        session.commit()
        session.refresh(order)
        return order
    except Exception as e:
        session.rollback()
        raise OrderProcessError(f"An Error occurred while processing the order: {e}")