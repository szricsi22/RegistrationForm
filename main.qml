import QtQuick
import QtQuick.Window

Window {
    width: 640
    height: 480
    visible: true
    title: "Registration Form"

    // this is a rectangle
    Rectangle{
        x: 200
        y: 100
        width: 100
        height: 100
        color: "red"
        radius: 20
        rotation: 45

        Rectangle{
            width: 60
            height: 80
            color: "blue"
            radius: 10
            x: 70

            MouseArea{
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
            }
        }
    }
}
