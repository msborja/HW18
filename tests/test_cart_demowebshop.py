import allure
from demowebshop_tests.pages.cart_page import add_product_api
from demowebshop_tests.test_data.data import ID_PRODUCT_1, NAME_PRODUCT_1, ID_PRODUCT_2, NAME_PRODUCT_2, ID_PRODUCT_3, \
    NAME_PRODUCT_3

@allure.story('Добавление и проверка наличия всех товаров в корзине')
def test_add_all_product():
    add_product_api.add_product([ID_PRODUCT_1, ID_PRODUCT_2, ID_PRODUCT_3])
    add_product_api.open_cart()
    add_product_api.check_add_product([NAME_PRODUCT_1, NAME_PRODUCT_2, NAME_PRODUCT_3])
