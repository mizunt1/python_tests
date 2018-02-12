"""
steps to inplement a q thread.
if the thread is going to result in outputting information that will be printed on
the gui, connect the signal made in the q thread to a function which prints that signal on the
gui.
connect the qthread to the desired function
qthread.connect(self.updategui)

 This function must have the decorator @pyqtSlot so that it can recieve the emitted signal.
create the function to write on the gui
create an instance of the qthread class and start it
qthread.start()

create a separete class for the thread
make some signals
pyqtSignal()
write a function which returns the actual outputted value every time the function is called
write a second function which calls the above function ^ in a loop.
this second function will include the emit signals
"""


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
        self.ui.progressBar.setValue(0)
        self.ui.pushButton.clicked.connect(self.start_generation)
        self.show()
        
    def start_generation(self):
        number_of_numbers = int(self.ui.input.text())
        self.thread_class = StartGenerationThread(number_of_numbers)
        # start thread
        self.thread_class.number_updated_signal.connect(self.add_to_list)
        self.thread_class.new_number_signal.connect(self.progress)
        # connect thread signal to function
        self.thread_class.start()
        # start thread
        
    @pyqtSlot(int)
    # this allows us to collect the emitted int and pass it to listwidget
    def add_to_list(self, number):
        self.ui.output_view.addItem(str(number))

    @pyqtSlot(int)
    def progress(self, percentage):
        self.ui.progressBar.setValue(percentage*10)

        
class StartGenerationThread(QThread):
    number_updated_signal = pyqtSignal(int)
    new_number_signal = pyqtSignal(int)
    
    def __init__(self, number_of_numbers):
        QThread.__init__(self)
        self.number_of_numbers = number_of_numbers
        
    def start_generation(self):
        time.sleep(2)
        return np.random.randint(1, 10)
        
    def run(self):
        for i in range(self.number_of_numbers):
            top_number = self.start_generation()
            self.number_updated_signal.emit(top_number)
            self.new_number_signal.emit((i/self.number_of_numbers)*10)

            
def main():
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()
