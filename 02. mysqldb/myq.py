


#pip install mysql-connector-python
#OR
#pip3 install mysqlclient

#import MySQLdb
# import pymysql
# pymysql.install_as_MySQLdb()

#only sqlalchemy works
#pip install sqlalchemy

# from sqlalchemy import create_engine, types # with or without types works
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.service import Service
# import pandas as pd
# webdriver_service = Service("./chromedriver")
# driver = webdriver.Chrome(service=webdriver_service)


# conn = create_engine('mysql://root:password@localhost/myquote_db') # enter your password and database names here
# d = []
# driver.get('https://www.example.com')
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

# df.to_sql(name='lan3', con = conn, if_exists = 'replace', index = False)

