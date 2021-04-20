import sys
import diceware
from PySide6 import QtCore, QtWidgets, QtGui

from saikorosrc.widgets import OptionsWidget, WrapAnywhereLabel
from saikorosrc.resources import load_css


CSS = load_css("main.css")


class DicewareWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(DicewareWidget, self).__init__()
        self.setWindowTitle("Saikoro: Easy way to generate diceware passphrases")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setMaximumWidth(800)
        self.setMaximumHeight(600)

        # Button to generate new passphrase
        self.generateButton = QtWidgets.QPushButton("Generate New Passphrase")
        self.generateButton.clicked.connect(self.generate_passphrase)
        self.generateButton.setFixedSize(300, 115)
        self.generateButton.setObjectName("generateButton")

        # Display passphrase
        self.options = diceware.handle_options(args=[])
        passphrase = diceware.get_passphrase(self.options)
        self.text = WrapAnywhereLabel(passphrase)
        self.text.setObjectName("passphrase")
        self.text.setFixedWidth(500)

        # Button to copy passphrase
        self.copyButton = QtWidgets.QPushButton("Copy passphrase")
        self.copyButton.clicked.connect(self.copy_passphrase)
        self.copyButton.setFixedSize(200, 45)
        self.copyButton.setObjectName("copyButton")

        # Layouting things
        formWidget = OptionsWidget(self)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(self.generateButton)
        vlayout.addWidget(self.text)
        vlayout.addWidget(self.copyButton)
        vlayout.setAlignment(QtCore.Qt.AlignCenter)
        vlayout.setAlignment(self.generateButton, QtCore.Qt.AlignHCenter)
        vlayout.setAlignment(self.copyButton, QtCore.Qt.AlignHCenter)
        mainWidget = QtWidgets.QWidget()
        mainWidget.setLayout(vlayout)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(mainWidget)
        layout.addWidget(formWidget)
        layout.setContentsMargins(0, 0, 0, 0)

        cwidget = QtWidgets.QWidget()
        cwidget.setLayout(layout)
        self.setCentralWidget(cwidget)
        self.setStyleSheet(CSS)

    def generate_passphrase(self):
        passphrase = diceware.get_passphrase(self.options)
        self.text.setText(passphrase)

    def copy_passphrase(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.text.toPlainText(), mode=clipboard.Clipboard)


def main():
    app = QtWidgets.QApplication([])
    widget = DicewareWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
