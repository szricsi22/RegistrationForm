import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts


Window {
    width: 640
    height: 480
    visible: true
    title: "Registration Form"

    Rectangle{
        width: parent.width
        height: 400
        color: "lightgray"
    }

    ColumnLayout{
        width: parent.width / 2
        anchors.centerIn: parent

        TextField{
            Layout.fillWidth: true
            placeholderText: "First name"
        }

        TextField{
            Layout.fillWidth: true
            placeholderText: "Last name"
        }

        TextField{
            Layout.fillWidth: true
            placeholderText: "Phone"
        }

        TextField{
            Layout.fillWidth: true
            placeholderText: "Email"
        }

        TextField{
            Layout.fillWidth: true
            placeholderText: "Address"
        }
    }
}
