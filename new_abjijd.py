# -*- coding: utf-8 -*-

import letter_parser
import database
from PyQt4 import QtCore, QtGui

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(629, 568)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Answer_label = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Answer_label.setFont(font)
        self.Answer_label.setObjectName(_fromUtf8("Answer_label"))
        self.verticalLayout.addWidget(self.Answer_label)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_3.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.setFont(font)
        self.gridLayout_3.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_3.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.button_group_1 = QtGui.QButtonGroup(self.horizontalLayout_2)
        self.radioButton = QtGui.QRadioButton(self.tab)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.setChecked(True)
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.button_group_1.addButton(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.tab)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.button_group_1.addButton(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.tab)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.button_group_1.addButton(self.radioButton_3)
        self.Generate_btn = QtGui.QPushButton(self.tab)
        self.Generate_btn.setObjectName(_fromUtf8("Generate_btn"))
        self.Generate_btn.clicked.connect(self.calculate_value)
        self.horizontalLayout_2.addWidget(self.Generate_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tabWidget.setCurrentIndex(1)
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 451, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.button_group_2 = QtGui.QButtonGroup(self.horizontalLayoutWidget_3)
        self.radioButton_4 = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.toggled.connect(self.updater)
        self.button_group_2.addButton(self.radioButton_4)
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_5.toggled.connect(self.updater)
        self.button_group_2.addButton(self.radioButton_5)
        self.horizontalLayout_3.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.radioButton_6.toggled.connect(self.updater)
        self.button_group_2.addButton(self.radioButton_6)
        self.horizontalLayout_3.addWidget(self.radioButton_6)
        self.formLayoutWidget = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(390, 150, 160, 71))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.letterLabel = QtGui.QLabel(self.formLayoutWidget)
        self.letterLabel.setObjectName(_fromUtf8("letterLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.letterLabel)
        self.letterLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.letterLineEdit.setObjectName(_fromUtf8("letterLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.letterLineEdit)
        self.valueLabel = QtGui.QLabel(self.formLayoutWidget)
        self.valueLabel.setObjectName(_fromUtf8("valueLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.valueLabel)
        self.valueLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.valueLineEdit.setObjectName(_fromUtf8("valueLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.valueLineEdit)
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 370, 160, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.update_list)
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.save_value)
        self.verticalLayout_3.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        #self.tabWidget.setCurrentIndex(self.tab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)



        self.formLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 301, 421))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        
        self.scrollArea = QtGui.QScrollArea(self.formLayoutWidget_2)
#        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(QtCore.QRect(10,10, 200,400 ))
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(100, 100, 300, 300))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutScroll = QtGui.QFormLayout(self.scrollAreaWidgetContents)

        self.retranslateUi(MainWindow)


        self.list_alpha('one')
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        MainWindow.setTabOrder(self.plainTextEdit, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.Generate_btn)
        MainWindow.setTabOrder(self.Generate_btn, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.radioButton_5)
        MainWindow.setTabOrder(self.radioButton_5, self.radioButton_6)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Abjad", None))
        self.Answer_label.setText(_translate("MainWindow", "Value ", None))
        self.radioButton.setText(_translate("MainWindow", "Preset1 ", None))
        self.radioButton_2.setText(_translate("MainWindow", "Preset 2", None))
        self.radioButton_3.setText(_translate("MainWindow", "Preset 3", None))
        self.Generate_btn.setText(_translate("MainWindow", "Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Calculator", None))
        self.radioButton_4.setText(_translate("MainWindow", "Preset 1", None))
        self.radioButton_5.setText(_translate("MainWindow", "Preset 2", None))
        self.radioButton_6.setText(_translate("MainWindow", "Preset 3", None))
        self.letterLabel.setText(_translate("MainWindow", "letter", None))
        self.valueLabel.setText(_translate("MainWindow", "value", None))
        self.pushButton_2.setText(_translate("MainWindow", "Add Value ", None))
        self.pushButton.setText(_translate("MainWindow", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings", None))


    def list_alpha(self,label):
        global obj_list
        db,cu = database.connect_db()
        
        self.letter_list = database.fetch_data(label,cu)
        font = QtGui.QFont()
        font.setPointSize(20)

        obj_list = []
        for letter,value in self.letter_list:
            valEdit = letter+"_Edit"
            value = str(value)
            self.letter = QtGui.QLabel(self.formLayoutWidget_2)
            self.letter.setObjectName(_fromUtf8(letter))
            self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.letter)
            self.letter.setText(_translate("MainWindow", letter, None))
            self.letter.setFont(font)
            self.formLayout.addWidget(self.letter)
            self.valEdit = QtGui.QLineEdit(self.formLayoutWidget_2)
            self.valEdit.setObjectName(_fromUtf8(valEdit))
            self.valEdit.setText(_translate("MainWindow", value, None))       
            self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.valEdit)
            self.verticalLayoutScroll.addWidget(self.letter)
            self.verticalLayoutScroll.addWidget(self.valEdit)
            objs = self.letter,self.valEdit
            obj_list.append(objs)
        self.scrollArea.setWidgetResizable(True)
        self.show()
        return 

    def save_value(self):
        label = self.label_id(self.button_group_2.checkedId())
        if label :
            updated_list = []
            for letter_obj,value_obj in obj_list:
                letter = letter_obj.text().toUtf8()
                value = value_obj.text()
                objs = letter,value
                updated_list.append(objs)
            database.update_data(updated_list,label)
        
            
    def calculate_value(self):
        label = self.label_id(self.button_group_1.checkedId())
        self.value = unicode(self.plainTextEdit.toPlainText(),'utf-8')
        answer,excluded = letter_parser.calculate_value(unicode(self.plainTextEdit.toPlainText()),label)
        self.Answer_label.setText(_translate("MainWindow", str(answer), None))
        excluded = ', '.join(set(excluded))
        self.lineEdit.setText(_translate("MainWindow", excluded, None))       
        
    def update_list(self):
        db,cu = database.connect_db()
        input_letter = self.letterLineEdit.text().toUtf8()
        input_letter = str(input_letter).strip()
        input_value =  self.valueLineEdit.text()
        label = 'one'
        try:
            input_value = int(input_value)
            database.insert_data(input_letter,input_value,label,cu,db)
            self.letterLineEdit.clear()
            self.valueLineEdit.clear()
            try:
                for i in range(self.verticalLayoutScroll.count()): self.verticalLayoutScroll.itemAt(i).widget().close()
            except:
                pass
            self.list_alpha(label)
        except :
            QtGui.QMessageBox.warning(self, "Cannot store value",
                "Please check values",
                QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton,
                QtGui.QMessageBox.NoButton)
            return 
        
    def label_id(self,labelid):
        if labelid == -2:
            label = "one"
        elif labelid == -3:
            label = "two"
        elif labelid == -4:
            label = "three"
        else:
            QtGui.QMessageBox.warning(self, "Cannot store value",
                "Please select one preset ",
                QtGui.QMessageBox.Cancel, QtGui.QMessageBox.NoButton,
                QtGui.QMessageBox.NoButton)
            label = False
        return label

    def updater(self):
        label = self.label_id(self.button_group_2.checkedId())
        # try:
        #     for i in range(self.verticalLayoutScroll.count()): self.verticalLayoutScroll.itemAt(i).widget().close()
        # except:
        #     pass
        # self.list_alpha(label)
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

