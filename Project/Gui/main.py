import sys
from PyQt5 import QtWidgets
from UI.basketballStats import Ui_MainWindow
from Project.Run.championships_stats import Championships
from Project.Run.player_stats import PlayerStats
from selenium.common.exceptions import NoSuchElementException


# Main კლასი ასევე მემკვიდრეა Championships (championships_stats ფაილიდან)
# კლასის, რომელშიც გვაქვს ბაზასთან კავშირი და სტატისტიკის საჩვენებელი მეთოდი
class Main(QtWidgets.QMainWindow, Championships):
    def __init__(self):
        # super()  # selenium driveris sheqmna
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.get_statistics.clicked.connect(self.team_stats)
        self.ui.search_team.clicked.connect(self.count_mvp)
        self.ui.search_player.clicked.connect(self.player_stats)

    # ითვლის გუნდის mvp-ების რაოდენობას და გამოაქვს ინტერფეისზე
    def count_mvp(self):
        team = self.ui.team.toPlainText()
        if not team:
            self.ui.noteam_label.clear()
            return
        counter = 0
        for tpl in self.mvp_stats:
            if team in tpl:
                counter += 1
        st = f"{team}: {counter} MVP(s) from 1956 to 2021"
        self.ui.noteam_label.setText(st)

    # edzebs motamasheebis statistikas da gamoaqvs interfaceze
    def player_stats(self):
        player_name = self.ui.player.toPlainText()

        with PlayerStats() as bot:
            try:
                self.ui.noplayer_label.clear()
                bot.player_stats(player_name)
            except NoSuchElementException:
                self.ui.noplayer_label.setText('No player found')


app = QtWidgets.QApplication([])
window = Main()
window.show()
sys.exit(app.exec())
