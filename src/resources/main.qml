import QtQuick 2.8
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3
import QtQuick.Controls.Material 2.0
import QtQuick.Controls.Universal 2.0
import Qt.labs.settings 1.0 // QSettings的QML版本,只適合保存簡單的key-value
import QtQuick.Window 2.2
import QtQuick.Dialogs 1.2

ApplicationWindow {
    id: window
    visible: true
    //width: Screen.width
    //height: Screen.height
    //minimumWidth: 1280
    //minimumHeight: 720
    width: 640
    height: 480

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
                //text: qsTr("file")
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
                //text: qsTr("Help")
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
                //text: qsTr("Exit")
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
                //text: qsTr("dump")
                Image {
                    id: dumpImage
                    source: "images/canbus.png"
                    asynchronous:true
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                }
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {
                    canbus.dump()
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
               written with QML based on PyQt5\n
               Version: 0.0.1
               Date:2018/02/22"
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
// status -> toolBar
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

    CanBus {}
}
