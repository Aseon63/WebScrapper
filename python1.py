#from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_last_page

# indeed_jobs = get_indeed_jobs()
#stackoverflow_jobs = get_stackoverflow_jobs()

# print(indeed_jobs)

so_page = get_last_page("https://stackoverflow.com/jobs?q=python&pg=1")
print(so_page)


# stackoverflow.py 에 에러 있음 last_page function에 문제 발견, page 읽지 못함 해결 하고 넘어갈 것, 2.9 강좌 참고