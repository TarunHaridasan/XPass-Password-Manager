from PyQt5 import QtCore, QtGui, QtWidgets
from . import icons_rc
from . import home
import sys
from scripts import login

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 338)
        Form.setMinimumSize(QtCore.QSize(648, 338))
        Form.setMaximumSize(QtCore.QSize(648, 338))
        self.Form = Form
        Form.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none;\n"
"font-family: Bahnschrift Condensed;")
        self.Titlebar = QtWidgets.QFrame(Form)
        self.Titlebar.setGeometry(QtCore.QRect(0, 0, 1001, 71))
        self.Titlebar.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.Titlebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Titlebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Titlebar.setObjectName("Titlebar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Titlebar)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, -4, 211, 79))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Title = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Title.setContentsMargins(0, 0, 0, 0)
        self.Title.setSpacing(11)
        self.Title.setObjectName("Title")
        self.Logo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/feather/shield.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QtCore.QSize(60, 60))
        self.Logo.setObjectName("Logo")
        self.Title.addWidget(self.Logo)
        self.Name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(47)
        font.setBold(False)
        font.setWeight(50)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Title.addWidget(self.Name)
        self.Main = QtWidgets.QFrame(Form)
        self.Main.setGeometry(QtCore.QRect(0, 70, 1001, 531))
        self.Main.setStyleSheet("#Main {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.824045, x2:0.227, y2:0.83, stop:0.0924574 rgba(32, 32, 32, 255), stop:0.751825 rgba(44, 44, 44, 255));\n"
"}")
        self.Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main.setObjectName("Main")
        self.Version = QtWidgets.QLabel(self.Main)
        self.Version.setGeometry(QtCore.QRect(560, 240, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.Version.setFont(font)
        self.Version.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Version.setObjectName("Version")
        self.formLayoutWidget = QtWidgets.QWidget(self.Main)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 40, 471, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Username = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Username.sizePolicy().hasHeightForWidth())
        self.Username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.Username.setFont(font)
        self.Username.setStyleSheet("color: black;")
        self.Username.setObjectName("Username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Username)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.Password.setFont(font)
        self.Password.setStyleSheet("color: black;")
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Password)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Main)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 170, 401, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Register = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.Register.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/feather/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Register.setIcon(icon1)
        self.Register.setIconSize(QtCore.QSize(35, 35))
        self.Register.setObjectName("Register")
        self.horizontalLayout.addWidget(self.Register)
        self.Login = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.Login.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/feather/log-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Login.setIcon(icon2)
        self.Login.setIconSize(QtCore.QSize(35, 35))
        self.Login.setObjectName("Login")
        self.horizontalLayout.addWidget(self.Login)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Login.clicked.connect(self.login)
        self.Register.clicked.connect(self.register)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "XPass"))
        self.Name.setText(_translate("Form", "XPass"))
        self.Version.setText(_translate("Form", "Version: 1.0.0"))
        self.label.setText(_translate("Form", "Username: "))
        self.label_2.setText(_translate("Form", "Password: "))
        self.Register.setText(_translate("Form", "Register"))
        self.Login.setText(_translate("Form", " Login"))

    #Extract text from input fields
    def extract(self):
        username = self.Username.text()
        password = self.Password.text()
        return username, password

    #Login button is pressed
    def login(self):
        username, password = self.extract()
        if username == "" or password == "":
            self.error("Some fields are left blank")
            return False
        if not login.userExists(username):
            self.error("User does not exist")
            return False
        key = login.verifyLogin(username, password)
        if not key:
            self.error("Invalid Credentials")
            return False
        print(key + "\n" + username + "\n" + password)
        self.Form.close() #Close login
        self.MainWindow = QtWidgets.QMainWindow() #Open main window
        self.ui = home.Ui_MainWindow()
        self.ui.setup(self.MainWindow, key, username, password)
        self.MainWindow.show()
        self.ui.refreshList()
    
    #Gegister button is pressed
    def register(self):
        username, password = self.extract()
        if username == "" or password == "":
            self.error("Some fields are left blank")
            return False
        if login.userExists(username):
            self.error("User already exists")
            return False
        login.addUser(username, password)    

    #Make error message
    def error(self, message):
        window = QtWidgets.QMessageBox()
        window.setIcon(QtWidgets.QMessageBox.Critical)
        window.setText(message)
        window.setWindowTitle("Error")
        window.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())