from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        # Navigation bar
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        # Back button
        back_button = QAction("⮜", self)
        back_button.triggered.connect(self.browser.back)
        nav_bar.addAction(back_button)

        # Forward button
        forward_button = QAction("⮞", self)
        forward_button.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward_button)

        # Reload button
        reload_button = QAction("⟳", self)
        reload_button.triggered.connect(self.browser.reload)
        nav_bar.addAction(reload_button)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        nav_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url_bar)

    def load_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())

app = QApplication(sys.argv)
app.setApplicationName("Simple Browser")
window = BrowserWindow()
app.exec_()
