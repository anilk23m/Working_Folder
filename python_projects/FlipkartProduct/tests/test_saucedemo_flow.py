from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD

def test_saucedemo_end_to_end(page):

    # Login
    login = LoginPage(page)
    login.load()
    login.login(USERNAME, PASSWORD)

    # Add product
    inventory = InventoryPage(page)
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    # Cart validation
    cart = CartPage(page)
    assert cart.verify_product_in_cart()

    cart.click_checkout()

    # Checkout
    checkout = CheckoutPage(page)
    checkout.fill_details("Anil", "Kumar", "560001")
    checkout.continue_checkout()
    checkout.finish_order()

    # Verification
    assert "Thank you for your order!" in checkout.get_success_message()