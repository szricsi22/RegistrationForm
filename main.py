# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys, json
from datetime import datetime

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Property, Signal, QTimer


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


class Clock(QObject):
    changed = Signal()

    def __init__(self):
        super(Clock, self).__init__()

        self._current_time = ""
        self.set_new_time()

        self.my_timer = QTimer()
        self.my_timer.timeout.connect(self.set_new_time)
        self.my_timer.start(1000)

    def set_new_time(self):
        now = datetime.now()
        self._current_time = now.strftime("%H:%M:%S")
        self.changed.emit()

    def _get_current_time(self):
        return self._current_time

    current_time = Property(str, _get_current_time, notify=changed)


class RegistrationForm:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.context = self.engine.rootContext()


        self.data_manager = DataManager()
        self.context.setContextProperty("DataManager", self.data_manager)

        self.clock = Clock()
        self.context.setContextProperty("Clock", self.clock)


        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    RegistrationForm()
