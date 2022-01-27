from selenium import webdriver
import pandas as pd
import time
#import sys
#URL=sys.agrv[1]
#Item=sys.agrv[2]
dfL=[]
pages= True
#Boot Chrome W Custom Options
options=webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

#Open Browser
def BestBuyTrawl(Item):
    global dfL
    browser =webdriver.Chrome()
    browser.get("https://bestbuy.ca")
    search_bar=browser.find_element_by_class_name('textField_e79SD')
    search_bar.send_keys(Item)
    search_bar.submit()
    time.sleep(5)
    # while pages == True:
    #     try:
    #         nextbutton=browser.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div[2]/button')
    #         nextbutton.click()
    #         pages = True
    #         time.sleep(5)
    #     except NoSuchElementException:
    #         pages= False
    item_price=browser.find_elements_by_class_name('productPricingContainer_3gTS3')
    print("UwU")
    item_name=browser.find_elements_by_class_name('productItemName_3IZ3c')
    #Initialize List
    titles_list = []
    prices_list= []
    for title in item_name:
        titles_list.append(title.text)
    for price in item_price:
        prices_list.append(price.text)
    
    #Create List
    dfL =pd.DataFrame(zip(titles_list, prices_list), columns=['ItemName', 'Price'])
    #dfL =dfL[dfL['ItemName'].str.contains('Case')==False]
    dfL['Price'] = dfL['Price'].str.replace('$', '')
    dfL['Price'] = dfL['Price'].str.replace(',', '')
    browser.quit()
    
def IkeaTrawl(Item):
    global idfL
    Item=str(Item)
    browser =webdriver.Chrome()
    browser.get("https://www.ikea.com/ca/en/")
    search_bar=browser.find_element_by_class_name('search-field__input')
    search_bar.send_keys(Item)
    search_bar.submit()
    time.sleep(5)
    #This section still needs to be changed to fit Ikea
    # while pages == True:
    #     try:
    #         nextbutton=browser.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div[2]/button')
    #         nextbutton.click()
    #         pages = True
    #         time.sleep(5)
    #     except NoSuchElementException:
    #         pages= False
    item_price=browser.find_elements_by_class_name('product-compact__price')
    item_dims=browser.find_elements_by_class_name('product-compact__type')
    #Initialize List
    iprices_list= []
    idims_list=[]
    for price in item_price:
        iprices_list.append(price.text)
    for dim in item_dims:
        idims_list.append(dim.text)
    
    #Create List
    idfL =pd.DataFrame(zip(idims_list, iprices_list), columns=['ItemName', 'Price'])
    #dfL =dfL[dfL['ItemName'].str.contains('Case')==False]
    idfL['Price'] = idfL['Price'].str.replace('$', '')
    idfL['Price'] = idfL['Price'].str.replace(',', '')
    browser.quit()

