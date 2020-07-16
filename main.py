from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PageObject import BasePage
import csv
import jieba
import jieba.analyse

class target_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        driver.get('https://udndata.com/ndapp/Searchdec?udndbid=udnfree&page=1&SearchString=%B3%B0%A5%CD%2B%A4%E9%B4%C1%3E%3D20100724%2B%A4%E9%B4%C1%3C%3D20200701%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%7C%B8%67%C0%D9%A4%E9%B3%F8%7C%C1%70%A6%58%B1%DF%B3%F8%2B&sharepage=50&select=0&kind=2')
        self.driver.set_window_size(1024, 768)
    def custom_get_text(self,*arg):
        return super().custom_get_text(*arg)
    def go_to_page(self, page):
        driver.get('https://udndata.com/ndapp/Searchdec?udndbid=udnfree&page='+str(page)+'&SearchString=%B3%B0%A5%CD%2B%A4%E9%B4%C1%3E%3D20100724%2B%A4%E9%B4%C1%3C%3D20200701%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8%7C%B8%67%C0%D9%A4%E9%B3%F8%7C%C1%70%A6%58%B1%DF%B3%F8%2B&sharepage=50&select=0&kind=2')



driver = webdriver.Chrome("./chromedriver")
target_page = target_page(driver)
data_table=[]
for j in range(1,92):
    target_page.go_to_page(j)
    for i in range(1,51):
        title = (By.XPATH, '//*[@id="mainbar"]/section/div[6]/ul/li['+str(i)+']/div/h2/a')
        content = (By.XPATH, '//*[@id="mainbar"]/section/div[6]/ul/li['+str(i)+']/div/p')
        date_time = (By.XPATH, '//*[@id="mainbar"]/section/div[6]/ul/li[4]/div/span')
        title_text=target_page.custom_get_text(*title)
        content_text=target_page.custom_get_text(*content)
        time_code = target_page.custom_get_text(*date_time) 

        if content_text != None:
            print(title_text)
            print(content_text)
            print(time_code[:10])
            tags = jieba.analyse.extract_tags(content_text, topK=5)
            print(tags)
            data_table.append([title_text,content_text,time_code[:10],tags])


with open("new_file.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data_table)
driver.close();
driver.quit();