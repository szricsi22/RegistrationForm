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
        width: 100
        height: 100
        color: "red"
        radius: 20

        Rectangle{
            width: 50
            height: 50
            color: "blue"
            radius: 20
        }
    }
}
