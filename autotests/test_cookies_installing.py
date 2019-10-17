from selenium import webdriver
def test_cookies__installing():                                             #Объявляем тестовый метод
    wd = webdriver.Firefox(executable_path='D:\\Selenium\\geckodriver.exe') #Инициализируем драйвер
    wd.get('http://localhost:58001/')
    cookies = wd.get_cookies()
    if len(wd.find_elements_by_css_selector("div.NPS"))==0:                 #Проверка, что если всплываюшее окно не показано (Не найден элемент div с классом NPS_message ), то куки не устанавливаются
        assert len(cookies)==0
    else:
        assert len(cookies)==1                                              #Проверка, что если всплываюшее окно показано, то куки устанавливаются и количество установленных кук = 1

    wd.close()

