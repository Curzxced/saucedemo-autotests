from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_successful_checkout_flow(auth_user):
    # добавляем товар и переходим в корзину
    inventory = InventoryPage(auth_user)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # начинаем оформление заказа
    cart = CartPage(auth_user)
    cart.click_checkout()

    # заполняем данные доставки и завершаем покупку
    checkout = CheckoutPage(auth_user)
    checkout.fill_shipping_info("Ivan", "Ivanov", "123456")
    checkout.finish_order()

    # проверяем финальный экран
    assert "Thank you for your order!" in checkout.get_success_message()
