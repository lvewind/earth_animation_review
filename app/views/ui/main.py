# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1707, 960)
        MainWindow.setMinimumSize(QSize(1707, 960))
        MainWindow.setMaximumSize(QSize(1707, 960))
        self.action_open_earth = QAction(MainWindow)
        self.action_open_earth.setObjectName(u"action_open_earth")
        self.action_setting = QAction(MainWindow)
        self.action_setting.setObjectName(u"action_setting")
        self.action_manual = QAction(MainWindow)
        self.action_manual.setObjectName(u"action_manual")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_tts_panel = QAction(MainWindow)
        self.action_tts_panel.setObjectName(u"action_tts_panel")
        self.action_open_nasa = QAction(MainWindow)
        self.action_open_nasa.setObjectName(u"action_open_nasa")
        self.action_download_nasa = QAction(MainWindow)
        self.action_download_nasa.setObjectName(u"action_download_nasa")
        self.action_update_voices = QAction(MainWindow)
        self.action_update_voices.setObjectName(u"action_update_voices")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 231, 471))
        self.tableWidget_collection = QTableWidget(self.groupBox_2)
        self.tableWidget_collection.setObjectName(u"tableWidget_collection")
        self.tableWidget_collection.setGeometry(QRect(0, 30, 231, 441))
        self.tableWidget_collection.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_collection.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_collection.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_collection.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_collection.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_collection.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_collection.verticalHeader().setVisible(False)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(240, 10, 391, 471))
        self.tableWidget_episode = QTableWidget(self.groupBox_3)
        self.tableWidget_episode.setObjectName(u"tableWidget_episode")
        self.tableWidget_episode.setGeometry(QRect(0, 30, 391, 441))
        self.tableWidget_episode.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_episode.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_episode.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_episode.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_episode.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_episode.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_episode.verticalHeader().setVisible(False)
        self.groupBox_subtitle_list = QGroupBox(self.centralwidget)
        self.groupBox_subtitle_list.setObjectName(u"groupBox_subtitle_list")
        self.groupBox_subtitle_list.setGeometry(QRect(640, 10, 901, 471))
        self.tableWidget_subtitle = QTableWidget(self.groupBox_subtitle_list)
        self.tableWidget_subtitle.setObjectName(u"tableWidget_subtitle")
        self.tableWidget_subtitle.setGeometry(QRect(0, 30, 901, 441))
        self.tableWidget_subtitle.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_subtitle.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_subtitle.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_subtitle.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_subtitle.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_subtitle.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_subtitle.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_subtitle.verticalHeader().setVisible(False)
        self.tableWidget_subtitle.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_subtitle.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_subtitle.verticalHeader().setHighlightSections(False)
        self.label_total_audio_time = QLabel(self.groupBox_subtitle_list)
        self.label_total_audio_time.setObjectName(u"label_total_audio_time")
        self.label_total_audio_time.setGeometry(QRect(690, 10, 71, 21))
        self.label_total_audio_time.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.groupBox_subtitle_list)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(630, 10, 51, 21))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_total_run_time = QLabel(self.groupBox_subtitle_list)
        self.label_total_run_time.setObjectName(u"label_total_run_time")
        self.label_total_run_time.setGeometry(QRect(830, 10, 71, 21))
        self.label_total_run_time.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.groupBox_subtitle_list)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(770, 10, 51, 21))
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.groupBox_media_list = QGroupBox(self.centralwidget)
        self.groupBox_media_list.setObjectName(u"groupBox_media_list")
        self.groupBox_media_list.setGeometry(QRect(640, 530, 621, 381))
        self.tableWidget_media = QTableWidget(self.groupBox_media_list)
        self.tableWidget_media.setObjectName(u"tableWidget_media")
        self.tableWidget_media.setGeometry(QRect(0, 20, 621, 361))
        self.tableWidget_media.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_media.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_media.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_media.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_media.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_media.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_media.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_media.verticalHeader().setVisible(False)
        self.tableWidget_media.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_media.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_media.verticalHeader().setHighlightSections(False)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 530, 621, 381))
        self.groupBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_img = QLabel(self.groupBox)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setGeometry(QRect(10, 20, 601, 351))
        self.label_img.setAlignment(Qt.AlignCenter)
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(1540, 10, 151, 471))
        self.tableWidget_subtitle_action = QTableWidget(self.groupBox_6)
        self.tableWidget_subtitle_action.setObjectName(u"tableWidget_subtitle_action")
        self.tableWidget_subtitle_action.setGeometry(QRect(0, 30, 151, 441))
        self.tableWidget_subtitle_action.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_subtitle_action.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_subtitle_action.horizontalHeader().setVisible(False)
        self.tableWidget_subtitle_action.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_subtitle_action.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_subtitle_action.verticalHeader().setDefaultSectionSize(23)
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(1260, 530, 431, 381))
        self.tableWidget_media_sub = QTableWidget(self.groupBox_5)
        self.tableWidget_media_sub.setObjectName(u"tableWidget_media_sub")
        self.tableWidget_media_sub.setGeometry(QRect(0, 20, 431, 361))
        self.tableWidget_media_sub.horizontalHeader().setVisible(False)
        self.tableWidget_media_sub.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_media_sub.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_media_sub.verticalHeader().setDefaultSectionSize(23)
        self.lineEdit_fly_to = QLineEdit(self.centralwidget)
        self.lineEdit_fly_to.setObjectName(u"lineEdit_fly_to")
        self.lineEdit_fly_to.setGeometry(QRect(110, 1000, 401, 31))
        self.pushButton_fly_to = QPushButton(self.centralwidget)
        self.pushButton_fly_to.setObjectName(u"pushButton_fly_to")
        self.pushButton_fly_to.setGeometry(QRect(10, 1000, 81, 31))
        self.pushButton_heading_0 = QPushButton(self.centralwidget)
        self.pushButton_heading_0.setObjectName(u"pushButton_heading_0")
        self.pushButton_heading_0.setGeometry(QRect(510, 490, 81, 31))
        self.pushButton_hide_earth_ui = QPushButton(self.centralwidget)
        self.pushButton_hide_earth_ui.setObjectName(u"pushButton_hide_earth_ui")
        self.pushButton_hide_earth_ui.setGeometry(QRect(210, 490, 81, 31))
        self.pushButton_show_earth_ui = QPushButton(self.centralwidget)
        self.pushButton_show_earth_ui.setObjectName(u"pushButton_show_earth_ui")
        self.pushButton_show_earth_ui.setGeometry(QRect(310, 490, 81, 31))
        self.pushButton_open_earth = QPushButton(self.centralwidget)
        self.pushButton_open_earth.setObjectName(u"pushButton_open_earth")
        self.pushButton_open_earth.setGeometry(QRect(10, 490, 81, 31))
        self.pushButton_set_3d_view = QPushButton(self.centralwidget)
        self.pushButton_set_3d_view.setObjectName(u"pushButton_set_3d_view")
        self.pushButton_set_3d_view.setGeometry(QRect(1000, 490, 81, 31))
        self.pushButton_set_2d_view = QPushButton(self.centralwidget)
        self.pushButton_set_2d_view.setObjectName(u"pushButton_set_2d_view")
        self.pushButton_set_2d_view.setGeometry(QRect(900, 490, 81, 31))
        self.pushButton_zoom_to_space = QPushButton(self.centralwidget)
        self.pushButton_zoom_to_space.setObjectName(u"pushButton_zoom_to_space")
        self.pushButton_zoom_to_space.setGeometry(QRect(800, 490, 81, 31))
        self.pushButton_street_view = QPushButton(self.centralwidget)
        self.pushButton_street_view.setObjectName(u"pushButton_street_view")
        self.pushButton_street_view.setGeometry(QRect(410, 490, 81, 31))
        self.pushButton_close_search = QPushButton(self.centralwidget)
        self.pushButton_close_search.setObjectName(u"pushButton_close_search")
        self.pushButton_close_search.setGeometry(QRect(700, 490, 81, 31))
        self.pushButton_clear_all_data = QPushButton(self.centralwidget)
        self.pushButton_clear_all_data.setObjectName(u"pushButton_clear_all_data")
        self.pushButton_clear_all_data.setGeometry(QRect(610, 490, 81, 31))
        self.pushButton_init_earth = QPushButton(self.centralwidget)
        self.pushButton_init_earth.setObjectName(u"pushButton_init_earth")
        self.pushButton_init_earth.setGeometry(QRect(110, 490, 81, 31))
        self.pushButton_fly_to_place_or_lla = QPushButton(self.centralwidget)
        self.pushButton_fly_to_place_or_lla.setObjectName(u"pushButton_fly_to_place_or_lla")
        self.pushButton_fly_to_place_or_lla.setGeometry(QRect(1100, 490, 81, 31))
        self.lineEdit_fly_to_place_or_lla = QLineEdit(self.centralwidget)
        self.lineEdit_fly_to_place_or_lla.setObjectName(u"lineEdit_fly_to_place_or_lla")
        self.lineEdit_fly_to_place_or_lla.setGeometry(QRect(1190, 490, 501, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1707, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.tableWidget_collection, self.tableWidget_episode)
        QWidget.setTabOrder(self.tableWidget_episode, self.tableWidget_subtitle)
        QWidget.setTabOrder(self.tableWidget_subtitle, self.tableWidget_media)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.action_open_earth)
        self.menu.addSeparator()
        self.menu.addAction(self.action_setting)
        self.menu_4.addAction(self.action_manual)
        self.menu_4.addAction(self.action_about)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_open_nasa)
        self.menu_4.addAction(self.action_download_nasa)
        self.menu_4.addSeparator()
        self.menu_5.addAction(self.action_tts_panel)
        self.menu_5.addAction(self.action_update_voices)
        self.menu_5.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EarthAnimation", None))
        self.action_open_earth.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00Earth", None))
        self.action_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.action_manual.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u624b\u518c", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_tts_panel.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u5408\u6210", None))
        self.action_open_nasa.setText(QCoreApplication.translate("MainWindow", u"open_nasa", None))
        self.action_download_nasa.setText(QCoreApplication.translate("MainWindow", u"download_nasa", None))
        self.action_update_voices.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u914d\u97f3\u5217\u8868", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5185\u5bb9\u7cfb\u5217", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u96c6", None))
        self.groupBox_subtitle_list.setTitle(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55", None))
        self.label_total_audio_time.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u65f6\u95f4:", None))
        self.label_total_run_time.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u65f6\u95f4:", None))
        self.groupBox_media_list.setTitle(QCoreApplication.translate("MainWindow", u"\u5a92\u4f53", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5a92\u4f53\u9884\u89c8", None))
        self.label_img.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u5b57\u5e55\u5c5e\u6027", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u5a92\u4f53\u5c5e\u6027", None))
        self.lineEdit_fly_to.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u53ef\u4ee5\u8f93\u5165 [\u5730\u70b9\u540d\u79f0]\uff0c\u6216\u8005[\u7ecf\u7eac\u5ea6\u5750\u6807]", None))
        self.pushButton_fly_to.setText(QCoreApplication.translate("MainWindow", u"\u98de\u5f80", None))
        self.pushButton_heading_0.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5317", None))
        self.pushButton_hide_earth_ui.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf UI", None))
        self.pushButton_show_earth_ui.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a UI", None))
        self.pushButton_open_earth.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00Earth", None))
        self.pushButton_set_3d_view.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.pushButton_set_2d_view.setText(QCoreApplication.translate("MainWindow", u"2D", None))
        self.pushButton_zoom_to_space.setText(QCoreApplication.translate("MainWindow", u"\u592a\u7a7a", None))
        self.pushButton_street_view.setText(QCoreApplication.translate("MainWindow", u"\u8857\u666f\u5207\u6362", None))
        self.pushButton_close_search.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u641c\u7d22", None))
        self.pushButton_clear_all_data.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6570\u636e", None))
        self.pushButton_init_earth.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316", None))
        self.pushButton_fly_to_place_or_lla.setText(QCoreApplication.translate("MainWindow", u"\u524d\u5f80", None))
        self.lineEdit_fly_to_place_or_lla.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5730\u70b9\u6216\u8005\u7ecf\u7eac\u5ea6\u53ef\u76f4\u63a5\u524d\u5f80", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u5408\u6210", None))
    # retranslateUi

