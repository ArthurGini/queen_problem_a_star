from PyQt5 import QtWidgets as qtw, QtCore, QtGui
from mainUI import Ui_MainWindow
from PyQt5.QtCore import QThread, QTimer
import sys, os, glob, PyQt5, time
from a_star import RunAStarAlgorithm


# If the resolution is high, then these lines will take care of the UI being displayed properly.
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


folder = 'states_images'
a_star_output = []


class MainWindow(qtw.QMainWindow):
    """Class that handles all the backend of the UI."""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.index = None
        print(self.index)
        self.image_names = []

        self.a_star_thread = None

        self.ui.autoTrace.clicked.connect(self.run_auto_trace)
        self.ui.stopAutotrace.clicked.connect(self.stop_auto_trace)

        self.ui.nextButton.clicked.connect(self.show_next_image)
        self.ui.prevButton.clicked.connect(self.show_prev_image)

        self.ui.runAStarButton.clicked.connect(self.run_a_star)
        self.ui.stopastarButton.clicked.connect(self.stop_a_star_thread)

        self.ui.resetButton.clicked.connect(self.reset)

        self.ui.nextButton.setDisabled(True)
        self.ui.prevButton.setDisabled(True)
        self.ui.autoTrace.setDisabled(True)
        self.ui.stopAutotrace.setDisabled(True)

        os.makedirs(folder, exist_ok=True) # Creating folder to store images if it does not exist.

    def run_a_star(self):
        """Function to run the A* algorithm. It uses a thread to run the algorithm in the background."""

        N_queens = self.ui.nQueenSpinBox.value()

        self.a_star_thread = AStarAlgorithmThread(N_queens=N_queens)

        self.ui.outputLabel.setText("A Star Algorithm Running...")
        self.a_star_thread.start()
        self.a_star_thread.finished.connect(self.show_a_star_results)

    def stop_a_star_thread(self):
        """Function to stop the algorithm's thread and enable some buttons."""

        self.ui.outputLabel.setText('Searching Stopped!')
        self.a_star_thread.terminate()

        self.ui.nextButton.setDisabled(False)
        self.ui.prevButton.setDisabled(False)
        self.ui.autoTrace.setDisabled(False)
        self.ui.stopAutotrace.setDisabled(False)
        win.close() # Closing window as stopping on large inputs can sometimes freeze the window.

    def show_a_star_results(self):
        """Function to display the output of the algorithm."""

        global a_star_output
        if len(a_star_output) != 0:
            output = f'Steps = {a_star_output[0]} | Time = {a_star_output[1] :.4} secs | Solution Found = {a_star_output[2]}'
            self.ui.outputLabel.setText(output)
            self.load_images_directory()
        else:
            print('Output List is Empty!')

    def run_auto_trace(self):
        """Function to run auto trace feature."""

        self.image_names.clear()

        self.load_images_directory()

        self.file_it = iter(self.image_names)

        self._timer = QtCore.QTimer(self, interval=300)
        self._timer.timeout.connect(self._on_timeout)
        self._timer.start()


    def stop_auto_trace(self):
        """Function to stop the auto tracer."""

        self._timer.stop()


    def _on_timeout(self):
        """Utility timeout function for auto tracing."""

        try:
            img = next(self.file_it)

            self.ui.imagecountLabel.setText(img)
            self.ui.imageLabel.setPixmap(QtGui.QPixmap(folder+'\\'+img))
        except StopIteration:
            self._timer.stop()

    def stop_auto_trace(self):
        """Function to stop the auto tracer."""

        self._timer.stop()

    def load_images_directory(self):
        """Function that loads the image names from the 'states_images' directory."""

        for filename in sorted(os.listdir(folder), key=lambda f: int(f[5:-4])):
            self.image_names.append(filename)
        print(self.image_names)

        self.ui.nextButton.setDisabled(False)
        self.ui.prevButton.setDisabled(False)
        self.ui.autoTrace.setDisabled(False)
        self.ui.stopAutotrace.setDisabled(False)

    def show_next_image(self):
        """Function to show next image in line."""

        if self.index is None:
            self.index = 0

        img = self.image_names[self.index]
        self.ui.imageLabel.setPixmap(QtGui.QPixmap(folder+'\\'+img))
        self.ui.imagecountLabel.setText(img)
        self.index += 1
        self.index = self.index % len(self.image_names)

    def show_prev_image(self):
        """Function to show previous image in line."""

        self.index -= 1
        self.index = self.index % len(self.image_names) # Using the property og -ve modulo in python.
        img = self.image_names[self.index]
        self.ui.imageLabel.setPixmap(QtGui.QPixmap(folder+'\\'+img))
        self.ui.imagecountLabel.setText(img)

    def reset(self):
        self.ui.outputLabel.setText("Steps/Time")
        self._clear_states_images_folder()
        self._display_initial_text()
        self.index = None
        self.image_names = []
        self.ui.imagecountLabel.setText('Image Count')
        self.ui.nextButton.setDisabled(True)
        self.ui.prevButton.setDisabled(True)
        self.ui.autoTrace.setDisabled(True)
        self.ui.stopAutotrace.setDisabled(True)

    def _clear_states_images_folder(self):
        """Function to clear image folder and reset the instructions on the main screen."""

        files = glob.glob('states_images/**/*.png', recursive=True)
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print(f"Error: {f} : {e.strerror}")
        self._display_initial_text()

    def _display_initial_text(self):
        """Function to display initial instructions again."""

        _translate = QtCore.QCoreApplication.translate
        text = '''<html><head /><body>	<p align=\"justify\"><span style=\" font-size:16pt; font-weight:600; text-decoration:			underline;\">Instrucoes:</span><span style=\" font-size:12pt; font-weight:600;\">:</span></p>	<p align=\"justify\"><span style=\" font-size:12pt; font-weight:300; text-decoration: bold;\"></span>1. Escolha a quantidade de rainhas n.</p></body></html>'''
        self.ui.imageLabel.setText(_translate("MainWindow", text))


class AStarAlgorithmThread(QThread):
    """Class that runs the algorithm as a thread."""

    def __init__(self, N_queens):
        super().__init__()
        self.N_queens = N_queens

    def run(self):
        global a_star_output
        a_star_output = RunAStarAlgorithm.run_a_star(N_queens=self.N_queens)



if __name__ == '__main__':
    app = qtw.QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())