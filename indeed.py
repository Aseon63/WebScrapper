import requests
from bs4 import BeautifulSoup

LIMIT = 50
#url 에서 맨끝에 start 부분이 생략됨, 이는 페이지를 지정하기 위함
url = f"https://kr.indeed.com/jobs?q=python&l=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&limit={LIMIT}&radius=25"

#indeed 구직 사이트에서 존재하는 페이지 수를 알아내는 function, 한 페이지당 50개의 결과가 나오게 설정됨
def extract_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))
    last_page = pages[-1]
    return(last_page)

#indeed 에서 각 구직 마다 구직업종, 회사명, 회사위치 를 가져오는 작업
def extract_job_for_indeed(html):
    title = html.find("div", {"class":"title"}).find("a")["title"]
    company = html.find("span", {"class":"company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
                company = str(company_anchor.string)
        else:
            company = str(company.string)
    else:
        company: None
    company = company.strip()
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title':title, 'company':company, 'location':location, 'link':f"https://kr.indeed.com/viewjob?jk={job_id}"}

# extract_job_for_indeed(html) 을 통해 가져온 리스트들을 list로 변환하여 반환하는 function
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Indeed의 페이지 {page+1}의 python 개발자 구직 정보")
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job_for_indeed(result)
            jobs.append(job)
        print(jobs)

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs

#url for indeed https://kr.indeed.com/jobs?q=python&l=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&limit=50&radius=25&start=50
