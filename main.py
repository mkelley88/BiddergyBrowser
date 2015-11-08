#!/usr/bin/env python3
from PySide import QtGui, QtCore
from PySide.QtCore import QThread, QObject, Signal, Slot
from main_gui import Ui_MainWindow  # my UI from Qt4 Designer(pyside-uic)
from Scrapers import Biddergy       # My own class
import sys
import time
import queue


class BiddergyWrapper(QThread):
    def __init__(self, q, loop_time=1.0/60):
        self.q = q
        self.timeout = loop_time
        super(BiddergyWrapper, self).__init__()

    def onThread(self, function, *args, **kwargs):
        self.q.put((function, args, kwargs))

    def run(self):
        while True:
            try:
                function, args, kwargs = self.q.get(timeout=self.timeout)
                function(*args, **kwargs)
            except queue.Empty:
                self.idle()

    def idle(self):
        pass

    def _summary(self):
        b.summary()

    def summary(self):
        self.onThread(self._summary)

    def _login(self):
        b.login()

    def login(self):
        self.onThread(self._login())


# Connect buttons
def connections():
    ui.btnRefreshSummary.clicked.connect(lambda: bw.summary())


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

    # Login, download summary, then refresh the UI.
    b = Biddergy(credentials[0], credentials[1])
    request_queue = queue.Queue()
    bw = BiddergyWrapper(request_queue)
    bw.start()

    # Run QApplication
    app.exec_()
    # Begin "Graceful stop?"
    bw.quit()
    b.logout()
    sys.exit()
