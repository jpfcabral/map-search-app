
import folium
import sys
import io
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QToolButton
from GeoSearch import GeoSearcher

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()


    def initUi(self):
        self.main_ui = uic.loadUi('interface-v0.2.ui')
        self.settings_ui = uic.loadUi('settings.ui')

        self.main_ui.searchButton.clicked.connect(self.search_button_clicked)
        self.main_ui.actionSettings.triggered.connect(self.open_settings)

        self.load_map(-5.888947323651743, -35.21097641464734)
        self.geocoord = GeoSearcher()

        self.main_ui.show()


    def search_button_clicked(self):
        address = self.main_ui.addressTextEdit.toPlainText()
        print(address)
        lat, lon = self.geocoord.find(address=address)
        print(lat, lon)
        self.load_map(lat, lon)

    
    def load_map(self, lat, lon, zoom=15):
        m = folium.Map(tiles='Stamen Terrain', zoom_start=zoom, location=(lat, lon))
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.main_ui.mapWidget.setHtml(data.getvalue().decode())

    
    def open_settings(self):
        self.settings_ui.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()