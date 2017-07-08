# The SwitchBerry Setup Guide
The SwitchBerry is a mobile PC game streaming device inspired by the Nintendo Switch and made from a Raspberry Pi. The goal was to play my PC games on the go, mouse and keyboard free, with little to no latency, and a steady frame rate.

## Table of Contents
  - [Credits](#credits)
  - [Media](#media)
  - [Hardware](#hardware)
  - [Software](#software)
  - [Setting Up the Hardware](#setting-up-the-hardware)
  - [Setting Up the Software](#setting-up-the-software)
  - [How to use](#how-to-use)
  - [The Story](#the-story)
  - [Donate](#donate)

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
  - @benjy_parsec#6335 the CEO of Parsec: for his generosity, encouragement, and availability to help.
  - Raspbery Pi Foundation: for making a small mobile computing solution that worked out wonderfully.
  - Parsec: for building the practically magic streaming solution that has such low latency to make the experience near flawless.
  - Nintendo: for making the Joy-Cons that power an awesome single player and even 2-player experience.
  - Microcenter: for selling me most of my hardware at a good price.
  - Adafruit: for selling me the smaller bits at a reasonable quantity and price.
  - Amazon: for selling me the last few parts I needed and shipping them quickly.
  - Best Buy: for having the Joy-Cons in stock! Also for having an SD card that works with the Pi.

## Media
  - [Pictures](https://drive.google.com/drive/folders/0BwfA42Ks3I6nQzBUdE5FRTZLOUU?usp=sharing)
  - Reddit posts:
    - [First post in /r/raspberry_pi](https://www.reddit.com/r/raspberry_pi/comments/69ebmb/help_requested_for_project_piswitch/)
    - [Reveal video in /r/raspberry_pi](https://www.reddit.com/r/raspberry_pi/comments/6l95bf/the_switchberry_a_mobile_pc_gaming_device_i_made/)
    - [Reveal video in /r/gaming](https://www.reddit.com/r/gaming/comments/6l92ux/the_switchberry_a_mobile_pc_gaming_device_i_made/)
    - [Reveal of Xbox One streaming in /r/gaming](https://www.reddit.com/r/gaming/comments/6lj1z0/i_used_my_switchberry_to_make_a_handheld_xbox_one/)
  - Videos:
    - [Reveal video on YouTube](https://youtu.be/VZErsaL_Czc)
    - [Xbox One streaming video on YouTube](https://youtu.be/kBMi8Y2XeFc)

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
  - 2 x M3 screws, 3 pack
  - [Tactile Switch Buttons (6mm tall) x 10 pack](https://www.adafruit.com/product/1490) <-- I don't recommend these for how I mounted mine
  - [Velleman Assorted Breadboard Jumper Wire Set 140 Pieces](http://www.microcenter.com/product/389976/Assorted_Breadboard_Jumper_Wire_Set_140_Pieces)
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

## Setting Up the Hardware
### Note: Do software steps 1-9 first. Also, if you get confused with the layout of things, check out the pictures above.
1. 3D print [this case](https://www.thingiverse.com/thing:1503651) but exclude the screen housing
1. 3D print this [screen housing](https://www.thingiverse.com/thing:2336532)
1. Place screen into 3D printed housing
1. Secure L backets with 4 M3 screws, flat side facing outward, over the holes on the 3D printed screen housing
1. Unscrew the screws from the riser screws on the touchscreen driver board and set them aside.
1. Replace the bottom right riser screw with one of the scres from the previous step from the touchscreen driver. This is so it doesn't poke the battery
1. Remove the top right riser screw.
1. On your permaboard, create [this circuit](https://github.com/craic/pi_power) from the parts you have (TODO: insert diagram here). You may wish to use a temporary breadboard for testing purposes so you don't have to go through the hassle of desoldering if you messed up. Read ahead to figure out where to place the attached components
1. The button is going to go right outside the case next to the Powerboost 1000C. It will be secured with velcro. There should be a hole, if not it was probably just filled in during the 3D printing process and you can clear it out with a knife
1. You may need to hot glue around the LED leads if it's exposed
1. Place the completed permaboard circuit vertically next to the Pi such that the soldered components are facing the same direction as the Pi's USB ports
1. Secure the Powerboost 1000C with 1 screw from the touchscreen driver board and another from the Kingwin 80 Piece Assorted Notebook Replacement Screw Kit
1. Secure the pi in place with 2 screws from the touchscreen driver board
1. Place a strip of velcro along the wall opposite of the Powerboost 1000C
1. Place a piece of velcro on the battery and gently press the battery against the back wall
1. Connect the battery to the Powerboot 1000C
1. Place the LED between the battery and the Powerboost 1000C
1. Connect the touchscreen to the Pi by ribbon cable
1. Connect a 5V GPIO pin to the 5V pin on the touchscreen
1. Connect a ground GPIO pin to the ground pin on the touchscreen

## Setting Up the Software
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
   1. Select Finish
   1. Agree to Reboot
1. When the Pi comes back to the login screen, login
1. Run `sudo apt-get install -y git`
1. Run `git clone https://github.com/drew-wallace/switchberry.git`
1. Run `mv switchberry/* ./`
1. Run `chmod +x 1-setup`
1. Run `./1-setup`
1. When the Pi comes back to the login screen, login
1. Run `./2-wifi`
1. When the Pi comes back to the login screen, login
1. Run `./3-touchscreen`
1. Run `./4-joycons`
1. Run `./5-desktop`
1. Disconnect the HDMI cable.
1. When the Pi comes back on, it should load the Desktop environment. Tap the terminal icon
1. Run `./6-parsec username password` where `username` is your e-mail you sign into Parsec with, and password is your Parsec password
1. For both Joy-Cons:
   1. Long press the Joy-Con sync button until the LEDs start to flash back and forth
   1. Touch the Bluetooth Icon on the taskbar
   1. Tap Add Device
   1. Tap the Joy-Con entry in the list when it pops up
   1. Tap Pair
   1. Tap Ok
1. Touch the network icon in the taskbar
1. Touch your WiFi access point
1. Enter your WiFi access point password
1. Touch Ok
1. In the terminal, run `sudo reboot`

## How to use
When you turn on the SwitchBerry, you will end up on the Desktop. There are 4 shortcuts for you to double tap:
  - Keyboard: Opens the onscreen keyboard. This is helpful when connecting to a new WiFi access point
  - LCD Mode: Enables the LCD screen and disables HDMI out. Also enables sound through the headphone jack and disables sound over HDMI
  - HDMI Mode: Enables HDMI out and disables the LCD screen video. Turns the touchscreen into one large touchpad. Also enables sound through over HDMI and disables the sound through the headphone jack
  - Parsec: Starts Parsec and chooses the first available server to stream from

## The Story
I've always wanted a really cool handheld gaming device. I had a GameBoy, PSP, and Nintendo DS growing up. I really liked the PSP the most because I could mod the heck out of it but also because they had more of the kind of games I like. Then I got into consoles by playing Xbox, Xbox 360, PS3, and now Xbox One. I'm also just now diving into PC gaming. My desire for a handheld console diminished because I enjoyed competitive multiplayer games and other single player and co-op games that I knew a handheld couldn't handle (no pun intended).

One day, Microsoft announced the ability to stream the Xbox One to any Windows 10 device. I was excited! All I had to do was find a small enough tablet and I'd be good to go. But it wouldn't be the same. I'd carry around a tablet, and a controller when I already carried a Surface Pro 3. So I waited again, until I found NVIDIA Game Stream using Moonlight. They had an android app and I had an Android phone. My problem was I didn't have a gaming rig. I was planning on building one but didn't have the money yet. Again, I waited.

Finally, one day I found Parsec. Their focus was on low latency and they supported AMD, Intel, and NVIDIA. My Surface had integrated graphics so I could test it out! It was buttery smooth. I then found out they made a Raspberry Pi version. It got me thinking, could I MAKE a handheld and use this app? I needed to see what other people had done. I found different tips about which Pi to use for mobile projects, what kind of battery life to expect, what screens I could use, but the one big question was the controller. I always imagined having to split an Xbox controller in half and just mounting it on the sides of a screen. I knew that would be difficult and ugly so I was hesitant. Then I saw the Nintendo Switch Joy-Cons. I found a video of some guy playing 2-player with the Joy-Cons in RetroPie. A plan was born.

The idea that I could have a console/PC gaming experience in my hands remained a dream, until now. I went to Microcenter and bought a bunch of parts. I ordered some off Amazon as well. I grabbed the Joy-Cons from Best Buy because no one else around had them in stock at the time. Everything came together except the ability to join the Joy-Cons together as 1 controller. I tried multiple apps desigend for remapping controlls. Even the ones that advertised joining 2 devices as 1 joystick didn't work. I tried modifying the source of another app to get it to work. Nothing was working. Then I found a Joy-Con driver written by [Kane York (riking)](https://github.com/riking/joycon). After getting it to compile, it worked!

Now that it's complete I'm going to start thinking up how to make it smaller and maybe add some features. For example:
  - I want to embed the Joy-Con Charging Grip into my case so the Joy-Cons charge while on the SwitchBerry
  - I want to see if I can drop the Pi 2B for a Pi Zero, but I'm not sure if they make a DSI connector or hat for connecting with the touchscreen. This would be 100% handheld instead of having an option to "dock" it and use HDMI. I would also need a sound solution since it doesn't have a headphone jack
  - Simplify the circuitry into a PCB for space and time saving

## Donate
[Here's my Square Cash](https://cash.me/$DrewWallace). This wasn't a cheap project by any means. It's too complicated right now to sell, so if you're feeling generous, drop me some cash!

If you don't have Square Cash yet, here's a sweet deal:

Sign up using my code ([VCNTKRK](https://cash.me/app/VCNTKRK)) and we’ll each get $5 from Square Cash when you send $5. So if we do the math, you send $5 to me and Square Cash gives you and me both $5. That means I get $10 and you spent $0.