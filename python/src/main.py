import sys
import os

from PyQt5.QtCore import QCoreApplication, QUrl, Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext

from src import qml
from src.thread import CanBusThread

def run(app, root_dir, mode):
    # Create QML engine
    engine = QQmlApplicationEngine()
    context = engine.rootContext()

    canbus = CanBusThread()
    context.setContextProperty("canbus", canbus)

    if mode == "prod":
        engine.addImportPath('qrc:/')
        engine.load(QUrl('qrc:/main.qml'))
    else:
        engine.addImportPath(os.path.join(root_dir, "frontend"))
        engine.load(QUrl(os.path.join(root_dir, "frontend/main.qml")))

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    run(app)
