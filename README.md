# Voice-Controlled Virtual Assistant

## Overview

This project is a voice-controlled virtual assistant that can perform various tasks and answer questions. It uses speech recognition and text-to-speech technology to provide a conversational experience.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functionalities](#functionalities)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Voice-controlled virtual assistants are becoming increasingly popular for their convenience and hands-free operation. This project implements a virtual assistant that can respond to voice commands and provide information on various topics.

## Features

- Voice recognition and synthesis using the `speech_recognition` and `win32com` libraries.
- Ability to answer questions, provide news updates, and perform web searches.
- Open websites, lock the computer, and create text files through voice commands.

## Requirements

To run this project, you will need the following:

- Python 3.x
- Required libraries: `requests`, `json`, `datetime`, `wikipedia`, `webbrowser`, `pyautogui`, `speech_recognition`, `win32com`, `playsound`, `random`

You can install the required libraries using `pip`:

## Installation

1. Clone this repository to your local machine:
2. 
```bash
git clone https://github.com/shukur-alom/Assistant.git
```

2. install requirements

```bash
pip3 install -r requirements.txt
```

## Usage
1. Make sure your microphone and speakers are properly set up and working.
2. Run the Python script:

```bash
python Assistant.py
```
3. Start interacting with the virtual assistant by speaking voice commands. You can ask questions, request news updates, open websites, and more.

## Functionalities
* Personal Information: The assistant can provide information about you, your name, and family members.

* News Updates: Ask for the latest news updates, and the assistant will read headlines from a news API.

* Date and Time: Request the current date and time.

* Open Websites: Instruct the assistant to open websites like YouTube, Facebook, or GitHub.

* Lock Computer: Lock your computer with a voice command.

* Create Text Files: Dictate text, and the assistant will create a text file with the specified content.

* Search on Wikipedia: Ask questions or request information on various topics using Wikipedia.

* Unknown Commands: If the assistant doesn't understand a command, it logs the request to a file for future reference.


** License
This project is licensed under the MIT License - see the [MIT LICENSE](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
