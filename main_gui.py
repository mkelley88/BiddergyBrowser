# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../biddergy.ui'
#
# Created: Thu Nov  5 14:33:24 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 510)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabMyAccount = QtGui.QTabWidget(self.centralwidget)
        self.tabMyAccount.setGeometry(QtCore.QRect(0, 60, 460, 410))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabMyAccount.sizePolicy().hasHeightForWidth())
        self.tabMyAccount.setSizePolicy(sizePolicy)
        self.tabMyAccount.setMinimumSize(QtCore.QSize(460, 410))
        self.tabMyAccount.setObjectName("tabMyAccount")
        self.tabSummary = QtGui.QWidget()
        self.tabSummary.setObjectName("tabSummary")
        self.gridLayout_4 = QtGui.QGridLayout(self.tabSummary)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblWatching = QtGui.QLabel(self.tabSummary)
        self.lblWatching.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblWatching.setObjectName("lblWatching")
        self.gridLayout.addWidget(self.lblWatching, 0, 0, 1, 1)
        self.lblBidding = QtGui.QLabel(self.tabSummary)
        self.lblBidding.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblBidding.setObjectName("lblBidding")
        self.gridLayout.addWidget(self.lblBidding, 1, 0, 1, 1)
        self.lblWon = QtGui.QLabel(self.tabSummary)
        self.lblWon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblWon.setObjectName("lblWon")
        self.gridLayout.addWidget(self.lblWon, 2, 0, 1, 1)
        self.lblNotWon = QtGui.QLabel(self.tabSummary)
        self.lblNotWon.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNotWon.setObjectName("lblNotWon")
        self.gridLayout.addWidget(self.lblNotWon, 3, 0, 1, 1)
        self.lblPurchases = QtGui.QLabel(self.tabSummary)
        self.lblPurchases.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPurchases.setObjectName("lblPurchases")
        self.gridLayout.addWidget(self.lblPurchases, 4, 0, 1, 1)
        self.lblInvoices = QtGui.QLabel(self.tabSummary)
        self.lblInvoices.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblInvoices.setObjectName("lblInvoices")
        self.gridLayout.addWidget(self.lblInvoices, 5, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnRefreshSummary = QtGui.QPushButton(self.tabSummary)
        self.btnRefreshSummary.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.btnRefreshSummary.setObjectName("btnRefreshSummary")
        self.horizontalLayout.addWidget(self.btnRefreshSummary)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.valWatching = QtGui.QLabel(self.tabSummary)
        self.valWatching.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.valWatching.setObjectName("valWatching")
        self.gridLayout_3.addWidget(self.valWatching, 0, 0, 1, 1)
        self.valBidding = QtGui.QLabel(self.tabSummary)
        self.valBidding.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.valBidding.setObjectName("valBidding")
        self.gridLayout_3.addWidget(self.valBidding, 1, 0, 1, 1)
        self.valWon = QtGui.QLabel(self.tabSummary)
        self.valWon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.valWon.setObjectName("valWon")
        self.gridLayout_3.addWidget(self.valWon, 2, 0, 1, 1)
        self.valNotWon = QtGui.QLabel(self.tabSummary)
        self.valNotWon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.valNotWon.setObjectName("valNotWon")
        self.gridLayout_3.addWidget(self.valNotWon, 3, 0, 1, 1)
        self.valPurchases = QtGui.QLabel(self.tabSummary)
        self.valPurchases.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.valPurchases.setObjectName("valPurchases")
        self.gridLayout_3.addWidget(self.valPurchases, 4, 0, 1, 1)
        self.valInvoices = QtGui.QLabel(self.tabSummary)
        self.valInvoices.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.valInvoices.setObjectName("valInvoices")
        self.gridLayout_3.addWidget(self.valInvoices, 5, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.tabMyAccount.addTab(self.tabSummary, "")
        self.tabWatching = QtGui.QWidget()
        self.tabWatching.setObjectName("tabWatching")
        self.tabMyAccount.addTab(self.tabWatching, "")
        self.tabBidding = QtGui.QWidget()
        self.tabBidding.setObjectName("tabBidding")
        self.tabMyAccount.addTab(self.tabBidding, "")
        self.tabWon = QtGui.QWidget()
        self.tabWon.setObjectName("tabWon")
        self.tabMyAccount.addTab(self.tabWon, "")
        self.tabNotWon = QtGui.QWidget()
        self.tabNotWon.setObjectName("tabNotWon")
        self.tabMyAccount.addTab(self.tabNotWon, "")
        self.tabPurchases = QtGui.QWidget()
        self.tabPurchases.setObjectName("tabPurchases")
        self.tabMyAccount.addTab(self.tabPurchases, "")
        self.imgBiddergyLogo = QtGui.QLabel(self.centralwidget)
        self.imgBiddergyLogo.setGeometry(QtCore.QRect(118, 9, 241, 51))
        self.imgBiddergyLogo.setText("")
        self.imgBiddergyLogo.setPixmap(QtGui.QPixmap("img/biddergy_new_logo.png"))
        self.imgBiddergyLogo.setScaledContents(True)
        self.imgBiddergyLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.imgBiddergyLogo.setObjectName("imgBiddergyLogo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionGeneral_Help = QtGui.QAction(MainWindow)
        self.actionGeneral_Help.setObjectName("actionGeneral_Help")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSummary_Refresh = QtGui.QAction(MainWindow)
        self.actionSummary_Refresh.setObjectName("actionSummary_Refresh")
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionGeneral_Help)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabMyAccount.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMyAccount.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSummary.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblWatching.setText(QtGui.QApplication.translate("MainWindow", "Watching:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblBidding.setText(QtGui.QApplication.translate("MainWindow", "Bidding:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblWon.setText(QtGui.QApplication.translate("MainWindow", "Won:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNotWon.setText(QtGui.QApplication.translate("MainWindow", "Not Won:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPurchases.setText(QtGui.QApplication.translate("MainWindow", "Purchases:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblInvoices.setText(QtGui.QApplication.translate("MainWindow", "Invoices:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefreshSummary.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.valWatching.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.valBidding.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.valWon.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.valNotWon.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.valPurchases.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.valInvoices.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMyAccount.setTabText(self.tabMyAccount.indexOf(self.tabSummary), QtGui.QApplication.translate("MainWindow", "Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMyAccount.setTabText(self.tabMyAccount.indexOf(self.tabWatching), QtGui.QApplication.translate("MainWindow", "Watching", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMyAccount.setTabText(self.tabMyAccount.indexOf(self.tabBidding), QtGui.QApplication.translate("MainWindow", "Bidding", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMyAccount.setTabText(self.tabMyAccount.indexOf(self.tabWon), QtGui.QApplication.translate("MainWindow", "Won", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMyAccount.setTabText(self.tabMyAccount.indexOf(self.tabNotWon), QtGui.QApplication.translate("MainWindow", "Not Won", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMyAccount.setTabText(self.tabMyAccount.indexOf(self.tabPurchases), QtGui.QApplication.translate("MainWindow", "Purchases", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGeneral_Help.setText(QtGui.QApplication.translate("MainWindow", "General Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSummary_Refresh.setText(QtGui.QApplication.translate("MainWindow", "Summary Refresh", None, QtGui.QApplication.UnicodeUTF8))
