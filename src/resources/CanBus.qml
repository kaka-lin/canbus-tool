import QtQuick 2.0
import QtQuick.Controls 1.4

Rectangle {
    width: parent.width
    height: 200

    TableView {
        id: tableView

        frameVisible: false
        sortIndicatorVisible: true

        anchors.fill: parent

        onRowCountChanged: {
            positionViewAtRow(rowCount - 1, ListView.End)
        }

        TableViewColumn {
            id: canidColumn
            title: "CAN ID"
            role: "can_id"
            movable: false
            resizable: false
            width: tableView.viewport.width / 3
        }

        TableViewColumn {
            id: dataColumn
            title: "DATA"
            role: "can_data"
            movable: false
            resizable: false
            width: tableView.viewport.width - canidColumn.width
        }

        model: listModel

        ListModel { id: listModel}

        WorkerScript {
            id: worker
            source: "candump.js" // 聲明js處理函數
        }

        Timer {
            id: timer
            interval: 1000; repeat: true
            running: true
            triggeredOnStart: true

            onTriggered: {
                canbus.dump(function(can_id, can_data) {
                    if (can_id != '') {
                        var msg = {'can_id': can_id, 'can_data': can_data, 'model': listModel};
                        worker.sendMessage(msg);
                    }
                })
            }
        }
    }
}
