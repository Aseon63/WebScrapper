import requests
from bs4 import BeautifulSoup

page = 1
#stackoverflow python 개발자 모집 url
url = "https://stackoverflow.com/jobs?q=python"

def get_last_page(html):
    result = requests.get(html)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"}).find_all('a')
    pages = []
    for link in pagination:
        pages.append(int(pagination.find("span").string))
    last_page = pages[-1]
    return last_page

def extract_job(html):
    title = html.find("h2",{"class":"mb4"}).find("a")["title"]
    return {'title': title}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
        
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    print(jobs)


#stackoverflow url https://stackoverflow.com/jobs?q=python&pg=1