import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QTabWidget, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QFileDialog, QFontDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - Ajundasrika")
        self.setGeometry(100, 100, 500, 300)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.init_menu()
        self.init_tabs()

    def init_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Keluar", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        fitur_menu = menu_bar.addMenu("Fitur")

        input_nama_action = QAction("Input Nama", self)
        input_nama_action.triggered.connect(lambda: self.tabs.setCurrentIndex(0))
        fitur_menu.addAction(input_nama_action)

        pilih_font_action = QAction("Pilih Font", self)
        pilih_font_action.triggered.connect(lambda: self.tabs.setCurrentIndex(1))
        fitur_menu.addAction(pilih_font_action)

        buka_file_action = QAction("Buka File", self)
        buka_file_action.triggered.connect(lambda: self.tabs.setCurrentIndex(2))
        fitur_menu.addAction(buka_file_action)

    def init_tabs(self):
        # Tab 1
        tab1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.setAlignment(Qt.AlignCenter)

        btn_input = QPushButton("Input Nama")
        btn_input.setStyleSheet("background-color: green; color: white")
        btn_input.clicked.connect(self.show_name)

        self.name_input = QLineEdit()
        self.name_label = QLabel("Nama:")

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.name_label)
        input_layout.addWidget(self.name_input)

        layout1.addWidget(btn_input, alignment=Qt.AlignCenter)
        layout1.addLayout(input_layout)
        tab1.setLayout(layout1)

        # Tab 2
        tab2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.setAlignment(Qt.AlignCenter)

        btn_font = QPushButton("Pilih Font")
        btn_font.setStyleSheet("background-color: green; color: white")
        btn_font.clicked.connect(self.select_font)

        layout2.addWidget(btn_font, alignment=Qt.AlignCenter)
        tab2.setLayout(layout2)

        # Tab 3
        tab3 = QWidget()
        layout3 = QVBoxLayout()
        layout3.setAlignment(Qt.AlignCenter)

        self.file_content = QLabel("")
        self.file_content.setAlignment(Qt.AlignCenter)
        btn_file = QPushButton("Buka File")
        btn_file.setStyleSheet("background-color: green; color: white")
        btn_file.clicked.connect(self.open_file)

        layout3.addWidget(btn_file, alignment=Qt.AlignCenter)
        layout3.addWidget(self.file_content, alignment=Qt.AlignCenter)
        tab3.setLayout(layout3)

        self.tabs.addTab(tab1, "Input Nama")
        self.tabs.addTab(tab2, "Pilih Font")
        self.tabs.addTab(tab3, "Buka File")

    def show_name(self):
        nama = self.name_input.text()
        self.name_label.setText(f"Nama: {nama}")

    def select_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.name_input.setFont(font)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Buka File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'r') as f:
                content = f.read()
            self.file_content.setText(f"Buka File .txt\n{content}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
