from PyQt5 import QtWidgets, uic
import sys
import os

app = QtWidgets.QApplication([])
settings_ui = uic.loadUi('settings.ui')
settings_ui.show()
app.exec()