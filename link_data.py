import csv
from bs4 import BeautifulSoup
import requests


url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Product%20Management&location=San%20Francisco%20Bay%20Area&geoId=90000084&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=0"
response = requests.get(url)

# soup = BeautifulSoup(response.content,'html.parser')
# job_title = soup.find('h3', class_='base-search-card__title').text.strip()
# print(job_title)
file = open('linkedin-jobs.csv', 'a')
writer = csv.writer(file)
writer.writerow(['Title', 'Company','Location','Apply'])

def link_scrapper(webpage, page_number):
    next_page= webpage + str(page_number)
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('div', class_= 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for job in jobs:
        job_title= job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
        job_location = job.find('span', class_= 'job-search-card__location').text.strip()
        job_link = job.find('a', class_= 'base-card__full-link')['href']

        writer.writerow([
            job_title.encode('utf-8'),
            job_company.encode('utf-8'),
            job_location.encode('utf-8'),
            job_location.encode('utf-8'),
        ])

    if page_number < 25:
        page_number = page_number + 25
        link_scrapper(webpage, page_number)
    else:
        file.close()
        print("file closed")


link_scrapper("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Product%20Management&location=San%20Francisco%20Bay%20Area&geoId=90000084&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=0",0)


