from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime 

url = "https://rabota.by/search/vacancy?text=junior+python&salary=&ored_clusters=true&enable_snippets=true"
url_nbrb = "https://www.nbrb.by/statistics/rates/ratesdaily.asp"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'}

job_dict = {}
job_numbers = 0

def get_min_solary(text):
    token_out = ''
    if '–' in text:
        token_out = text.replace(' ','').split(' ', 3)[3]
        text_out = text.replace(' ','').split()[0]
    elif 'от' or 'до' in text:
        token_out = text.replace(' ','').split(' ', 3)[2]
        text_out = text.replace(' ','').split()[1]
    return  text_out, token_out


def get_currency_course(url):
    df = pd.DataFrame(columns=['Name', 'Amount', 'Token', 'Cours'])
    response = requests.get(url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    table = soup.find("table",{"class":"currencyTable"})
    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        if (columns != []):
            name = columns[0].text.strip()
            amount = columns[1].text.strip()
            amount_count = amount.split()[0]
            token = amount.split()[1]
            cours = columns[2].text.strip().replace(',','.')
            df.loc[len(df)] = [name, amount_count, token, cours] 
    return df


def page_parser(url, job_dict, job_numbers):
    
    response = requests.get(url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    jobs = soup.find_all("div",{"class":"serp-item"})
    
    for job in jobs:
        title = job.find("a", {"class":"serp-item__title"}).text
        location_tag = job.find("div", {"data-qa":"vacancy-serp__vacancy-address"})
        location = location_tag.text.split(',', 1)[0] if location_tag else None
        link = job.find('a', {'class':'serp-item__title'}).get('href')
        solary_tag = job.find("span", {"data-qa":"vacancy-serp__vacancy-compensation"})
        if solary_tag:
            solary, token = get_min_solary(solary_tag.text)  
        else: solary, token = '0', 'N/A' 

        job_response = requests.get(link, headers=headers)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, 'html.parser')
        job_data_creation_tag = job_soup.find('p',{'class':'vacancy-creation-time-redesigned'})
        job_data_creation = '-'.join(job_data_creation_tag.text.split()[2:5]) if job_data_creation_tag else None
        job_numbers += 1
        print(job_numbers)
        job_dict[job_numbers] = [title, float(solary), token, location, link, job_data_creation]
        #print('Job Title:', title, '\nLocation:', location, '\nLink:', link, '\nCreation:', *job_data_creation,  '\n---------------')
    return soup.find('a', {"data-qa":"pager-next"}), job_dict, job_numbers


while True:
    url_tag, job_dict, job_numbers = page_parser(url, job_dict, job_numbers)
    if url_tag :
        url = "https://rabota.by" + url_tag.get('href')
    else:
        break


today = datetime.datetime.now()
today.strftime("%d_%B_%Y")
jobs_df = pd.DataFrame.from_dict(job_dict, orient='index', columns=['Job Title', 'Solary','Token', 'Location', 'Link', 'Creation'])
currency_df = get_currency_course(url_nbrb)
jobs_df = jobs_df.sort_values(by=['Solary'], ascending=False)

currency_df.to_csv('currency_course_' + today.strftime("%d_%B_%Y") + '.csv' )
jobs_df.to_csv('rabota_by_' + today.strftime("%d_%B_%Y") + '.csv' )
