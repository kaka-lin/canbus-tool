#include <string.h> // strcpy

#include "canbus.h"

CanBus::CanBus() {

}

int CanBus::open(const string can_name) {
  // 1. Create a socket(int domain, int type, int protocol)
  if ((can_fd_ = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
		perror("Error while Opening Socket");
		return CanBusStatus::STATUS_SOCKET_CREATE_ERROR;
	}

  // 2. Retrieve the interface index for the interface name
  //    ex: can0, can1, vcan0 etc
	strcpy(ifr_.ifr_name, can_name.c_str());
	ioctl(can_fd_, SIOCGIFINDEX, &ifr_);

  // 3. Bind the socket to the CAN Interface:
  memset(&addr_, 0, sizeof(addr_));
	addr_.can_family  = AF_CAN;
	addr_.can_ifindex = ifr_.ifr_ifindex;

  if (bind(can_fd_, (struct sockaddr *)&addr_, sizeof(addr_)) < 0) {
		perror("Error in Socket bind");
		return CanBusStatus::STATUS_BIND_ERROR;
	}

  return CanBusStatus::STATUS_OK;
}

int CanBus::send(const CanFrame& msg) {
  struct canfd_frame frame;

  frame.can_id = msg.can_id;
  frame.len = msg.can_dlc;
  copy(msg.data.begin(), msg.data.end(), frame.data);

  if (write(can_fd_, &frame, sizeof(struct can_frame)) != sizeof(struct can_frame)) {
    perror("[Error] Write");
    return CanBusStatus::STATUS_WRITE_ERROR;
  }

  return CanBusStatus::STATUS_OK;
}
