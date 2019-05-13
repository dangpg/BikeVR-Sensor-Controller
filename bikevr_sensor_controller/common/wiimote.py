import cwiid
import subprocess
import re

BLUETOOTH_TIMEOUT = 1000

def Wiimote():
    wiimote = cwiid.Wiimote()
    wiimote.led = 1
    wiimote.enable(cwiid.FLAG_MOTIONPLUS)
    wiimote.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_MOTIONPLUS
    connected_devices = subprocess.check_output(("hcitool","con"))
    addresses = re.findall(r"(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))",connected_devices)
    for i in addresses:
        name = subprocess.check_output(("hcitool","name",i[0]))
        if name.strip()=="Nintendo RVL-CNT-01":
            subprocess.call(("hcitool","lst",i[0], str(BLUETOOTH_TIMEOUT*16/10)))

    return wiimote
