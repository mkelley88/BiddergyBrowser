
#!/usr/bin/env python3
from PySide import QtGui
# from PySide.QtCore import QThread, QObject, Signal, Slot
from main_gui import Ui_MainWindow  # my UI from Qt4 Designer(pyside-uic)
from Scrapers import Biddergy       # My own class
import sys
import threading


# Connect buttons
def connections():
    ui.btnRefreshSummary.clicked.connect(lambda: b.summary())


# Refresh items in gui
def refresh_ui():
    if summary_data != []:
        ui.valWatching.setText(summary_data[0])
        ui.valBidding.setText(summary_data[1])
        ui.valWon.setText(summary_data[2])
        ui.valNotWon.setText(summary_data[3])
        ui.valPurchases.setText(summary_data[4])
        ui.valInvoices.setText(summary_data[5])


# Change status bar message
def status_msg(msg):
    ui.statusbar.showMessage(msg)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    connections()
    # Load credentials from file.
    with open('login.txt') as f:
        credentials = f.readline().strip().split(':')
    f.closed

    # Login, download summary, then refresh the UI.
    b = Biddergy()
    b.login(credentials[0],credentials[1])
    summary_data = b.summary()
    b.logout()


    refresh_ui()
    sys.exit(app.exec_())
