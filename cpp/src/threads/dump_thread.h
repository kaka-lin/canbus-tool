#ifndef DUMP_THREAD_H
#define DUMP_THREAD_H

#include <QObject>
#include <QDebug>
#include <vector>

#include "src/app/canbus.h"

using namespace std;

class DumpThread : public QObject
{
private:
  Q_OBJECT

public:
  explicit DumpThread();
  ~DumpThread() {};

public slots:
  void dump();
  void abortDump();

signals:
  void dumpSig(const QString &time,
               const QString &can_id,
               const QString &dlc,
               const QString &data);
  void dumpDone();

private:
  CanBus *can_bus_;
  CanFrame msg_;
  bool __abort = false;
  int status_;
};

#endif // DUMP_THREAD_H

