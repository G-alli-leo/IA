import QtQuick

ListView {
    width: 100
    height: 100
    required model

    delegate: Rectangle {
        required property string modelData
        height: 25
        width: 100
        Text { text: parent.modelData }
    }
}