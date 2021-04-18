import sys
import diceware
from PySide6 import QtCore, QtWidgets, QtGui


class DicewareWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diceware UI: Easy way to generate passphrases")
        self.setMinimumWidth(600)
        self.setMinimumHeight(575)
        self.setMaximumWidth(600)
        self.setMaximumHeight(575)

        # Button to generate new passphrase
        self.button = QtWidgets.QPushButton("New Password")
        self.button.clicked.connect(self.generate_passphrase)

        # Various options fields
        self.nowWidget = QtWidgets.QSpinBox()
        self.nowWidget.setRange(3, 50)
        self.nowWidget.setSingleStep(1)
        self.nowWidget.setValue(6)
        self.nowWidget.valueChanged.connect(self.update_no_of_words)
        self.spCharacterWidget = QtWidgets.QSpinBox()
        self.spCharacterWidget.setRange(0, 50)
        self.spCharacterWidget.setSingleStep(1)
        self.spCharacterWidget.setValue(0)
        self.spCharacterWidget.valueChanged.connect(self.update_spcharacters)
        self.delimiterWidget = QtWidgets.QLineEdit()
        self.delimiterWidget.textChanged.connect(self.update_delimiter)

        # Display passphrase
        self.options = diceware.handle_options(args=[])
        passphrase = diceware.get_passphrase(self.options)
        self.text = QtWidgets.QLabel(passphrase,
                                     alignment=QtCore.Qt.AlignCenter)

        # Layouting things
        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("&No. of words: ", self.nowWidget)
        formLayout.addRow("&No. of special characters", self.spCharacterWidget)
        formLayout.addRow("&Delimiter", self.delimiterWidget)
        formWidget = QtWidgets.QWidget()
        formWidget.setLayout(formLayout)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(formWidget)
        layout.addWidget(self.button)
        cwidget = QtWidgets.QWidget()
        cwidget.setLayout(layout)
        self.setCentralWidget(cwidget)

    def generate_passphrase(self):
        passphrase = diceware.get_passphrase(self.options)
        self.text.setText(passphrase)
    
    def update_no_of_words(self):
        self.options.num = self.nowWidget.value()

    def update_spcharacters(self):
        self.options.specials = self.spCharacterWidget.value()
    
    def update_delimiter(self):
        self.options.delimiter = self.delimiterWidget.text()


def main():
    app = QtWidgets.QApplication([])
    widget = DicewareWidget()
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    
