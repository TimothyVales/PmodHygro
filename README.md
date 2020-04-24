# PmodHygro

## Get Started
If you already have your Jupyter Notebook opened follow these steps:
On the right side of the screen, click on "New", and open a new terminal. Pip install the repo containing the code from my github using this command. 

```sh
sudo pip3 install git+https://github.com/TimothyVales/PmodHygro.git
```

## Instrument Maintenance
One of the most important aspects of playing an instrument, besides actually making music, is taking proper care of your instrument. After playing the viola for almost 12 years, I've realized that my instrument played best when I made sure to control as many environmental variables as I could. Two of those variables, humidity and temperature, affect almost every aspect of an instrument's performance (tone, color, etc), and will be the driving force behind this project. 

First, I need a way to monitor the humidity and temperature, not only in my apartment, but also within the instrument case to make sure that they are staying within acceptable ranges. I use the Pynq-Z2 because of its Pmod ports, and because of its, relatively, small size. Second, I need a sensor that will grab this specific type of information, and for that, I found the Pmod Hygro. This small sensor contains a TI HDC1080, which will measure the relative temperature and humidity of its environment. Lastly, I need a way to display this information in real time to watch trends as the day goes by, and to see any anomalies that may need remedying immediately. 
I hope that this project can serve as a thorough introduction on how to get Pynq started, and will help future developers create their own projects! 

![Full Project](https://github.com/TimothyVales/PmodHygro/blob/master/Full_board_setup.jpg)

## Setup - Install and Boot Pynq v2.5 Image
Go to the Pynq website, pynq.io, and grab the pynq v2.5 for the Pynq-Z2 board under the "Boards" tab. 
Using Balena Etcher, write the pynqv2.5 image onto the SD card in your SD port.

![Balena UI](https://github.com/TimothyVales/PmodHygro/blob/master/Balena.JPG)

Wait for the process to finish and validate, then, safely, eject the SD card from your laptop, and insert the micro SD card onto the Pynq-Z2 board as shown. 

![SD Card Location](https://github.com/TimothyVales/PmodHygro/blob/master/SD_Card.jpg)

Connect the microUSB and ethernet cables from your board to your laptop. 
Make sure everything is connected properly, and turn on the board. After a couple of seconds, open any web browser (I use Google Chrome), and type in "pynq:9090". This will open up the Jupyter Notebook. 

![Jupyter NB](https://github.com/TimothyVales/PmodHygro/blob/master/JupyterNB.JPG)

## How the Code Works
To fully utilize Jupyter Notebook, I have documented every aspect of the aspect using Jupyter Notebooks Markup feature. I will explain some things in this section that would be better explained here than on the notebook itself. 
To write and run your own code follow these steps:
1) Click on the cell at the very top of the page
2) Click "Run", and this will auto-increment which cell is selected to the next cell
3) A cell is finished when there is a number in the bracket to the left of the code, so wait until after a cell is finished to run the code below it
4) Continue doing this until you have compiled everything
How to Setup Hardware
Insert the Pmod Hygro into the lower row of Pmod A as seen in these pictures! 

![Pmod Top](https://github.com/TimothyVales/PmodHygro/blob/master/Pmod_top.jpg)

![Pmod Side](https://github.com/TimothyVales/PmodHygro/blob/master/Pmod_side.JPG)

The Pmod can, technically, be place on any Pmod Port and on any row, but for this project and for how the code is written, I placed mine this way. 
 
Good luck on using the Pynq-Z2, and I hope to see all your great projects! Leave a comment on what you think about this project, and if there are things I should change/work on for my next project! 
