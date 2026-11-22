from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_items_and_check_badge(auth_user):
    inventory = InventoryPage(auth_user)

    # добавляем два разных товара
    inventory.add_backpack_to_cart()
    inventory.add_bike_light_to_cart()

    # проверяем счетчик на иконке корзины
    assert inventory.get_cart_badge_count() == "2"


def test_remove_item_from_cart(auth_user):
    inventory = InventoryPage(auth_user)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart = CartPage(auth_user)

    # убеждаемся что товар в корзине и удаляем его
    assert cart.get_items_count() == 1
    cart.remove_backpack()

    # проверяем что корзина пустая
    assert cart.get_items_count() == 0
