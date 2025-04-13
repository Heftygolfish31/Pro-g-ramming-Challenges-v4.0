# Download Manager

# Standard Libraries
import sys

# The GUI library
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg


# Program information
class METADATA:
    TITLE = "Download Manager"
    VERSION = "v0.0.1"


class DownloadManager:
    def __init__(self):
        # Start the GUI engine
        app = qtw.QApplication(sys.argv)

        # Setup the main window
        main_widget = qtw.QWidget()
        main_layout = qtw.QVBoxLayout()

        # Configure the main window
        main_widget.setWindowTitle(METADATA.TITLE + " " + METADATA.VERSION)

        # Compile the main widget
        main_layout.addWidget(self.title_widget())
        main_widget.setLayout(main_layout)

        # Run the device!
        main_widget.show()
        app.exec()

    def title_widget(self):
        """
        The section of the window dedicated to the logo, title, and similar
        information.

        Returns:
            - `title_widget`:
                The PyQt6 widget item to add to the main window.
        """
        # Setup the title widget
        title_widget = qtw.QWidget()
        title_layout = qtw.QVBoxLayout()

        # Add the program title
        title_label = qtw.QLabel(METADATA.TITLE)
        title_label.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(qtg.QFont("Cantarell", 28, 600))

        # Add the program version
        version_label = qtw.QLabel(METADATA.VERSION)
        version_label.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        version_label.setFont(qtg.QFont("Cantarell", 12, italic=600))

        # Compile the title widget
        title_layout.addWidget(title_label)
        title_layout.addWidget(version_label)
        title_widget.setLayout(title_layout)

        return title_widget


# Start function at runtime
if __name__ == '__main__':
    DownloadManager()
