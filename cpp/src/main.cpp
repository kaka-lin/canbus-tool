#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QDebug>

#include "threads/can_main_thread.h"

int main(int argc, char *argv[])
{
  QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
  QGuiApplication app(argc, argv);
  QString program_name(argv[0]);

  app.setOrganizationName("Kaka");
  app.setOrganizationDomain("https://github.com/kaka-lin");
  app.setApplicationName("CanBus Tool");
  app.setApplicationVersion("0.0.1");

  QQmlApplicationEngine engine;

  CanMainThread *canbus = new CanMainThread();
  engine.rootContext()->setContextProperty("canbus", canbus);

  engine.addImportPath(QStringLiteral("qrc:/"));
  engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
  if (engine.rootObjects().isEmpty()) {
    return -1;
  }

  return app.exec();
}
