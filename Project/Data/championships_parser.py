from bs4 import BeautifulSoup
import requests

# mocemuli saitidan parsings uketebs gundebis
# chempionad gaxdomis statistikas wlebis mixedvit
def championships():
    html_txt = requests.get('https://www.basketball-reference.com/playoffs/').text
    soup = BeautifulSoup(html_txt, 'lxml')
    years = soup.find_all('th', {'data-stat': 'year_id'})
    years = [year.text.strip() for year in years if year.text.strip().isdigit()]
    teams = soup.find_all('td', {'data-stat': 'champion'})
    teams = [team.text.strip() for team in teams]

    zipped = list(zip(years, teams))
    return zipped

