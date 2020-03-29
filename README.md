# bot_tinder

<blockquote>В данной статье я буду использовать браузер <b>Chrome.</blockquote>
  <p><h2><b>Подготовка.</b></h2>
<p>1)	Создадим папку с проектом <b>bot_tinder</b>;
<p>2)	В папке <b>bot_tinder</b> создадим подпапки с названиями <b>chromedriver_for_win</b> и <b>chromedriver_for_mac</b>, и <b>chromedriver_for_lin</b> (так как реализацию делаем для 3 ОС Windows, macOS, Linux);
<p>3)	Скачаем <b><a href="https://chromedriver.chromium.org/downloads">webdriver</a></b> под вашу версию браузера (я использую Chrome, если используете Firefox то можно скачать от <b><a href="https://github.com/mozilla/geckodriver/releases">сюда</a></b>), для большего сходства с моей реализации можете скачать для каждой ОС. 
Скаченные файлы размещаем по папкам <b>chromedriver_for_win</b>, <b>chromedriver_for_mac</b>, <b>chromedriver_for_lin</b>;
<blockquote>*Если скачали только для своей ОС, ничего страшного, т.к. в коде мы это предусмотрим.</blockquote>
<p>4)	В папке <b>bot_tinder</b> создадим файл с названием <b>log.txt</b> (в нем будет храниться номер телефона по которому будет заходить в Tinder). Формат без восьмерки: 9851234567
<p>5)	Поместим в папку <b>bot_tinder</b> файлы <b>tinder.py</b>, <b>function.py</b>.
