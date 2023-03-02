from bs4 import BeautifulSoup
import requests


# აგზავნის requests და იღებს ცხრილში არსებული მონაცემებიდან გუნდებსა და წლებს
# აბრუნებს ასეთი ტაპლების ლისტს: ('წელი', 'გუნდი')
def mvp():
    try:
        html_text = requests.get('http://www.espn.com/nba/history/awards/_/id/33').text
        soup = BeautifulSoup(html_text, 'lxml')
        rows = soup.find_all('tr', class_='oddrow')
        tds_in_row = [row.find_all('td') for row in rows]
        years = [[td.text for td in row[0]][0] for row in tds_in_row]
        teams = [[td.text for td in row[3]][0] for row in tds_in_row]
        zipped = list(zip(years, teams))
        print(zipped)
        return zipped
    except:
        return 'Something went wrong, we could not fetch the data'
