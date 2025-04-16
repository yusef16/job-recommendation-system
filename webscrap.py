import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

df = pd.read_csv("dataset/Resume.csv")
df = df[['Category']]
unique_values = df['Category'].unique()

np.savetxt('output.txt', unique_values, fmt='%s')

URL1 = 'https://www.rabota.md/ro/vacancies/category/{}'
html_page = requests.get(URL1, headers={"User-Agent":"Mozilla/5.0"})


URL = 'https://www.rabota.md/ro/vacancies/category/hr'

link_array = []

def vacancies(predicted):
    if predicted == 'HR':
        URL = 'https://www.rabota.md/ro/vacancies/category/hr'
        html_page = requests.get(URL)
        soup = BeautifulSoup(html_page.text, "html.parser")
        links = soup.find_all('a', {
            "class": "vacancyShowPopup py-0.5 truncate text-[#18191C] hover:text-secondary mr-auto"})

        for a in links:
            href = a.get('href')
            if href:
                print("https://www.rabota.md" + href)
                full_link = "https://www.rabota.md" + href
                link_array.append(full_link)
        return link_array
    elif predicted == 'DESIGNER':
        URL = 'https://www.rabota.md/ro/vacancies/category/design'
    elif predicted == 'INFORMATION-TECHNOLOGY':
        URL = 'https://www.rabota.md/ro/vacancies/category/it'
    elif predicted == 'TEACHER':
        URL = 'https://www.rabota.md/ro/vacancies/category/teachers'
    elif predicted == 'ADVOCATE':
        URL = 'https://www.rabota.md/ro/vacancies/category/law'
    elif predicted == 'BUSINESS-DEVELOPMENT':
        URL = 'https://www.rabota.md/ro/vacancies/category/entertainment'
    elif predicted == 'HEALTHCARE':
        URL = 'https://www.rabota.md/ro/vacancies/category/health'
    elif predicted == 'FITNESS':
        URL = 'https://www.rabota.md/ro/vacancies/category/health'
    elif predicted == 'AGRICULTURE':
        URL = 'https://www.rabota.md/ro/vacancies/category/agriculture'
    elif predicted == 'BPO':
        URL = 'https://www.rabota.md/ro/vacancies/category/entertainment'
    elif predicted == 'SALES':
        URL = 'https://www.rabota.md/ro/vacancies/category/sales'
    elif predicted == 'CONSULTANT':
        URL = 'http://rabota.md/ro/jobs-chisinau-vanzator-consultant'
    elif predicted == 'DIGITAL-MEDIA':
        URL = 'https://www.rabota.md/ro/vacancies/category/media'
    elif predicted == 'AUTOMOBILE':
        URL = 'https://www.rabota.md/ro/jobs-chisinau-auto'
    elif predicted == 'CHEF':
        URL = 'https://www.rabota.md/ro/jobs-chisinau-bucatar'
    elif predicted == 'FINANCE':
        URL = 'https://www.rabota.md/ro/vacancies/category/banks'
    elif predicted == 'APPAREL':
        URL = 'https://www.rabota.md/ro/jobs-chisinau-vestimentatie'
    elif predicted == 'ENGINEERING':
        URL = 'https://www.rabota.md/ro/vacancies/category/engineering'
    elif predicted == 'ACCOUNTANT':
        URL = 'https://www.rabota.md/ro/vacancies/category/accounting'
    elif predicted == 'CONSTRUCTION':
        URL = 'https://www.rabota.md/ro/vacancies/category/building'
    elif predicted == 'PUBLIC-RELATIONS':
        URL = 'https://www.rabota.md/ro/jobs-chisinau-PR'
    elif predicted == 'BANKING':
        URL = 'https://www.rabota.md/ro/vacancies/category/banks'
    elif predicted == 'ARTS':
        URL = 'https://www.rabota.md/ro/vacancies/category/arts'
    elif predicted == 'AVIATION':
        URL = 'https://www.rabota.md/ro/jobs-moldova-agent-ticketing'


html_page = requests.get(URL)
soup = BeautifulSoup(html_page.text, "html.parser")
links = soup.find_all('a', {
    "class": "vip_company--name text-[17px] sm:text-xl block mb-0 sm:mb-1.5 mr-2.5 sm:mr-0 font-bold text-primary"})

for a in links:
    href = a.get('href')
    if href:
        print("https://www.rabota.md" + href)
