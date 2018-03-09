#!/usr/bin/env python3.4
from PySide.QtCore import QThread, Signal
from PySide import QtGui
from main_gui import Ui_MainWindow  # my UI from Qt4 Designer(pyside-uic)
from Scrapers import Biddergy       # My own class
import queue
import sys


class BiddergyWrapper(QThread):
    dataReceived = Signal(list)

    def __init__(self, q, loop_time=1.0/60):
        self.q = q
        self.timeout = loop_time
        super(BiddergyWrapper, self).__init__()

    def on_thread(self, function, *args, **kwargs):
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
        data = b.summary()
        print('Data received in background thread =', data)
        self.dataReceived.emit(data)

    def summary(self):
        self.on_thread(self._summary)

    def _login(self):
        returnvalue = b.login()
        print(returnvalue)

    def login(self):
        self.on_thread(self._login())


# Connect buttons
def connections():
    ui.btnRefreshSummary.released.connect(lambda: bw.summary())
    # ui.actionExit.activate(app.instance().quit)


# Refresh items in gui
def refresh_ui(summary):
    if summary:
        ui.valWatching.setText(summary['watched'])
        ui.valBidding.setText(summary['bidding'])
        ui.valWon.setText(summary['won'])
        ui.valNotWon.setText(summary['not_won'])
        ui.valPurchases.setText(summary['purchases'])
        ui.valInvoices.setText(summary['sales'])


def load_item(data):
    item = b.get_item_info(data)

    ui.val_itemTitle.setText(item['title'])
    ui.val_itemListingNumber.setText(item['listing_number'])
    ui.val_itemLotNumber.setText(item['lot_number'])
    ui.val_itemFormat.setText(item['format'])
    ui.val_itemBids.setText(item['bids'])
    ui.val_itemCurrentPrice.setText(item['price'])
    ui.val_itemHighBidder.setText(item['highbidder'])
    ui.val_itemLocation.setText(item['location'])
    ui.val_itemStart.setText(item['start'])
    ui.val_itemEnd.setText(item['end'])
    ui.txt_itemDescription.setHtml(item['description'])

    i = '<style>img { width: 100%; } </style>'
    for image in item['images']:
        i = i + '<p><img src="' + image + '"</img></p>'
    ui.web_itemImage.setHtml(i)


# Change status bar message
def status_msg(msg):
    ui.statusbar.showMessage(msg)


def sandbox():
    browse = 0
    try:
        browse = b.get_browse()
        x = 0
        for i in browse:
            ui.listWidget.addItems(x, i['title'])
            x += 1
    except:
        pass


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

    b = Biddergy(credentials[0], credentials[1])

    request_queue = queue.Queue()
    bw = BiddergyWrapper(request_queue)
    bw.dataReceived.connect(lambda data: refresh_ui(data))
    bw.start()
    connections()
    # b.login()

    # search = b.search_by_title('101987')
    # load_item(search)
    sandbox()

    app.exec_()
    bw.quit()
    # b.logout()
    sys.exit()
