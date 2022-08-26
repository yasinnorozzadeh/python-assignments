import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("TicTacToe.ui", None)
        self.ui.show()
        self.game = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3],
                     [self.ui.btn_4, self.ui.btn_5, self.ui.btn_6],
                     [self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]]
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText("")
                self.game[i][j].setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(100, 100, 100)")
                self.game[i][j].clicked.connect(partial(self.Play, i, j))
        self.ui.btn_new.clicked.connect(self.new_game)
        self.ui.btn_abt.clicked.connect(self.about)
        self.ui.btn_newscore.clicked.connect(self.new_score)
        self.player = "X"
        self.player_score = 0
        self.player2_score = 0
    def check(self): 
        if ((self.game[0][0].text() == "X" and self.game[1][1].text() == "X" and self.game[2][2].text() == "X") or (self.game[0][2].text() == "X" and self.game[1][1].text() == "X" and self.game[2][0].text() == "X") or (self.game[0][0].text() == "X" and self.game[0][1].text() == "X" and self.game[0][2].text() == "X") or (self.game[1][0].text() == "X" and self.game[1][1].text() == "X" and self.game[1][2].text() == "X") or (self.game[2][0].text() == "X" and self.game[2][1].text() == "X" and self.game[2][2].text() == "X") or (self.game[0][0].text() == "X" and self.game[1][0].text() == "X" and self.game[2][0].text() == "X") or (self.game[0][1].text() == "X" and self.game[1][1].text() == "X" and self.game[2][1].text() == "X") or (self.game[0][2].text() == "X" and self.game[1][2].text() == "X" and self.game[2][2].text() == "X")):
            self.player_score += 1
            ms_box = QMessageBox()
            ms_box.setText("player 1 wins")
            self.ui.scorex.setText(str(self.player_score))
            ms_box.exec()
            self.new_game()
        elif ((self.game[0][0].text() == "O" and self.game[1][1].text() == "O" and self.game[2][2].text() == "O") or (self.game[0][2].text() == "O" and self.game[1][1].text() == "O" and self.game[2][0].text() == "O") or (self.game[0][0].text() == "O" and self.game[0][1].text() == "O" and self.game[0][2].text() == "O") or (self.game[1][0].text() == "O" and self.game[1][1].text() == "O" and self.game[1][2].text() == "O") or (self.game[2][0].text() == "O" and self.game[2][1].text() == "O" and self.game[2][2].text() == "O") or (self.game[0][0].text() == "O" and self.game[1][0].text() == "O" and self.game[2][0].text() == "O") or (self.game[0][1].text() == "O" and self.game[1][1].text() == "O" and self.game[2][1].text() == "O") or (self.game[0][2].text() == "O" and self.game[1][2].text() == "O" and self.game[2][2].text() == "O")):
            self.player2_score += 1
            ms_box = QMessageBox()
            ms_box.setText("player2 win")
            self.ui.scoreo.setText(str(self.player2_score))
            ms_box.exec()
            self.new_game()
        if self.game[0][0].text() != "" and self.game[0][1].text() != "" and self.game[0][2].text() != "" and self.game[1][0].text() != "" and self.game[1][1].text() != "" and self.game[1][2].text() != "" and self.game[2][0].text() != "" and self.game[2][1].text() != "" and self.game[2][2].text() != "":
            ms_box = QMessageBox()
            ms_box.setText("draw")
            ms_box.exec()
            self.new_game()
    def Play(self, i, j):
        if self.game[i][j].text() == "":
            if self.ui.btn_ptp.isChecked():
                if self.player == "X":
                    self.game[i][j].setText("X")
                    self.game[i][j].setStyleSheet("color:rgb(0, 255, 127); background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(198, 0, 3, 255), stop:0.443182 rgba(255, 0, 127, 255), stop:0.5 rgba(198, 0, 3, 255), stop:0.534091 rgba(255, 0, 127, 255), stop:1 rgba(198, 0, 3, 255))")
                    self.player = "O"
                else:
                    self.game[i][j].setText("O")
                    self.game[i][j].setStyleSheet("color:rgb(255, 255, 0); background-color:qlineargradient(spread:pad, x1:0, y1:0.0222727, x2:1, y2:1, stop:0 rgba(0, 10, 154, 255), stop:0.448864 rgba(101, 0, 159, 255), stop:0.482955 rgba(0, 10, 154, 255), stop:0.517045 rgba(101, 0, 159, 255), stop:1 rgba(0, 10, 154, 255))")
                    self.player = "X"
            if self.ui.btn_ptc.isChecked():
                if self.player == "X":
                    self.game[i][j].setText("X")
                    self.game[i][j].setStyleSheet("color:rgb(0, 255, 127); background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(198, 0, 3, 255), stop:0.443182 rgba(255, 0, 127, 255), stop:0.5 rgba(198, 0, 3, 255), stop:0.534091 rgba(255, 0, 127, 255), stop:1 rgba(198, 0, 3, 255))")
                    self.player = "O"
                if self.player == "O":
                    while True:
                        i = random.randint(0, 2)
                        j = random.randint(0, 2)
                        if self.game[i][j].text() == "":
                            self.game[i][j].setText("O")
                            self.game[i][j].setStyleSheet("color:rgb(255, 255, 0); background-color:qlineargradient(spread:pad, x1:0, y1:0.0222727, x2:1, y2:1, stop:0 rgba(0, 10, 154, 255), stop:0.448864 rgba(101, 0, 159, 255), stop:0.482955 rgba(0, 10, 154, 255), stop:0.517045 rgba(101, 0, 159, 255), stop:1 rgba(0, 10, 154, 255))")
                            self.player = "X"
                            break
        self.check()
    def about(self):
        ms_box = QMessageBox()
        ms_box.setText("Tic-Tac-Toe\n This Game using Pyside6\nprogram was developed by:\nnorozzadehyasin@gmail.com")
        ms_box.exec()
    def new_score(self):
        self.ui.scoreo.setText("0")
        self.ui.scorex.setText("0")
        self.player_score = 0
        self.player2_score = 0
    def new_game(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(100, 100, 100)")
                self.game[i][j].setText("")

app = QApplication([])
window = TicTacToe()
app.exec()
