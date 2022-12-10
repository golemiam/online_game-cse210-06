# Richochet
Richochet is a game about avoiding projectiles that bounce around the screen.

## Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

python3 -m pip install raylib

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

python3 richochet 

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:

root                    (project root folder)
/-- richochet              (source code for game)
  /-- game              (specific game classes)
    /-- casting         (various actor classes)
      /--entities       (various actor classes with physics)
    /-- directing       (director and scene manager classes)
    /-- scripting       (various action classes)
      /-- art_actions   (various drawing actions)
      /-- physics       (various physics actions)
    /-- services        (various service classes)
  /-- __main__.py       (entry point for program)
  /-- constants.py      (game constants)
/-- README.md           (general info)


## Required Technologies

* Python 3.8.0
* Raylib Python CFFI 3.7

## Additional Help
In the case that the program starts but closes immediately after, make sure that the folder you have selected the program to run from is the parent folder of '__main__.py'.

## Thursday Team Members 

* Marc Rollins
* Robbie Platt
* Helaman Cristian Pinheiro Ewerton