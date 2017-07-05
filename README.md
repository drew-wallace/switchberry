# The SwitchBerry Setup Guide
The SwitchBerry is a mobile PC game streaming device inspired by the Nintendo Switch and made from a Raspberry Pi. The goal was to play my PC games on the go, mouse and keyboard free, with little to no latency, and a steady frame rate.

## Credits
I did not do this project alone. I was helped by friends, family, and the Parsec community. Because of how awesome everyone has been, I feel the credits should come first.

  - My wife: for lettimg me spend a chunk of change and most of my free time for the past month on this!
  - @CBNathanael#5078 from the Parsec Discord: Helped all throughout the project. We bounced ideas off each other. He helped me visualize things. Most notably he helped with the power circuit planning and gave me a visual diagram of how to hook it all up.
  - My dad: for soldering the power circuit for me.
  - My pastor: for 3D prining my case over and over as we tweaked the design and dialed in the tollerances.
  - @Rysha#1207 from Parsec and the Parsec Discord: for helping me troubleshoot issues on my Pi with Parsec and my Joy-Cons.
  - [Kane York (riking)](https://github.com/riking/joycon): for developing (and continuing to develope) the Joy-Con driver I'm using.
  - [Pimoroni Ltd (pimoroni)](https://github.com/pimoroni/python-multitouch): for making the touchscreen driver I'm using.
  - [Rob Jones (craic)](https://github.com/craic/pi_power): for making the power solution I'm using.
  - Raspbery Pi Foundation: for making a small mobile computing solution that worked out wonderfully.
  - Parsec: for building the practically magic streaming solution that has such low latency to make the experience near flawless.
  - Nintendo: for making the Joy-Cons that power an awesome single player and even 2-player experience.
  - Microcenter: for selling me most of my hardware at a good price.
  - Adafruit: for selling me the smaller bits at a reasonable quantity and price.
  - Amazon: for selling me the last few parts I needed and shipping them quickly.
  - Best Buy: for having the Joy-Cons in stock! Also for having an SD card that works with the Pi.

## Hardware
  - [Raspberry Pi 2B](http://www.microcenter.com/product/473292/Raspberry_Pi_2_Model_B)
  - [Raspberry Pi Micro USB Power Supply 5V1 2.5A - White](http://www.microcenter.com/product/462652/Micro_USB_Power_Supply_5V1_25A_-_White)
  - [SanDisk - Ultra PLUS 32GB microSDHC UHS-I (SDSQUSC-032G-ANCIA)](http://www.bestbuy.com/site/sandisk-ultra-plus-32gb-microsdhc-uhs-i-memory-card-gray-red/3142635.p?skuId=3142635)
  - [Official Raspberry Pi 7" Touch Screen LCD](http://www.microcenter.com/product/462658/7_Touch_Screen_LCD)
  - [Edimax AC1200-nano Wi-Fi USB Adapter](https://www.amazon.com/gp/product/B01MY7PL10/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)
  - [Plugable USB Bluetooth 4.0 Low Energy Micro Adapter](https://www.amazon.com/gp/product/B009ZIILLI/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
  - [Nintendo Switch - Joy-Con Charging Grip](https://www.amazon.com/gp/product/B01N33MFPK/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
  - [Nintendo - Joy-Con (L/R) Wireless Controllers](http://www.bestbuy.com/site/nintendo-joy-con-l-r-wireless-controllers-for-nintendo-switch-gray/5730705.p?skuId=5730705)
  - [PowerBoost 1000 Charger - Rechargeable 5V Lipo USB Boost @ 1A - 1000C](https://www.adafruit.com/product/2465)
  - [Adafruit Perma-Proto Half-sized Breadboard PCB - Single](https://www.adafruit.com/product/1609)
  - [MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://www.adafruit.com/product/856)
  - [1N4001 Diode - 10 pack](https://www.adafruit.com/product/755)
  - [Diffused RGB (tri-color) LED - Common Anode](https://www.adafruit.com/product/159)
  - [0.1uF ceramic capacitors - 10 pack](https://www.adafruit.com/product/753)
  - [Through-Hole Resistors - 100K ohm 5% 1/4W - Pack of 25](https://www.adafruit.com/product/2787)
  - [Through-Hole Resistors - 10K ohm 5% 1/4W - Pack of 25](https://www.adafruit.com/product/2784)
  - [E-Projects 10EP514330R 330 Ohm Resistors, 1/4 W, 5% (Pack of 10)](https://www.amazon.com/gp/product/B00CVZ4134/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
  - [E-Projects 10EP5146K80 6.8k Ohm Resistors, 1/4 W, 5% (Pack of 10)](https://www.amazon.com/gp/product/B00CVZ4CLU/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)
  - 2 x [Schmartboard Inc. 9" Male to Female Jumper Wires with Headers](http://www.microcenter.com/product/420048/9_Male_to_Female_Jumper_Wires_with_Headers)
  - [Kingwin 80 Piece Assorted Notebook Replacement Screw Kit](http://www.microcenter.com/product/429404/80_Piece_Assorted_Notebook_Replacement_Screw_Kit)
  - Some M3 screws... (TODO)
  - [Tactile Switch Buttons (6mm tall) x 10 pack](https://www.adafruit.com/product/1490) <-- I don't recommend these for how I mounted mine
  - Solder
  - Soldering Iron
  - Hot glue stick
  - Hot glue gun
  - Industrial strength velcro
  - HDMI cable
  - Ethernet cable for initial setup
  - TV or monitor with HDMI input for initial setup

## Software
  - [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/)
  - [Etcher](https://etcher.io/)
  - You'll get the rest of it from this repo. After running the scripts from this repo, you'll be completely set up.

## Setting up the hardware
1. 3D print this case
1. Place screen into 3D printed housing
1. Connect the touchscreen to the Pi by ribbon cable
1. Connect a 5V GPIO pin to the 5V pin on the touchscreen
1. Connect a ground GPIO pin to the ground pin on the touchscreen

## Setting up the software
DISCLAIMER: If you deviated from the hardware listed above, mainly the touchscreen and wifi adapter, this won't work and you'll be on your own. I rely on a touchscreen driver for that specific touchscreen and a wifi driver for that specific dongle. Also, the bluetooth adapter I used is plug-and-play. If you choose a different one, and it's not plug-and-play or doesn't find the Joy-Cons, you're on your own.

1. Download the latest Raspbian Lite image.
1. Download Etcher
1. Write the latest Raspbian Lite image to your SD card with Etcher.
1. Plug in SD card to Pi
1. Plug in ethernet cable into Pi
1. Plug in HDMI cable to Pi and TV
1. Plug in Pi AC adapter to turn on the Pi
1. Log in to the Pi with username: `pi`, password: `raspberry`
1. Run `sudo raspi-config`
   1. Change password
   1. Change hostname if you want
   1. Change locale/timezone/keyboard/wifi region in Localisation
   1. Enable ssh in Interfacing
   1. Disable terminal, enable hardware for Serial in Interfacing
1. Run `sudo apt-get install -y git`
1. Run `git clone https://github.com/drew-wallace/switchberry.git`
1. Run `mv switchberry/* ./`
1. Run `chmod +x 1-setup`
1. Run `sudo ./1-setup`
1. When the Pi comes back to the login screen, login
1. Run `chmod +x ./2-wifi`
1. Run `sudo ./2-wifi`
1. When the Pi comes back to the login screen, login
1. Run `chmod +x ./3-touchscreen`
1. Run `sudo ./3-touchscreen`
1. Run `chmod +x ./4-joycons`
1. Run `sudo ./4-joycons`
1. Run `chmod +x ./5-desktop`
1. Run `sudo ./5-desktop`
1. Disconnect the HDMI cable.
1. When the Pi comes back on, it should load the Desktop environment. Open a terminal and run `chmod +x ./6-parsec`
1. Run `sudo ./6-parsec username password` where `username` is your e-mail you sign into Parsec with, and password is your Parsec password
1. For both Joy-Cons:
   1. Long press the Joy-Con sync button until the LEDs start to flash back and forth
   1. Touch the Bluetooth Icon on the taskbar
   1. Touch the Joy-Con entry in the list when it pops up and pair it
1. Touch the network icon in the taskbar
1. Touch your WiFi access point
1. Double tap the Keyboard shortcut on the Desktop
1. Enter your WiFi access point password
1. Touch Ok
1. Disconnect the ethernet cable

You should now be completely set up.
