from selenium import webdriver
import timegit commit -

#moje_pierwsze_okno_chrome = webdriver.Chrome()
#moje_pierwsze_2_chrome = webdriver.Chrome()
#moje_pierwsze_1_firefox = webdriver.Firefox()


driver = webdriver.Chrome()
driver.get('https://google.com')
time.sleep(2)
driver.quit()