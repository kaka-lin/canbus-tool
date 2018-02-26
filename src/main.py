import sys
from PyQt5.QtCore import QCoreApplication, QUrl, Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlContext
from src.thread import CanBusThread

def run(app):
    #QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    # Create the application instance.
    #app = QGuiApplication(sys.argv)

    # Create QML engine
    engine = QQmlApplicationEngine()
    context = engine.rootContext()

    canbus = CanBusThread()
    context.setContextProperty("canbus", canbus)

    engine.load(QUrl('src/resources/main.qml'))

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    run(app)
