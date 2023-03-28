#include "send_thread.h"

SendThread::SendThread()
{
  can_bus_ = new CanBus();
  can_bus_->open();
}

void SendThread::send(const QString &can_id, const QString &dlc,
                      const QString &data)
{
  can_id_ = can_id.toUInt(nullptr, 16);
  dlc_ = dlc.toUInt();
  int data_length = data.length();
  if (data_length / 2 != dlc_) {
    emit sendErrMsg("Data length wrong, please check it");
    return;
  }

  can_data_.reserve(dlc_);
  for (int i = 0; i < data_length; i += 2) {
    can_data_.push_back(data.mid(i, 2).toUInt(nullptr, 16));
  }

  msg_.can_id = can_id_;
  msg_.can_dlc = dlc_;
  msg_.data = can_data_;
  can_bus_->send(msg_);
  emit sendDone();
}
