from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome("/home/anil/Desktop/chromedriver")
driver.get("https://m.youtube.com/results?search_query=pubg+live")
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
for i in soup.findAll('a',attrs={'class':'yt-simple-endpoint style-scope ytd-video-renderer'}):
    print(i.get('href'))


  
 
   




