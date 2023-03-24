import QtQuick 2.12
import QtQuick.Controls 2.4

import components 1.0

Rectangle {
    id: root
    anchors.fill: parent

    Row {
        id: grid
        spacing: 5

        Rectangle {
            id: canDumpArea
            width: (root.width - grid.spacing) / 3 * 2
            height: root.height

            CanDump {}
        }

         Rectangle {
            id: canSendArea
            width: (root.width - grid.spacing) / 3 * 1
            height: root.height
            color: "#f5f5dc"

            CanSend {}
        }
    }
}
