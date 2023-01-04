from bs4 import BeautifulSoup
import requests

def extract_remoteok_jobs(keyword):
  Base_URL = f"https://remoteok.com/remote-{keyword}-jobs"
  request = requests.get(Base_URL, headers={"User-Agent": "Kimchi"})
  
  if request.status_code == 200:
      results=[]
      soup = BeautifulSoup(request.text, "html.parser")
      jobs = soup.find_all('table', id = 'jobsboard')
      for job_section in jobs:
          jobs_posts = job_section.find_all('tr', class_ = 'job')
          for jobss in jobs_posts:
              tds = jobss.find_all('td')
              CPCP = tds[1]
              position = CPCP.find('h2')
              company = CPCP.find('h3')
              anchors = CPCP.select('a', class_ = 'preventLink')
              anchor = anchors[0]
              region = CPCP.find_all('div', class_ = 'location')
              link = anchor['href']
              job_data = {
                  'position': position.string,
                  'link': f'https://remoteok.com/{link}',
                  'company': company.string,
                  'region': region[0].string
              }
              results.append(job_data)
      return(results)