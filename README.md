# raspberry-pi-sensehat-demos
Some examples to use the raspberry pi sensehat with Python

* Advanced rainbow: creates a reflection curve, converts to RGB and displays the result on the LED matrix.
* Countdown: converts numbers to a 3 * 5 matrix, so 2 numbers fit on the LED matrix. Counts down from 99 to 0.
* Compass: displays a dot on the LED matrix that points north.
* Joystick: move a dot over the LED matrix usingthe joystick.
* Point up: the arrow on the LED matrix points up and is colored red when shaken.


# Install RTIMULib
sudo apt-get install -y git cmake python3-dev libopenjp2-7 libtiff6
cd ~
git clone https://github.com/RPi-Distro/RTIMULib.git
cd RTIMULib/Linux/python
python setup.py build
python setup.py install
python -c "from sense_hat import SenseHat; print('Success')"