from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Визначник переможця')
my_win.move(100,100)
my_win.resize(400,200)

button = QPushButton(my_win)
button.setText('Згенерувати')
button.move(160,130)

text = QLabel(my_win)
text.setText('Натичніть, щоб дізнатися переможця')
text.move(110,10)

winner = QLabel(my_win)
winner.setText('?')
winner.move(195,70)

def show_winner():
    number = randint(1,999)
    winner.setText(str(number))
    text.setText('Переможець')
    text.move(165,10)

button.clicked.connect(show_winner)

my_win.show()
app.exec_()
