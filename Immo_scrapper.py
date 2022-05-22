import json as _json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(2)


email=driver.find_element_by_id("email")
email.send_keys("onsdridi90@yahoo.com")
password=driver.find_element_by_id("pass")
password.send_keys("espoire44*")
time.sleep(1)
login=driver.find_element_by_name("login")
login.click()
time.sleep(2)
driver.get("https://www.facebook.com/Tunisie-tabarka-immobilier-1867350173541484/")#time.sleep(4)

posts = []
for c in range(1,20):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_posts = soup.find_all("div", {"class": "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"})
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

for post in all_posts:
    post = post.find("div").get_text()

    print(post)
    posts.append(post)


list_posts=[]
posts_dict=dict()
for i in range(len(posts)):
    annonce={"annonce"+" "+str(i): posts[i] }
    key="annonce"+" "+str(i)
    posts_dict[key]=posts[i]
    list_posts.append(annonce)


with open("posts.json", mode="w") as posts_file:
      _json.dump(posts_dict,posts_file)



client=MongoClient('localhost', 27017)
db=client.Immo
print(list_posts)
print(db.Annonces)
for el in list_posts:
    db.Annonces.insert_one(el)