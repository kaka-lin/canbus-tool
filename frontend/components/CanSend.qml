import QtQuick 2.12
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3

Rectangle {
    id: root
    anchors.fill: parent
    color: parent.color

    property real area_width: 250

    Column {
        anchors.fill: root

        spacing: 10

        GridLayout {
            id: grid

            columns: 2
            rows: 4
            rowSpacing: 12
            columnSpacing: 12

            // row 1
            Label {
                id: canID
                text: "Message ID"

                Layout.row: 0
                Layout.column: 0
            }

            TextField {
                id: canIDField
                Layout.preferredWidth: area_width
                placeholderText: qsTr("0x123")

                selectByMouse: true

                Layout.row: 0
                Layout.column: 1

                onAccepted: {
                    sendBtn.enabled = true;
                }

                onTextChanged: {
                    sendBtn.enabled = false;
                }
            }

            // row 2
            Label {
                id: dlc
                text: "DLC"

                Layout.row: 1
                Layout.column: 0
            }

            TextField {
                id: dlcField
                Layout.preferredWidth: area_width
                placeholderText: qsTr("8")

                selectByMouse: true

                Layout.row: 1
                Layout.column: 1

                onAccepted: {
                    sendBtn.enabled = true;
                    // canbus.writeSerialNum(root.current_module, text);
                }

                onTextChanged: {
                    sendBtn.enabled = false;
                }
            }

            // row 3
            Label {
                id: data
                text: "Data Bytes (hex string)"

                Layout.row: 2
                Layout.column: 0
            }

            TextField {
                id: dataField
                Layout.preferredWidth: area_width
                placeholderText: qsTr("DEADBEEF00113144")

                selectByMouse: true

                Layout.row: 2
                Layout.column: 1

                onAccepted: {
                    sendBtn.enabled = true;
                }

                onTextChanged: {
                    sendBtn.enabled = false;
                }
            }

            // row 4
            Button {
                id: sendBtn
                text: "Send"

                enabled: false

                Layout.row: 4
                Layout.column: 0

                onClicked: {
                    canbus.send(canIDField.text, dlcField.text, dataField.text);
                }
            }
        }
    }
}
