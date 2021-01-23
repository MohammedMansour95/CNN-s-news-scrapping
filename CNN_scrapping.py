from selenium import webdriver
from time import sleep
from newspaper import Article
from newspaper import fulltext
import requests

driver = webdriver.Chrome( executable_path='chromedriver.exe')


# لتحميل محتويات الصفحه كامله
driver.get("https://edition.cnn.com/specials/politics/fact-check-politics")
sleep(5)
first_len = 0
last_len = len(driver.find_elements_by_class_name('zn__containers'))
while first_len != last_len:
    containers = driver.find_elements_by_class_name('zn__containers')
    first_len = len(containers)
    containers[len(containers)-1].location_once_scrolled_into_view
    sleep(5)
    containers = driver.find_elements_by_class_name('zn__containers')
    last_len = len(containers)


#لأستخراج البيانات
link_list=[]
containers = driver.find_elements_by_class_name('zn__containers')
for cont in range(1,len(containers)):
    li = containers[cont].find_elements_by_tag_name('li')
    for l in li:
        article = l.find_elements_by_tag_name('article')
        for art in article:
            link = 'https://edition.cnn.com'+art.get_attribute('data-vr-contentbox')
            is_containt_img =False
            if (('/videos/' not in art.get_attribute('data-vr-contentbox')) and (link!='https://edition.cnn.com')):
                print('-----------------------')
                print(link)
                link_list.append(link)

for l in link_list :
  try:
      if l.endswith('index.html'):
        article = Article(l)
        article.download()
        article.parse()
        url=requests.get(l).text
        text = fulltext(url)
        print("Title: ", article.title)
        print("Authors: ", article.authors)
        print("Date: ", article.publish_date)
        #print("Full text:",text)
        print("top_image:",article.top_image)
        print("image:",article.url)
  except :
    print("link error")
    
                
               

