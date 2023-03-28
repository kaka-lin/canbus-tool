#ifndef CAN_MAIN_THREAD_H
#define CAN_MAIN_THREAD_H

#include <QObject>
#include <QDebug>
#include <QThread>
#include <QMap>

class CanMainThread : public QObject
{
private:
  Q_OBJECT

public:
  CanMainThread(QObject *parent = nullptr);
  ~CanMainThread();

public slots:
  // void dump();
  // void abortDump();
  // void dumpDone();

  void send(const QString &can_id,
            const QString &dlc,
            const QString &data);
  void sendDone();

signals:
  void dumpSig(const QString &time, const QString &can_id,
               const QString &dlc, const QString &data);
  void dumpInit();

private:
  QMap<QString, QThread *> threads;
};

#endif // CAN_MAIN_THREAD_H

