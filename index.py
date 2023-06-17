from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = "https://shopee.co.id/Laptop-cat.11044364.11044440"
driver.get(url)
sleep(10)

driver.execute_script("window.scrollTo(0, (document.body.scrollHeight / 5));")
sleep(5)
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight / 4));")
sleep(5)
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight / 3));")
sleep(5)
driver.execute_script("window.scrollTo(0, (document.body.scrollHeight / 2));")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)

req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')

items = soup.select('.col-xs-2-4.shopee-search-item-result__item')
for item in items:
    title = item.select_one('.WoKSjC').text.strip()
    sold = item.select_one('.wOebCz').text.strip()
    print(title, ' - ', sold)