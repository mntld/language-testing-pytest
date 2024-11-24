import time

def test_add_to_cart_button(browser):
    # Ссылка на товар
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Визуальная проверка языка
    # Проверяем наличие кнопки добавления в корзину
    button = browser.find_element("css selector", ".btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена!"
