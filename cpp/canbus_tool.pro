QT += qml quick
CONFIG += c++17
#CFLAGS = -Wall -pedantic -fPIC
#CXXFLAGS = -Wall -pedantic -fPIC

# The following define makes your compiler emit warnings if you use
# any Qt feature that has been marked deprecated (the exact warnings
# depend on your compiler). Refer to the documentation for the
# deprecated API to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS \

# You can also make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

UI_DIR += obj
RCC_DIR += obj
MOC_DIR += obj
OBJECTS_DIR += obj
#DESTDIR = obj

SOURCES += \
    src/main.cpp \
    src/app/canbus.cpp \
    src/threads/can_main_thread.cpp \
    src/threads/send_thread.cpp

HEADERS += \
    src/app/canbus.h \
    src/threads/can_main_thread.h \
    src/threads/send_thread.h

RESOURCES += ../frontend/qml.qrc

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Additional import path used to resolve QML modules just for Qt Quick Designer
QML_DESIGNER_IMPORT_PATH =

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
