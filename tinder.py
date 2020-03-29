# -*- coding: utf-8 -*-
from selenium import webdriver

from function import get_OC, information_from_txt_files, close_start_popups, notice_off, click_like
from function import log_in_using_your_phone, input_number_phone, go_on, input_cod, geolocation_ok

def tinder():
    # Определение ОС
    info, put = get_OC()
    print(info)

    # путь к драйверу chrome
    chromedriver = put
    options = webdriver.ChromeOptions()
    options.add_argument('--start-minimize')
    # options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    # browser.minimize_window()

    # После успешного входа в систему переходим на страницу
    browser.get('https://tinder.com/app/recs')

    # Открываем txt файлы с данными
    info_txt, log = information_from_txt_files()
    print(info_txt)
    # Закрываем в начале всплывающее окно
    print(close_start_popups(browser))
    # Нажимаем Вход с помощью телефона
    print(log_in_using_your_phone(browser))
    # Вводим номер телефона
    print(input_number_phone(browser, log))
    # Нажимаем кнопку Продолжить
    print(go_on(browser))
    # Вводим код
    print(input_cod(browser))
    # Нажимаем кнопку Продолжить
    print(go_on(browser))
    # Нажимаем кнопку Разрешить определять геолокацию
    print(geolocation_ok(browser))
    # Нажимаем Выключить уведомления
    print(notice_off(browser))
    # Нажимаем Лайк
    click_like(browser)

if __name__=='__main__':
    tinder()