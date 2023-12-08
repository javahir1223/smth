import requests
from bs4 import BeautifulSoup
import re
response = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Python+Scripting%22&txtKeywords=%22Python+Scripting%22&txtLocation=").text
soup = BeautifulSoup(response,"lxml")

jobs = soup.findAll("li",class_="clearfix job-bx wht-shd-bx")

# # print(title)
# # published_date = soup.find("span", class_ = "sim-posyed").span.text
# # print(published_date)
# result = []
with open("smth.txt","w") as f:
    
    for job in jobs:
        dtl = soup.find("ul", class_="top-jd-dtl clearfix")
        name = soup.find('a').text
        publ_list = job.find("span",class_="sin-posted")
        salary = dtl.findAll('li')[1].text
        # print(salary)
        # print(name)
        # print(publ_list
    text = f"""
        smth:{name}
        oylik:{salary}
        sana:{publ_list}
"""
    f.write(text)



#all pages

# respons = requests.get("https://soffstudy.uz/posts").text
# soup = BeautifulSoup(respons,"lxml")
# maqomalar = soup.findAll("div",class_="card-info")
# name = maqomalar.find("h4",class_="mt-15 color-white").text
# date = maqomalar.find("span", class_="color-gray-700 text-sm timeread").text
# with open ("maqomalar.txt","a") as f:
#     for maqoma in maqomalar:
#         name = maqoma.find("h4",class_="mt-15 color-white").text
#         date = maqoma.find("span", class_="color-gray-700 text-sm timeread").text 
#     f.write(f"nomi:{name}, soni:{date}")

#timesjob all
#how do smth as^^^ this im


# respons = requests.get("https://soffstudy.uz/posts").text
# soup = BeautifulSoup(respons,"lxml")
# images = soup.findAll("img",class_="h-100")
# # images = images.find_all('crc')
# # print(images)
# a = "maqomalar.cvc"
# with open (a,"a+") as f:
#     f.readlines()
# print("this has been added")
    





