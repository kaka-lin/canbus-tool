#include "can_main_thread.h"
#include "send_thread.h"

CanMainThread::CanMainThread(QObject *parent) : QObject(parent)
{
}

CanMainThread::~CanMainThread()
{
}

void CanMainThread::send(const QString &can_id, const QString &dlc,
                         const QString &data)
{
    QThread *thread = new QThread(0);
    qDebug() << ">>> Send Thread Start <<<";
    SendThread *worker = new SendThread();
    threads["send"] = thread;
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
