



#df to mongodb
# import pandas as pd
# from pymongo import MongoClient
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.service import Service
# import pandas as pd
# webdriver_service = Service("./chromedriver") 
# driver = webdriver.Chrome(service=webdriver_service)

# d = []
# driver.get('https://www.zalando.es/release-calendar/zapatillas-mujer/')
# driver.maximize_window()
# time.sleep(5)

# soup = BeautifulSoup(driver.page_source,"html.parser")
# price= [x.get_text(strip=True) for x in soup.select('.Wqd6Qu + div')]
# #print(price)
# title= [x.get_text(strip=True) for x in soup.select('.Wqd6Qu + div + div + div')]
# #print(title)

# date = [x.get_text(strip=True) for x in soup.select('.Wqd6Qu + div + div + div + div')]
# #print(date)

# cols = ['title', 'price', 'date']
  
# df = pd.DataFrame(data=list(zip(title,price,date)), columns=cols)
# #print(df)

# # Connect to MongoDB
# client =  MongoClient("mongodb+srv://mtest:password@cluster0.tvylfi7.mongodb.net/?retryWrites=true&w=majority")
# db = client['mquote_df']
# collection = db['mtd']
# df.reset_index(inplace=True)
# data_dict = df.to_dict("records")
# # Insert collection
# collection.insert_many(data_dict)





