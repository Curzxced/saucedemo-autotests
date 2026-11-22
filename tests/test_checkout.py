from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_successful_checkout_flow(driver):
    # авторизуемся
    LoginPage(driver).login("standard_user", "secret_sauce")
    
    # добавляем товар и идем в корзину
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    
    # начинаем оформление
    cart = CartPage(driver)
    cart.click_checkout()
    
    # заполняем данные и завершаем заказ
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_info("Ivan", "Ivanov", "123456")
    checkout.finish_order()
    
    # проверяем фин экран
    assert "Thank you for your order!" in checkout.get_success_message()