#include "can_main_thread.h"
#include "dump_thread.h"
#include "send_thread.h"

CanMainThread::CanMainThread(QObject *parent) : QObject(parent)
{
}

CanMainThread::~CanMainThread()
{
}

void CanMainThread::dump()
{
  emit this->dumpInit();

  QThread *thread = new QThread(0);
  qDebug() << ">>> Dump Thread Start <<<";
  DumpThread *worker = new DumpThread();
  threads["dump"] = thread;
  workers["dump"] = QVariant::fromValue(worker);
  worker->moveToThread(thread);

  connect(worker, &DumpThread::dumpSig, this, &CanMainThread::dumpSig);
  connect(worker, &DumpThread::dumpDone, this, &CanMainThread::dumpDone);

  connect(thread, &QThread::finished, worker, &QObject::deleteLater);
  connect(thread, &QThread::started, worker, &DumpThread::dump);

  thread->start();
}

void CanMainThread::abortDump()
{
  DumpThread *worker;
  if (workers.contains("dump")) {
    worker = qvariant_cast<DumpThread *>(workers.value("dump"));
    worker->abortDump();
  }
}

void CanMainThread::dumpDone()
{
  QThread *thread;
  if (threads.contains("dump")) {
    thread = threads.value("dump");
    thread->quit();
    thread->wait();
    qDebug() << ">>> Dump Thread Finish <<<";
  }
}

void CanMainThread::send(const QString &can_id, const QString &dlc,
                         const QString &data)
{
  QThread *thread = new QThread(0);
  qDebug() << ">>> Send Thread Start <<<";
  SendThread *worker = new SendThread();
  threads["send"] = thread;
  workers["send"] = QVariant::fromValue(worker);
  worker->moveToThread(thread);

  connect(worker, &SendThread::sendDone, this, &CanMainThread::sendDone);

  connect(thread, &QThread::finished, worker, &QObject::deleteLater);
  connect(thread, &QThread::started, [=](){worker->send(can_id, dlc, data);});

  thread->start();
}

void CanMainThread::sendDone()
{
  QThread *thread;
  if (threads.contains("send")) {
    thread = threads.value("send");
    thread->quit();
    thread->wait();
    qDebug() << ">>> Send Thread Finish <<<";
  }
}
