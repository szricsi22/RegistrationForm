# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys, json

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot


class DataManager(QObject):
    @Slot(str, str, str, str, str)
    def save_action(self, first_name, last_name, phone, email, address):
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "address": address
        }

        with open("user_data.json", "w") as f:
            json.dump(user_data, f)


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
