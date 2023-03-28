#include <QString>

#include "dump_thread.h"
#include "src/helper.h"

DumpThread::DumpThread()
{
  can_bus_ = new CanBus();
  can_bus_->open();
}

void DumpThread::dump()
{
  QString time, can_id, dlc, data_string;

  while (true) {
    if (this->__abort) {
      break;
    }

    can_bus_->recv(msg_);

    time = QString::fromStdString(currentDateTime());
    can_id = QString::fromStdString(int_to_hex_prefix(int(msg_.can_id)));
    dlc = QString::fromStdString(zfill(int(msg_.can_dlc), 2));
    for (uint8_t i = 0; i < msg_.can_dlc; i++) {
      QString d = QString::fromStdString(int_to_hex(int(msg_.data[i]))).toUpper();
      data_string.append(d);
      data_string.append(" ");
    }
    emit dumpSig(time, can_id, dlc, data_string);
    data_string = "";
  }

  emit dumpDone();
}


void DumpThread::abortDump()
{
  this->__abort = true;
}
