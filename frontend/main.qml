import QtQuick 2.8
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3
import QtQuick.Controls.Material 2.0
import QtQuick.Controls.Universal 2.0
import Qt.labs.settings 1.0 // QSettings的QML版本,只適合保存簡單的key-value
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2
import QtGraphicalEffects 1.0 // DropShadow

import components.common 1.0
import "pages"

ApplicationWindow {
    id: window
    visible: true
    //width: Screen.width
    //height: Screen.height
    //minimumWidth: 1280
    //minimumHeight: 720
    width: 1280
    height: 720

    title: qsTr("CanBus Tool")

    property real dpi: Screen.pixelDensity.toFixed(2)

//////////////////////////////////////////////////////////////////////////
// menu -> toolBar

    header: ToolBar {
        id: menu

        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 50
            border.color: "#999"
            //color: "blue"

            gradient: Gradient {
                GradientStop { position: 0 ; color: "#fff" }
                GradientStop { position: 1 ; color: "#eee" }
            }
        }

        Row {
            anchors.fill: parent
            spacing: 5

            ToolButton {
                Image {
                    id: newFileImage
                    source: "images/newFile.ico"
                    asynchronous:true
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                }
                anchors.verticalCenter: parent.verticalCenter
                onClicked: fileDialog.open();
            }

            ToolButton {
                Image {
                    id: aboutImage
                    source: "images/about.ico"
                    asynchronous:true
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                }
                anchors.verticalCenter: parent.verticalCenter
                onClicked: aboutBox.open();
            }

            ToolButton {
                Image {
                    id: exitImage
                    source: "images/exit.ico"
                    asynchronous:true
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                }
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {
                    Qt.quit();
                }
            }

            ToolButton {
                id: canbusButton
                checkable: true
                checked: false
                anchors.verticalCenter: parent.verticalCenter

                Image {
                    id: dumpImage
                    source: canbusButton.checked ? "images/connect.png" : "images/disconnect.png"
                    asynchronous:true
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                }

                DropShadow {
                    anchors.fill: dumpImage
                    horizontalOffset: 3
                    verticalOffset: 3
                    samples: 17
                    color: "#80000000"
                    source: dumpImage
                }

                onClicked: {
                    if (checked) {
                        canbus.dump()
                    } else {
                        canbus.abortDump()
                    }
                }
            }
        }

        Clock {
            id: clock
            anchors.right: parent.right
            //anchors.top: parent.top
            //anchors.topMargin: 15
            anchors.verticalCenter: parent.verticalCenter

            gradient: Gradient {
                GradientStop { position: 0 ; color: "#fff" }
                GradientStop { position: 1 ; color: "#eee" }
            }
        }
    }

    MessageDialog {
        id: aboutBox
        title: "About"
        text: "
               This is CanBus Tool
               written with QML
               based on PyQt5\n
               Version: 0.1
               Date:2018/02/26"
        icon: StandardIcon.Information
    }

    FileDialog {
        id: fileDialog
        visible: false
        title: "Please choose a file"
        folder: shortcuts.home
        selectFolder: true
    }

//////////////////////////////////////////////////////////////////////////
// footer -> toolBar

    footer: ToolBar {
        id: status

        background: Rectangle {
            implicitWidth: 100
            implicitHeight: 40
            border.color: "#999"
            //color: "blue"

            gradient: Gradient {
                GradientStop { position: 0 ; color: "#fff" }
                GradientStop { position: 1 ; color: "#eee" }
            }
        }

        RowLayout {
            anchors.fill: parent

            Image {
                id: statusImage
                source: "images/light_r.png"
                sourceSize.height: status.height-5
                asynchronous:true
                fillMode: Image.PreserveAspectFit
            }


            Label {
                id: statusLabel
                anchors.centerIn: parent
                text: "CanBus Test"
                color: "black"
                font.pixelSize: 20
            }
        }
    }

//////////////////////////////////////////////////////////////////////////
// Page

    CanBusToolPage {}
}
