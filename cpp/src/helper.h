#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <ctime>

template< typename T >
std::string int_to_hex_prefix(T i) {
  std::stringstream stream;
  stream << "0x"
        //  << std::setfill('0') << std::setw(sizeof(T)*2)
         << std::hex << i;
  return stream.str();
}

template< typename T >
std::string int_to_hex(T i) {
  std::stringstream stream;
  stream << std::setfill('0') << std::setw(2)
         << std::hex << i;
  return stream.str();
}

template< typename T >
std::string zfill(T i, int length) {
  std::stringstream stream;
  stream << std::setfill('0') << std::setw(length) << i;
  return stream.str();
}

std::string currentDateTime() {
  std::time_t cur_time = std::time(nullptr);
  std::tm* now = std::localtime(&cur_time);

  char buffer[128];
  // "%m-%d-%Y %X": m-d-y h:m:s
  strftime(buffer, sizeof(buffer), "%X", now);
  return buffer;
}
