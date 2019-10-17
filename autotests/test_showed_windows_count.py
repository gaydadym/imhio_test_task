from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
import time
def test_showed_windows_count():                                             #Объявляем тестовый метод
    wd = webdriver.Firefox(executable_path='D:\\Selenium\\geckodriver.exe')  #Инициализируем драйвер
    i = 0                                                                    #Инициализируем счетчик количества открытий страницы
    showed_windows_count = 0                                                 #Инициализируем счетчик количеств показов всплывающего окна
    wd.implicitly_wait(0.1)
    while i < 100:                                                           #Устанавливаем количество открытий страницы равным 100
        wd.delete_all_cookies()
        wd.get('http://localhost:58001/')
        try:
            EC.element_to_be_clickable(wd.find_element_by_css_selector("div.NPS"))
            i += 1
            time.sleep(0.5)
            cookies = wd.get_cookies()
            showed_windows_count += 1                                        # Увеличиваем значение счетчика показов всплывающего окна
            wd.delete_all_cookies()                                          # Стираем все куки
            i += 1

        except NoSuchElementException:
            i += 1                                                            #Увеличивам значение счетчика количества открытий страницы

    print("Окно было показано "+showed_windows_count.__str__()+" из "+ i.__str__()+" раз")
    assert showed_windows_count==10                                           #Проверяем процент показов всплывающего окна пользователям. Он должен быть равен 10%
    wd.close()                                                                #Закрываем браузер



...
