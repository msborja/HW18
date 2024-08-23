import json

import allure
from allure_commons.types import AttachmentType
from selene import browser, query
import requests


class AddProduct:
    def __init__(self):
        self.session = requests.Session()
        self.cookie = None

    @allure.story('Добавление товара через api')
    def add_product(self, id_products):
        url = 'https://demowebshop.tricentis.com/addproducttocart/catalog/'
        for id_product in id_products:
            with allure.step(f'Отправка POST запроса с ID товара {id_product}'):
                response = self.session.post(url + id_product)
                allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name='Response',
                              attachment_type=AttachmentType.JSON, extension='json')

                with allure.step('Проверка Status Code'):
                    assert response.status_code == 200
        with allure.step('Получение cookie'):
            self.cookie = response.cookies.get('Nop.customer')
            allure.attach(body=str(response.cookies), name='Cookies', attachment_type=AttachmentType.TEXT,
                          extension='txt')

        return self

    @allure.story('Открытие корзины')
    def open_cart(self):
        with allure.step('Открытие браузера'):
            browser.open('')
        with allure.step('Добавление Cookie'):
            browser.driver.add_cookie({"name": "Nop.customer", "value": self.cookie})
        with allure.step('Перезагрузка браузера'):
            browser.driver.refresh()

        return self

    def check_add_product(self, names_products):
        with allure.step('Проверка наличия товаров в корзине'):
            for name_product in names_products:
                product_elements = browser.all('.product-name')
                found = False
                for element in product_elements:
                    if element.get(query.text) == name_product:
                        found = True
                        break
                assert found, f'Продукт {name_product} не найден в корзине'

            return self


add_product_api = AddProduct()
