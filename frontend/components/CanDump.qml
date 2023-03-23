import QtQuick 2.10
import QtQuick.Controls 1.4

Rectangle {
    anchors.fill: parent

    TableView {
        id: tableView

        frameVisible: false
        sortIndicatorVisible: true

        anchors.fill: parent

        onRowCountChanged: {
            positionViewAtRow(rowCount - 1, ListView.End)
        }

        TableViewColumn {
            id: timeColumn
            title: "Time"
            role: "time"
            movable: false
            resizable: false
            width: tableView.viewport.width / 4
        }

        TableViewColumn {
            id: canidColumn
            title: "CAN ID"
            role: "can_id"
            movable: false
            resizable: false
            width: tableView.viewport.width / 4
        }

        TableViewColumn {
            id: dlcColumn
            title: "DLC"
            role: "dlc"
            movable: false
            resizable: false
            width: tableView.viewport.width / 12
        }

        TableViewColumn {
            id: dataColumn
            title: "DATA"
            role: "data"
            movable: false
            resizable: false
            width: (tableView.viewport.width / 3) * 2
        }

        model: listModel

        ListModel { id: listModel}

        WorkerScript {
            id: worker
            source: "qrc:/js/candump.js"  // 聲明js處理函數 or "../js/candump.js"
        }
    }

    Connections {
        target: canbus

        // Sum signal handler
        onDumpSig: {
            console.log(time + ' ' + can_id + ' ' + dlc + ' ' + data);
            var msg = {'time': time, 'can_id': can_id, 'dlc': dlc, 'data': data, 'model': listModel};
            worker.sendMessage(msg);
        }
    }
}
