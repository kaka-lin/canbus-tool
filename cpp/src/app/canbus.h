#ifndef CANBUS_H
#define CANBUS_H

#include <iostream>
#include <string>
#include <vector>

#include <unistd.h>
#include <net/if.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>

#include <linux/can.h>
#include <linux/can/raw.h>

using namespace std;

struct CanFrame {
  uint32_t can_id;
  uint8_t can_dlc;
  uint8_t flags;
  // uint8_t data[64];
  vector<uint8_t> data;
};

enum CanBusStatus {
  STATUS_OK = 1,
  STATUS_SOCKET_CREATE_ERROR = 1 << 1,
  STATUS_INTERFACE_NAME_TO_IDX_ERROR = 1 << 2,
  STATUS_BIND_ERROR = 1 << 3,
  STATUS_WRITE_ERROR = 1 << 4,
  STATUS_READ_ERROR = 1 << 5,
};

class CanBus {
 public:
  CanBus();
  ~CanBus() {};

  int open(const string can_name="can0");
  int send(const CanFrame& msg);
  int recv(CanFrame& msg);
  int close();
  int canStatus = 0;

 private:
  int can_fd_;
  int nbytes_;
  struct ifreq ifr_; // for saving config of interface
  struct sockaddr_can addr_;
};

#endif // CANBUS_H
