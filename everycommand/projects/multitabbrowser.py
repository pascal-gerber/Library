# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

# main window
class MainWindow(QMainWindow):

	# constructor
    def __init__(window, *fuckme, **kiddingme):
        super(MainWindow, window).__init__(*fuckme, **kiddingme)
        window.tabs = QTabWidget()
        
		# making document mode true
        window.tabs.setDocumentMode(True)
        
		# adding action when double clicked
        window.tabs.tabBarDoubleClicked.connect(window.tab_open_doubleclick)

		# adding action when tab is changed
        window.tabs.currentChanged.connect(window.current_tab_changed) 
        
		# making tabs closeable
        window.tabs.setTabsClosable(True)

		# adding action when tab close is requested
        window.tabs.tabCloseRequested.connect(window.close_current_tab)

		# making tabs as central widget
        window.setCentralWidget(window.tabs)

		# creating a status bar
        window.status = QStatusBar()
        window.setStatusBar(window.status)
        navtb = QToolBar("Navigation")
        window.addToolBar(navtb)

		# creating back action
        back_btn = QAction("Back", window)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: window.tabs.currentWidget().back())

		# adding this to the navigation tool bar
        navtb.addAction(back_btn)

		# similarly adding next button
        next_btn = QAction("Forward", window)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: window.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

		# similarly adding reload button
        reload_btn = QAction("Reload", window)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: window.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

		
        home_btn = QAction("Home", window)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(window.navigate_home)
        navtb.addAction(home_btn)

        Proxy_Btn = QAction("Proxy", window)
        Proxy_Btn.triggered.connect(window.proxy)
        navtb.addAction(Proxy_Btn)
		# adding a separator
        navtb.addSeparator()

		# creating a line edit widget for URL
        window.urlbar = QLineEdit()
		# adding action to line edit when return key is pressed
        window.urlbar.returnPressed.connect(window.navigate_to_url)
        
		# adding line edit to tool bar
        navtb.addWidget(window.urlbar)
		# similarly adding stop action
        stop_btn = QAction("Stop", window)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: window.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

		# creating first tab
        window.add_new_tab(QUrl('https://duckduckgo.com/'), 'Homepage')

		# showing all the components
        window.show()

		# setting window title
        window.setWindowTitle("pyrome")

	# method for adding new tab
    def add_new_tab(window, qurl = None, label ="Blank"):
        qurl = QUrl('https://duckduckgo.com/')
		# creating a QWebEngineView object
        browser = QWebEngineView()
		# setting url to browser
        browser.setUrl(qurl)

		# setting tab index
        i = window.tabs.addTab(browser, label)
        window.tabs.setCurrentIndex(i)
		# adding action to the browser when url is changed
		# update the url
        browser.urlChanged.connect(lambda qurl, browser = browser:
        window.update_urlbar(qurl, browser))
		# adding action to the browser when loading is finished
		# set the tab title
        browser.loadFinished.connect(lambda _, i = i, browser = browser:
        window.tabs.setTabText(i, browser.page().title()))

    
	# when double clicked is pressed on tabs
    def tab_open_doubleclick(window, i):
        
		# checking index i.e
		# No tab under the click
        if i == -1:
			# creating a new tab
            window.add_new_tab()

	# when tab is changed
    def current_tab_changed(window, i):
        
		# get the curl
        qurl = window.tabs.currentWidget().url()
        
		# update the url
        window.update_urlbar(qurl, window.tabs.currentWidget())
        
		# update the title
        window.update_title(window.tabs.currentWidget())
        

	# when tab is closed
    def close_current_tab(window, i):

		# if there is only one tab
        if window.tabs.count() < 2:
            return

		# else remove the tab
        window.tabs.removeTab(i)

	# method for updating the title
    def update_title(window, browser):
        
		# if signal is not from the current tab
        if browser != window.tabs.currentWidget():
            return

		# get the page title
        title = window.tabs.currentWidget().page().title()

		# set the window title
        window.setWindowTitle("% s - Geek PyQt5" % title)

	# action to go to home
    def navigate_home(window):
        window.tabs.currentWidget().setUrl(QUrl("https://duckduckgo.com/"))

    def proxy(window):
        window.tabs.currentWidget().setUrl(QUrl('https://proxyscrape.com/web-proxy'))

	# method for navigate to url
    def navigate_to_url(window):
		# get the line edit text
		# convert it to QUrl object
        
        q = QUrl(window.urlbar.text())
		# if scheme is blank
        if q.scheme() == "":
            q.setScheme("http")

		# set the url
        window.tabs.currentWidget().setUrl(q)

        

	# method to update the url
    def update_urlbar(window, q, browser = None):
		# If this signal is not from the current tab, ignore
        if browser != window.tabs.currentWidget():
            return

		# set text to the url bar	
        window.urlbar.setText(q.toString())
            
		# set cursor position
        window.urlbar.setCursorPosition(0)



# creating a PyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("Geek PyQt5")

# creating MainWindow object
window = MainWindow()

# loop the browser window
app.exec_()

#note, most of this structure i didn't make myself
#most of it i gathered and formed it into my own liking.





