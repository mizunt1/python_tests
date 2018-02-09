import sys
import time
import numpy as np
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication

from gui import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_generation)
        self.show()
        
    def start_generation(self):
        number_of_numbers = int(self.ui.input.text())
        self.thread_class = StartGenerationThread(number_of_numbers)
        # start thread
        self.thread_class.number_updated_signal.connect(self.add_to_list)
        # connect thread signal to function
        self.thread_class.start()
        # start thread
        
    @pyqtSlot(int)
    # this allows us to collect the emitted int and pass it to listwidget
    def add_to_list(self, number):
        self.ui.output_view.addItem(str(number))


class StartGenerationThread(QThread):
    number_updated_signal = pyqtSignal(int)

    def __init__(self, number_of_numbers):
        QThread.__init__(self)
        self.number_of_numbers = number_of_numbers
        
    def start_generation(self):
        time.sleep(2)
        return np.random.randint(1, self.number_of_numbers)
        
    def run(self):
        for i in range(self.number_of_numbers):
            top_number = self.start_generation()
            self.number_updated_signal.emit(top_number)
            print(top_number)

            
def main():
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()