import sys
import psycopg2

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class LoadData(object):
    @staticmethod
    def ld_labels(cursor, tableWidget):
        tableWidget.setColumnCount(5)
        row_list = LoadData.load_name_tables(cursor)
        if len(row_list) != 0:
            tableWidget.setHorizontalHeaderLabels([row_list[0], row_list[1], row_list[2], row_list[3], row_list[4]])

    @staticmethod
    def ld_data_main_window(cursor, tableWidget):
        sql = "SELECT * FROM table_gui"
        cursor.execute(sql)  # type: ignore
        result = cursor.fetchall()  # type: ignore
        row_count = 0
        for row in result:
            lst = []
            for elem in row:
                lst.append(elem)
            tableWidget.insertRow(row_count)
            for i in range(0, 5):
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, lst[i])  # type: ignore
                tableWidget.setItem(row_count, i, item)
                tableWidget.resizeColumnToContents(i)
            tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(lst[2])))  # type: ignore
            tableWidget.resizeColumnToContents(2)
        tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)  # type: ignore

    @staticmethod
    def show_message(message, type):
        msg = QMessageBox()
        msg.setWindowTitle("Помощь")
        msg.setText(message)  # type: ignore
        msg.setIcon(type)  # type: ignore
        msg.exec_()

    @staticmethod
    def load_name_tables(cursor):
        sql1 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'table_gui'"
        cursor.execute(sql1)  # type: ignore
        result_header = cursor.fetchall()  # type: ignore
        row_list = []
        for row in result_header:
            for elem in row:
                row_list.append(elem)
        return row_list

    @staticmethod
    def ld_data_add_window(cursor, tableWidget, column_name):
        sql = "SELECT " + column_name + " FROM table_gui"
        cursor.execute(sql)  # type: ignore
        result = cursor.fetchall()  # type: ignore
        row_count = 0
        for row in result:
            lst = []
            for elem in row:
                lst.append(elem)
            tableWidget.insertRow(row_count)
            if column_name == 'дата_рождения':
                tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(lst[0])))  # type: ignore
            else:
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, lst[0])  # type: ignore
                tableWidget.setItem(row_count, 0, item)
            tableWidget.resizeColumnToContents(0)
        if column_name == 'id':
            tableWidget.sortItems(0, QtCore.Qt.AscendingOrder)  # type: ignore


class Ui_MainWindow(object):
    def __init__(self):
        self.connection = psycopg2.connect(dbname='lab3_gui', user='postgres', password='11', host='localhost')
        self.cursor = self.connection.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1024, 720))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)  # type: ignore
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)  # type: ignore
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)  # type: ignore
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)  # type: ignore
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.execute_query)
        self.gridLayout_3.addWidget(self.pushButton, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)  # type: ignore
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget_2, 2, 0, 1, 6)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_connection = QtWidgets.QAction(MainWindow)
        self.actionOpen_connection.setObjectName("actionOpen_connection")
        self.actionOpen_connection.triggered.connect(self.open_connect)
        self.actionClose_connection = QtWidgets.QAction(MainWindow)
        self.actionClose_connection.setObjectName("actionClose_connection")
        self.actionClose_connection.triggered.connect(self.close_connect)
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_2.triggered.connect(self.exit_click)
        self.menuMenu.addAction(self.actionOpen_connection)
        self.menuMenu.addAction(self.actionClose_connection)
        self.menuMenu.addAction(self.actionExit_2)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit_click(self):
        self.close_connect()
        quit()

    def open_connect(self):
        self.connection = psycopg2.connect(dbname='lab3_gui', user='postgres', password='11', host='localhost')
        self.cursor = self.connection.cursor()
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        LoadData.ld_labels(self.cursor, self.tableWidget)
        LoadData.ld_data_main_window(self.cursor, self.tableWidget)
        self.comboBox.addItems(LoadData.load_name_tables(self.cursor))

    def close_connect(self):
        self.connection.close()  # type: ignore
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.clear()
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.comboBox.clear()

    def execute_query(self):
        if self.comboBox.currentText() != "":
            self.tableWidget_2.clear()
            self.tableWidget_2.setColumnCount(1)
            self.tableWidget_2.setRowCount(0)
            LoadData.ld_data_add_window(self.cursor, self.tableWidget_2, self.comboBox.currentText())
        else:
            msg_text = 'Неизвестный запрос'
            LoadData.show_message(msg_text, QMessageBox.Warning)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр базы данных"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Страница 1"))
        self.pushButton.setText(_translate("MainWindow", "Выполнить запрос"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Страница 2"))
        self.menuMenu.setTitle(_translate("MainWindow", "Меню подключения"))
        self.actionOpen_connection.setText(_translate("MainWindow", "Открыть соединение"))
        self.actionClose_connection.setText(_translate("MainWindow", "Закрыть соединение"))
        self.actionExit_2.setText(_translate("MainWindow", "Выход"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
