from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from sys import platform
from time import sleep
import datetime

error = '⛔'
warning = '⚠'
ok = '✅'
oc = '🖥'
like = '👍'
all_sleep = 3
like_sleep = 2


def get_data_time():
    time_now = datetime.datetime.now()
    return time_now.strftime("%d-%m-%Y %H:%M")

def get_OC():
    """
    Определить ОС.
    :return: информация об ОС и путь к chromedriver.exe
    """
    if platform == "linux" or platform == "linux2":
        time_now = datetime.datetime.now()
        information = "[" + time_now.strftime("%d-%m-%Y %H:%M") + '] {} Ваша ОС Linux'.format(oc)
        put = ""
        return information, put

    elif platform == "darwin":
        time_now = datetime.datetime.now()
        information = "[" + time_now.strftime("%d-%m-%Y %H:%M") + '] {} Ваша ОС Mac'.format(oc)
        put = ""
        return information, put

    elif platform == "win32":
        time_now = datetime.datetime.now()
        information = "[" + time_now.strftime("%d-%m-%Y %H:%M") + '] {} Ваша ОС Windows'.format(oc)
        put = "chromedriver_for_win/chromedriver.exe"
        return information, put

def information_from_txt_files():
    """
    Читаем фалы .txt
    :return: Информацию. Логин. Сообщения.
    """
    information = ''
    with open('log.txt', 'r') as file:
        log = file.read()
        information += "[" + get_data_time() + \
                       '] {} Логин для входа на сайт Tinder: {}'.format(ok, log)

    return information, log

def close_start_popups(browser):
    """
    Закрываем всплывающее окно.
    :param browser: парметр запущенного браузера.
    :return: информация
    """
    sleep(all_sleep)
    try:
        browser.find_element_by_xpath('//button[@aria-label="Закрыть"]').click()
        return "[" + get_data_time() + "] {} Всплывающее окно закрыто.".format(ok)
    except ElementNotInteractableException as err:
        return "[" + get_data_time() + '] {} ' + err + ''.format(error)
    except NoSuchElementException as err:
        return "[" + get_data_time() + '] {} Не нашел всплавающего окна.'.format(error)

def log_in_using_your_phone(browser):
    """
    Нажимаем кнопку Войти с помощью номера телефона.
    :param browser: парметр запущенного браузера.
    :return: информация
    """
    sleep(all_sleep)
    try:
        browser.find_element_by_xpath('//div[@id="modal-manager"]').find_element_by_xpath(
            '//button[@aria-label="Войти с помощью номера телефона"]').click()
        return "[" + get_data_time() + "] {} Войти с помощью номера телефона.".format(ok)
    except ElementNotInteractableException as err:
        return "[" + get_data_time() + '] {} ' + err + ''.format(error)
    except NoSuchElementException as err:
        browser.find_element_by_xpath('//button[text()="Другие варианты"]').click()
        return log_in_using_your_phone(browser)

def input_number_phone(browser, log):
    """
    Вводим номер телефона.
    :param browser: парметр запущенного браузера.
    :param log: номер телефона.
    :return: информация.
    """
    sleep(all_sleep)
    try:
        browser.find_element_by_name('phone_number').send_keys(log)
        return "[" + get_data_time() + '] {} Введен номер телефона {}'.format(ok, log)
    except NoSuchElementException:
        return "[" + get_data_time() + '] {} Не нашел окна для ввода телефона.'.format(error)

def go_on(browser):
    """
    Нажимаем кнопку Продолжить.
    :param browser: парметр запущенного браузера.
    :return: информация.
    """
    sleep(all_sleep)
    try:
        browser.find_element_by_xpath('//span[text()="Продолжить"]').click()
        return "[" + get_data_time() + '] {} Нажата кнопка Продолжить'.format(ok)
    except NoSuchElementException:
        return "[" + get_data_time() + '] {} Не нашел кнопки Продолжить.'.format(error)

def input_cod(browser):
    """
    Ввод кода.
    :param browser: парметр запущенного браузера.
    :return: информация.
    """
    try:
        kod_numbers = code_check()
        kod = browser.find_elements_by_xpath('//input[@type="tel"]')
        n = 0
        for i in kod:
            i.send_keys(kod_numbers[n])
            n += 1
        return "[" + get_data_time() + '] {} Код введен.'.format(ok)
    except NoSuchElementException:
        return "[" + get_data_time() + '] {} Не нашел полей для ввода кода.'.format(error)

def code_check():
    """
    Проверка введеного кода.
    :return: введенный код
    """
    kod_numbers = input("[" + get_data_time() + "] {} Введите код: ".format(warning))
    if len(kod_numbers) != 6:
        print("[" + get_data_time() + '] {} Код не верный.'.format(error))
        return code_check()
    else:
        print("[" + get_data_time() + '] {} Формат кода проверен.'.format(ok))
        return kod_numbers

def geolocation_ok(browser):
    """
    Разрешаем геолокацию.
    :param browser: парметр запущенного браузера.
    :return: информация.
    """
    sleep(all_sleep)
    try:
        browser_button = browser.find_elements_by_tag_name("button")
        button_list = {i.text: i for i in browser_button}
        if "РАЗРЕШИТЬ" in button_list.keys():
            button = [value for key, value in button_list.items() if key == "РАЗРЕШИТЬ"]
            button[0].click()
            return "[" + get_data_time() + '] {} Геолокация разрешена.'.format(ok)
        else:
            return "[" + get_data_time() + '] {} Не нашел полей Разрешить для Геолокации.'.format(error)
    except NoSuchElementException:
        return "[" + get_data_time() + '] {} Не нашел полей Разрешить для Геолокации.'.format(error)

def notice_off(browser):
    """
    Отключаем оповещения.
    :param browser: парметр запущенного браузера.
    :return: информация.
    """
    sleep(all_sleep)
    try:
        browser_button = browser.find_elements_by_tag_name("button")
        button_list = {i.text: i for i in browser_button}
        if "НЕИНТЕРЕСНО" in button_list.keys():
            button = [value for key, value in button_list.items() if key == "НЕИНТЕРЕСНО"]
            button[0].click()
            return "[" + get_data_time() + '] {} Уведомления отключены.'.format(ok)
        else:
            return "[" + get_data_time() + '] {} Не нашел поле Неинтерсно для Уведомлений.'.format(error)
    except NoSuchElementException:
        return "[" + get_data_time() + '] {} Не нашел поле Неинтерсно для Уведомлений.'.format(error)

def popup_windows_off(browser):
    """
    Закрываем всплывающие окна.
    :param browser: парметр запущенного браузера.
    :return: информация.
    """
    sleep(like_sleep)
    try:
        browser_button = browser.find_elements_by_tag_name("button")
        button_list = {i.text: i for i in browser_button}
        if "НЕИНТЕРЕСНО" in button_list.keys():
            button = [value for key, value in button_list.items() if key == "НЕИНТЕРЕСНО"]
            button[0].click()
            print("[" + get_data_time() + '] {} Всплавающее окно.'.format(ok))
    except NoSuchElementException:
        pass

def click_like(browser):
    """
    Нажимаем LIKE.
    :param browser: парметр запущенного браузера.
    :return: информация.
    """
    sum_like = 0
    while True:
        try:
            popup_windows_off(browser)
            browser.find_element_by_xpath('//button[@aria-label="Лайк"]').click()
            sum_like += 1
            print("[" + get_data_time() + '] {} - {}'.format(like, str(sum_like)))
        except NoSuchElementException:
            print("[" + get_data_time() + '] {} Не нашел поле Лайк.'.format(error))