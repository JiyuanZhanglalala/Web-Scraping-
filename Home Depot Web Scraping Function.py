#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import random

def get_sore_and_Price(store_id,internet_id):
    driver = webdriver.Chrome('C:/Users/cunzh/Desktop/chromedriver.exe') ## you can delete this
    start_page = driver.get("https://www.homedepot.com/l/")
    driver.find_element_by_id("storeSearchBox").send_keys(store_id)
    driver.find_element_by_class_name("sfSearchbox__button").click()
    time.sleep(random.randint(3,5))
    Message=''
    try:
        store = driver.find_element_by_class_name('sfstores')
        store_name = store.find_element_by_class_name('sfstorename').text
    #print(store.get_attribute("outerHTML"))
    except:
        price="NA"
        Message="store cannot be found"
    else:
        
        a = store.find_element_by_class_name('sfstorelinks').find_element_by_tag_name('a')
        time.sleep(random.randint(3,5))
        a.click()
        time.sleep(random.randint(3,5))
    
    
        driver.find_element_by_id("headerSearch").send_keys(internet_id)
        time.sleep(random.randint(3,5))
        driver.find_element_by_id("headerSearchButton").click()
        time.sleep(random.randint(3,5))
        try:
            content = driver.find_element_by_class_name("price-detailed__wrapper")
            # print(content.get_attribute('innerHTML'))
            spans = content.find_elements_by_tag_name('span')
            if len(spans) != 3:
                price='NA'
                Message='price cannot be found'
            else:
                a = spans[1]
                b = spans[2]
                price = a.text + '.' + b.text
            
        except:
            price='NA'
            Message='price cannot be found'

    return store_id,price,Message


# In[ ]:

# We can test the code by using follwing example:
store_list = ['954', '907', '6917']
test_list = ['302895490', '302895488', '100561401', '206809290']
list1=[]
for store in store_list:
        for item in test_list:
            list1.append(get_sore_and_Price(store,item))


# In[ ]:


list1

