# Rock-paper-scissors-exercise

A Python application to play Rock, Paper, Scissors against the computer.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip
  + Python-dotenv

## Installation

Fork this [remote repository](https://github.com/mdv5/my-first-python-app) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment, perhaps called "rock-paper-scissors-exercise":

```sh
conda create -n rock-paper-scissors-exercise python=3.8
conda activate rock-paper-scissors-exercise
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    PLAYER_NAME="Mike"

## Usage

Run the game script:

```py
python app/game.py
```

## General game rules
Follow the in-game prompts to play the game.

+ Rock crushes scissors, rock wins against scissors
+ Paper covers rock, paper wins against rock
+ Scissors cuts paper, scissors wins against paper

If the player and computer make the same choice, the game ends in a tie.
