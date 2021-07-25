# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot


class DataManager(QObject):
    def __init__(self):
        super(DataManager, self).__init__()

    @Slot()
    def print_hello(self):
        print("Hello from DataManager")


class RegistrationForm:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.context = self.engine.rootContext()

        self.data_manager = DataManager()
        self.context.setContextProperty("DataManager", self.data_manager)

        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)
        sys.exit(self.app.exec())


if __name__ == "__main__":
    RegistrationForm()
