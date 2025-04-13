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
        main_layout.addWidget(self.input_widget())
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

    def input_widget(self):
        """
        The section of the main window for the user to input a two key pieces
        of information:
        
            - The Download Link, the network location of the file to download.
            - The Target Folder, the network location to store the file.

        Returns:
            - `input_widget`:
                The PyQt6 widget item to add to the main window.
        """
        # Setup the input widget
        input_widget = qtw.QWidget()
        input_layout = qtw.QVBoxLayout()

        # Download Link Field

        # Setup the download link input field
        download_link_widget = qtw.QWidget()
        download_link_layout = qtw.QHBoxLayout()

        # Add the download link input field
        self.download_link_label = qtw.QLabel("Download Link:")
        self.download_link_field = qtw.QLineEdit()

        # Compile the download link input field
        download_link_layout.addWidget(self.download_link_label)
        download_link_layout.addWidget(self.download_link_field)
        download_link_widget.setLayout(download_link_layout)

        # Target Folder Field

        # Setup the download link input field
        target_folder_widget = qtw.QWidget()
        target_folder_layout = qtw.QHBoxLayout()

        # Add the download link input field
        self.target_folder_label = qtw.QLabel("Target Folder:")
        self.target_folder_field = qtw.QLineEdit()

        # Compile the download link input field
        target_folder_layout.addWidget(self.target_folder_label)
        target_folder_layout.addWidget(self.target_folder_field)
        target_folder_widget.setLayout(target_folder_layout)

        # Run Process Button

        # Setup the run process button
        run_button_widget = qtw.QWidget()
        run_button_layout = qtw.QHBoxLayout()

        run_button = qtw.QPushButton("Run Process")

        # Compile run button
        run_button_layout.addWidget(run_button)
        run_button_widget.setLayout(run_button_layout)

        # Balancing

        # Balance the input field widths
        label_max_width = max(
            self.download_link_label.widthMM(),
            self.target_folder_label.widthMM()
        )
        self.download_link_label.setFixedWidth(label_max_width)
        self.target_folder_label.setFixedWidth(label_max_width)

        self.download_link_field.setMinimumWidth(300)
        self.target_folder_field.setMinimumWidth(300)

        # Compile input widget
        input_layout.addWidget(download_link_widget)
        input_layout.addWidget(target_folder_widget)
        input_layout.addWidget(run_button_widget)
        input_widget.setLayout(input_layout)

        return input_widget
    

# Start function at runtime
if __name__ == '__main__':
    DownloadManager()
