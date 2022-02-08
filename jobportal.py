from bs4 import BeautifulSoup
import requests
import time
import os,sys

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=software+developer&txtLocation=United+States').text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    print(jobs)
    for index, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if '1' in published_date:
            company_name  = job.find('h3',class_='joblist-comp-name')
            skills = job.find('span',class_='srp-skills').text
            more_info = job.header.h2.a["href"]
            with open(os.path.join(sys.path[0],'posts', f"file{index}.txt"),'w') as file:
                file.write(f"Company: {company_name.text.strip()} \n")
                file.write(f"Required Skills: {skills.strip().replace('  ,  ', ', ')} \n")
                file.write(f"More Info: {more_info} ")
            print(f'File file{index}.txt saved!')

if __name__=="__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes')
        time.sleep(time_wait*60)

