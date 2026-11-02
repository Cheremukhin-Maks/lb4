import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, 
    QFileDialog, QMessageBox
)
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("task 3 Window")
        self.setMinimumSize(500, 450)


        self.text_ed = QTextEdit()
        self.setCentralWidget(self.text_ed)
        self.statusBar().showMessage("Готове до роботи")

        self.open_action = QAction("Відкрити", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setStatusTip("Відкрити текстовий файл з диска")

        
        self.save_action = QAction("Зберегти", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("Зберегти поточний текст у файл")

        
        self.exit_action = QAction("Вийти", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip("Завершити роботу програми")
        self.exit_action.triggered.connect(self.close) 

        
        self.about_action = QAction("Про програму", self)
        self.about_action.setStatusTip("v 0.0.1")

        
        self.clear_action = QAction("Очистити текст", self)
        self.clear_action.setStatusTip("Очистити всі символи у текстовому полі")
        self.clear_action.triggered.connect(self.text_ed.clear)


        menu_bar = self.menuBar()

        
        file_menu = menu_bar.addMenu("Файл")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        
        help_menu = menu_bar.addMenu("Довідка")
        help_menu.addAction(self.clear_action)
        help_menu.addAction(self.about_action)

        
        toolbar = self.addToolBar("Основна панель")
        
        
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()
        toolbar.addAction(self.clear_action)
    

        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.about_action.triggered.connect(self.show_about)
        self.text_ed.textChanged.connect(self.upd_statusbar)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Відкрити файл", "", "Текстові файли (*.txt);;Усі файли (*)"
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                self.text_ed.setText(f.read())
            self.statusBar().showMessage(f"Відкрито файл: {file_path}", 5000)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Зберегти файл", "", "Текстові файли (*.txt);;Усі файли (*)"
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.text_ed.toPlainText())
            self.statusBar().showMessage(f"Збережено у файл: {file_path}", 5000)

    def show_about(self):
        QMessageBox.about(
            self,
            "Про програму",
            "<b>Текстовий редактор PyQt6</b><br>"
            "Демонстрація меню, QToolBar та QStatusBar.<br>"
            "Лабораторна робота"
        )


    def upd_statusbar(self):
        text = self.text_ed.toPlainText()
        char_count = len(text)
        word_count = len(text.split()) if text.strip() else 0
        self.statusBar().showMessage(f"Символів: {char_count} | Слів: {word_count}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


