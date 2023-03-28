#ifndef SEND_THREAD_H
#define SEND_THREAD_H

#include <QObject>
#include <QDebug>
#include <vector>

#include "src/app/canbus.h"

using namespace std;

class SendThread : public QObject
{
private:
  Q_OBJECT

public:
  explicit SendThread();
  ~SendThread() {};

public slots:
  void send(const QString &can_id,
            const QString &dlc,
            const QString &data);

signals:
  void sendDone();
  void sendErrMsg(const QString &error);

private:
  CanBus *can_bus_;
  uint32_t can_id_;
  uint8_t dlc_;
  vector<uint8_t> can_data_;
  CanFrame msg_;
};

#endif // SEND_THREAD_H

