from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_items_and_check_badge(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    
    # тут добавление двух разных товаров
    inventory.add_backpack_to_cart()
    inventory.add_bike_light_to_cart()
    
    # проверка что счетчик на иконке корзины обновился
    assert inventory.get_cart_badge_count() == "2"

def test_remove_item_from_cart(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    
    from pages.cart_page import CartPage
    cart = CartPage(driver)
    
    # в корзине 1 товар, удаляем его
    assert cart.get_items_count() == 1
    cart.remove_backpack()
    
    # проверяем что корзина стала пустая
    assert cart.get_items_count() == 0