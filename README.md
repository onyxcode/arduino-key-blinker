# arduino-key-blinker
Every time you press a key on your keyboard, the built-in light on the Arduino blinks.

## Requirements
- [Arduino IDE](https://www.arduino.cc/en/software)
- [USB cable for Arduino](https://store.arduino.cc/usa/usb-2-0-cable-type-a-b)
- Compatible Arduino board [flashed with StandardFirmata](https://www.instructables.com/Arduino-Installing-Standard-Firmata)
- [pip](https://bootstrap.pypa.io/get-pip.py)
- [Python 3.8](https://www.python.org/downloads/release/python-388/)

## Installation | NOT TESTED ON WINDOWS
1. Clone the repo to your device.
2. CD to the repo location.
3. `pip install -r requirements.txt`
4. Plug in your Arduino
5. `keyblinker.py`
6. Enter the serial port that your Arduino is connected on. [Can't find it?](https://onyxcode.net/not-in-sync)
7. Enjoy the chaos!
