import time
from bs4 import BeautifulSoup
import requests
import json
import os

url = "https://internshala.com/internships/"


html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

jobs=soup.find_all("div",class_="internship_meta")

# print("Put some unfamiliar skills you want to filter out",jobs)

for job in jobs:

    companys=job.find("div", class_="individual_internship_header")
    
    posted = job.find("div", class_="tags_container_outer").div.div.div.div.text
  

    locations = job.find("div", class_="individual_internship_details")
    location=locations.find("div", id="location_names").span.a.text
    # print(location)

    company = companys.find("div", class_="company")
    profile=company.h3.text.strip()
    company_name = company.find("div", class_="heading_6 company_name").text.strip()


    if "home" in location:

    

        print(f'''
        Company: {company_name}
        Location: {location}
        Posted On: {posted}
        Profile: {profile}

        ''')

