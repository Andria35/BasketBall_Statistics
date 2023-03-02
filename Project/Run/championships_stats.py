import matplotlib.pyplot as plt
import pandas as pd
from sqlite3 import Connection
from Project.Data.mvp_stats_parser import mvp


# gundebis statistikis klasi
# daamushavebs informacias gundebze da gamoitans
# grafikis saxit
class Championships:
    def __init__(self):
        # ბაზასთან კავშირი და წაკითხული მონაცემებით dataframe-ის შექმნა
        self.connect = Connection(r'D:\MyPythonProjects\Project\Data\base.db3')
        self.df = pd.read_sql('SELECT * FROM Championships', self.connect)

        # mvp_stats_parser ფაილში "გაპარსული" მონაცემების ლისტი,
        # გვაქვს ინფორმაცია თითოეულ წელს რომელმა გუნდმა აიღო mvp
        self.mvp_stats = mvp()


    # გამოაქვს 2 სტატისტიკა:
    # თითოეულ წელს mvp-ს მომპოვებელი გუნდი
    # თითოეულ წელს playoff-ში გამარჯვებული გუნდი
    def team_stats(self):
        modified_list = []
        for tpl in self.mvp_stats:
            modified_list.append((tpl[0][-2:], tpl[1]))
        print(modified_list)
        plt.scatter(*zip(*modified_list))
        plt.title('MVP')
        plt.xlabel('Year')
        plt.ylabel('Team')
        plt.show()

        df_teams_stats = self.df['Team'].groupby(self.df['Team']).count()
        ndf1 = pd.DataFrame(df_teams_stats)
        ndf1.plot(kind="bar")
        plt.title('Playoffs')
        plt.xlabel('Team')
        plt.ylabel('Wins')
        plt.show()




