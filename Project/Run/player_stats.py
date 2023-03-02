import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Project.Data.google_bot import Googling
from io import StringIO
import threading


# tito motamashis statistikis klasi
# klasi miigebs informacias saitidan daamushavebs
# motamashis monacemebs da grafikze gamoitans
class PlayerStats(Googling):

    def __init__(self):
        Googling.__init__(self)  # selenium driveris sheqmna


    def write_to_file(self, stats):

        with open('stats', 'w') as f:
            f.writelines(stats)


    def player_stats(self, basketball_player='Kevin Durant'):
        # statistikis migeba da monacemebis damushaveba
        stats = self.get_stats(basketball_player=basketball_player).split('\n')
        # grafikistvis arasasurveli informaciis gafiltvra
        for stat in stats:
            if 'Did Not Play' in stat:
                stats.remove(stat)
        stats = '\n'.join(stats)
        # file shi chawera threadebit
        th = threading.Thread(target=self.write_to_file, args=(f'Name:{basketball_player}\n{stats}',)) # threadebis gamoyeneba
        th.start()
        th.join()


        # panda dataframe ad formireba statistikis
        stats = StringIO(stats)
        df = pd.read_csv(stats, sep=' ')
        df.set_index('Season', inplace=True)
        df = df[:'Career']
        df = df[:-1]
        # print(df)
        # dataframe is damushaveba da nawilebad dayofa
        df_games = df[['G', 'GS', 'MP']]  # dataframe = Games, games played, minutes played (tamashebis raodenoba)
        df_fg = df[['FGA', 'FG', 'FG%']]  # dataframe = field goals made, field goals attempted, field goals% (tamasheb)
        df_3p = df[['3PA', '3P', '3P%']]  # dataframe = 3 pointers attempted, 3p made, 3p% (3qulianebi)
        df_2p = df[['2PA', '2P', '2P%']]  # dataframe = 2 pointers attempted, 2p made, 2p% (2 qulianebi)
        df_ft = df[['FTA', 'FT', 'FT%']]  # dataframe = free throws attempted, ft made , ft% (sajarimoebi)
        df_defence = df[['TRB', 'STL', 'BLK']]  # dataframe = rebounds, steals, blocks (dacva)
        df_assists = df[['AST', 'TOV']]  # dataframe = assist, turnover (pasebi, shecdomebi)
        df_pts = df[['PTS']] # dataframe = points (qulebi)
        df_seasons = pd.DataFrame(df['Tm'].groupby(df['Tm']).count())  # ramdeni sezoni itamasha motamashem gundshi

        # grafikis ageba
        df_pts.plot(kind='bar')
        plt.title('ქულები')
        plt.show()
        df_assists.plot(kind='bar', stacked=True)
        plt.title('გადაცემები')
        plt.show()
        df_defence.plot(kind='barh', stacked=True)
        plt.title('დაცვა')
        plt.show()
        df_ft.plot(kind='bar')
        plt.title('საჯარიმოები')
        plt.show()
        df_2p.plot(kind='pie', subplots=True)
        plt.title('2 ქულიანი სროლები')
        plt.show()
        df_3p.plot(kind='pie', subplots=True)
        plt.title('3 ქულიანი სროლები')
        plt.show()
        df_fg.plot(kind='line')
        plt.title('ნასროლი ბურთების შეფარდება')
        plt.show()
        df_games.plot(kind='area')
        plt.title('თამაშების რაოდენობა')
        plt.show()
        df_seasons.plot(kind='bar')
        plt.title('გატარებული სეზონი რაოდენობა ცალკეულ გუნდში')
        plt.show()
        # print(df_seasons)
        # self.quit()  # selenium browseris daxurva



# with PlayerStats() as bot:
#     bot.player_stats()

