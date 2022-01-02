from PyQt5 import QtCore, QtGui, QtWidgets
from . import icons_rc
import random
import string
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setModal(True)
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 325)
        self.Dialog = Dialog
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(460, 325))
        Dialog.setMaximumSize(QtCore.QSize(460, 325))
        Dialog.setStyleSheet("QDialog {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.824045, x2:0.227, y2:0.83, stop:0.0924574 rgba(32, 32, 32, 255), stop:0.751825 rgba(44, 44, 44, 255));\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: transparent;\n"
"color: white;\n"
"background-color: rgb(50, 50, 50);\n"
"font-family: Arial;\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 371, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name.setMinimumSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.url = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.url.setMinimumSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.url.setFont(font)
        self.url.setObjectName("url")
        self.verticalLayout.addWidget(self.url)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username.setMinimumSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setMinimumSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.generate = QtWidgets.QPushButton(Dialog)
        self.generate.setGeometry(QtCore.QRect(400, 210, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        self.generate.setFont(font)
        self.generate.setStyleSheet("background-color: transparent;")
        self.generate.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/feather/edit-3.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.generate.setIcon(icon)
        self.generate.setIconSize(QtCore.QSize(30, 30))
        self.generate.setObjectName("generate")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.generate.clicked.connect(self.generatePassword)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Record"))
        self.name.setPlaceholderText(_translate("Dialog", "Name"))
        self.url.setPlaceholderText(_translate("Dialog", "URL"))
        self.username.setPlaceholderText(_translate("Dialog", "Username"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))

    #Load dialog box with a preset
    def load(self, name, data):
        self.name.setText(name)
        self.url.setText(data["url"])
        self.username.setText(data["username"])
        self.password.setText(data["password"])

    #Accept the dialog box
    def accept(self):
        name = self.name.text()
        url = self.url.text()
        username = self.username.text()
        password = self.password.text()
        if name and url and username and password:
            self.Dialog.accept()
        else: #Error message
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Missing Information")
            msg.setInformativeText('Please fill all fields')
            msg.setWindowTitle("Error")
            msg.exec_()

    #Generate random password
    def generatePassword(self):
        rand = "".join(random.choice(string.ascii_letters + string.digits) for i in range(16))
        self.password.setText(rand)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog() 
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())