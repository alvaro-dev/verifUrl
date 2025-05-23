from scraping_url import scrapping_vagas

jobs_python = scrapping_vagas('https://www.vagas.com.br/vagas-de-python')
jobs_javascript = scrapping_vagas('https://www.vagas.com.br/vagas-de-javascript')

print(len(jobs_python))
print(len(jobs_javascript))
