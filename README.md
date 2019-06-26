# BikeVR-Sensor-Controller
VR Class 2019 - Group Project BikeVR - Python project for sensor controller


## Getting started

The following guideline was tested and checked with a Raspberry Pi 3 Model B+ and a Raspberry Pi Zero Wireless.
Make sure that you download and install the official Raspbian Lite Image onto your raspberry before continuing.

1. Update your Raspberry Pi `sudo apt-get update -y` & `sudo apt-get upgrade -y`
2. Requires Python 2.7 (https://www.python.org/download/releases/2.7/)
3. Install pip if not already present `sudo apt-get install python-pip`
4. Install git if not already present `sudo apt-get install git`
4. Clone project `git clone https://github.com/dangpg/BikeVR-Sensor-Controller.git`
5. Install dependencies `sudo pip install -r requirements.txt`
6. In addition, run `sudo apt-get install python-cwiid`
7. Copy [this config file](https://github.com/ukBaz/python-bluezero/blob/master/examples/ukBaz.bluezero.conf) to `/etc/dbus-1/system.d/.` (e.g. download it and copy it over `sudo cp ukBaz.bluezero.conf /etc/dbus-1/system.d/.`)
8. Restart the dbus `sudo systemctl restart dbus`
9. Start the sensor controller by running `python -m bikevr_sensor_controller`

## Add Sensor Controller to Autostart

In order to automatically start the sensor controller at startup, add the following command to your `rc.local` file:


    #!/bin/sh -e
    #
    # rc.local
    #
    # This script is executed at the end of each multiuser runlevel.
    # Make sure that the script will "exit 0" on success or any other
    # value on error.
    #
    # In order to enable or disable this script just change the execution
    # bits.
    #
    # By default this script does nothing.

    # Print the IP address
    _IP=$(hostname -I) || true
    if [ "$_IP" ]; then
    printf "My IP address is %s\n" "$_IP"
    fi

    sudo PYTHONPATH=/home/pi/BikeVR-Sensor-Controller python -m bikevr_sensor_controller &

    exit 0

Edit by typing `sudo nano /etc/rc.local` and feel free to modify the path if you saved the project under another file location.


Use `sudo ps -ax | grep python` to display all running Python applications.
In order to kill a process, use `sudo kill <PID>`


## How to run

Start sensor controller by running `python -m bikevr_sensor_controller`. The Raspberry Pi will be automatically advertise as a BLE peripheral. There are certain commands which allow for more options: (just enter these into the console)

(Currently disabled)

1. `wii` - Starts scanning for a nearby Wiimote. Press 1+2 on the Wiimote to connect. When successfully connected, the respective characteristics will be updated.

2. `exit` or `quit` - Quits the application


## List of Services and Characteristics

Name | UUID
--- | ---
Sensor-Controller Service | `00000000-0000-4b23-9358-f235b978d07c`


Name | UUID | Format | Description 
--- | --- | --- | ---
IR Sensor | `11111111-1111-4b23-9358-f235b978d07c` | boolean | Represents state of TCRT5000 sensor. 1 indicates that infrared is getting reflected back to the phototransistor, i.e. something is in front of the sensor and blocking its way.
Wiimote Status | `22222222-2222-4b23-9358-f235b978d07c` | boolean | Indicates whether Wiimote is connected or not
Wiimote Buttons | `33333333-3333-4b23-9358-f235b978d07c` | unsigned int 16 | Represents the current state of the Wiimote buttons. See `docs\wiimote_buttons.txt` for more information regarding the mapping of the buttons.

## Acknowledgements

This project would not have been possible without the following libraries:

Library | Credits | URL
--- | --- | ---
python-bluezero | ukBaz | https://github.com/ukBaz/python-bluezero
cwiid | abstrakraft | https://github.com/abstrakraft/cwiid
