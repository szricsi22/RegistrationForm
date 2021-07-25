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
            id: first_name_field
            Layout.fillWidth: true
            placeholderText: "First name"
        }

        TextField{
            id: last_name_field
            Layout.fillWidth: true
            placeholderText: "Last name"
        }

        TextField{
            id: phone_field
            Layout.fillWidth: true
            placeholderText: "Phone"
        }

        TextField{
            id: email_field
            Layout.fillWidth: true
            placeholderText: "Email"
        }

        TextField{
            id: address_field
            Layout.fillWidth: true
            placeholderText: "Address"
        }
    }

    Button{
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 20
        width: 100
        height: 50
        text: "Save"

        onClicked: DoNothing.print_do_nothing()
    }
}
