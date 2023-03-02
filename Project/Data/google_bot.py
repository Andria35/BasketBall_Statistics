from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# google shi unda ipovos gadacemuli moatamashis
# sezonuri machvenebeli
class Googling(webdriver.Chrome):

    # object takes as parameter the selenium chrome driver path
    # with-as idan gamosvlis shemdeg browser-is daxurvis tanxmobas
    def __init__(self, driver_path="C:\\Users\\admin\Desktop\\Selenium\\chromedriver.exe", teardown=True):
        self.teardown = teardown # if true browseri daixureba yvelafris gaketebis mere
        # web driver lang = english
        lang_eng = webdriver.ChromeOptions()
        lang_eng.add_argument("--lang=en-ca")
        # web driver connect
        super().__init__(executable_path=driver_path, options=lang_eng)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # xsnis google is pirvel gverds
    def land_first_page(self, url='https://www.google.com/'):
        self.get(url)

    # ipovis motamasheze statistikas da shemdeg mas daabrunebs
    # string is formatshi
    def get_stats(self, basketball_player='kevin durant'):

        self.land_first_page() # pirvel gverdze gadasvla
        # get google search bar
        search_bar = self.find_element(By.NAME, 'q')
        search_bar.clear()
        # write to google search bar
        search_bar.send_keys(f'basketball-reference.com {basketball_player} stats')
        try:
            # get google search button
            search_button = self.find_element(By.CLASS_NAME, 'Tg7LZd')
            # click on search button
            search_button.click()
        except NoSuchElementException:
            # get google search button
            search_button = self.find_elements(By.NAME, 'btnK')
            # click on search button
            search_button[1].click()
        # basketball-reference.com ze gadasvla
        nba_web = self.find_element(By.CLASS_NAME, 'DKV0Md')
        nba_web.click()
        # statistikis cxrilis migeba
        stats_table = self.find_element(By.ID, 'div_per_game')

        return stats_table.text.strip()








# with Googling(teardown=True) as bot:
#     bot.land_first_page()
#     print(bot.get_stats(basketball_player='kevin durant'))