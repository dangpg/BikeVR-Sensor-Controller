# BikeVR-Sensor-Controller
VR Class 2019 - Group Project BikeVR - Python project for sensor controller


## Getting started

1. Run and tested only on Raspberry Pi 3 Model B+
2. Requires Python 2.7 (https://www.python.org/download/releases/2.7/)
3. Clone project and run `pip install -r requirements.txt`
4. In addition, run `sudo apt-get install python-cwiid`


## How to run

Start sensor controller by running `python -m bikevr_sensor_controller`. The Raspberry Pi will be automatically advertise as a BLE peripheral. There are certain commands which allow for more options: (just enter these into the console)

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