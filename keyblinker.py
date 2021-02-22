from pynput.keyboard import Listener
from pyfirmata import Arduino
import sys


if __name__ == "__main__":
    try:
        def on_press(key):
            pass


        def on_release(key):
            print('{0} pressed, now blinking LED.'.format(key))
            with open("/media/daniel/PROJECTS/arduino-stuff/key.log", "a") as log:
                log.write('{0} pressed, now blinking LED.\n'.format(key))
                log.close()
            board.digital[13].write(0)
            board.digital[13].write(1)

        port = input("Enter your serial port.\n>")
        board = Arduino(port)
        print(f"Communication established with Arduino UNO on port {port}.")

        # Collect events until released
        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

    except KeyboardInterrupt:
        count = 0
        for line in open("key.log", "r").readlines():
            count += 1
        print(f"\nLED has blinked {count} times.")
        sys.exit(0)

