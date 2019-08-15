# Scrape-Calendar-Data

## Services

| Service Name | Badge                                                                                                                                                                                                                                                                                           | Description                   |
|-------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Synk         | [![Known Vulnerabilities](https://snyk.io/test/github/goffstown-sports-app/Scrape-Calendar-Data/badge.svg)](https://snyk.io/test/github/goffstown-sports-app/Scrape-Calendar-Data)                                                                                                              | Security Monitoring           |
| Travis CI    | [![Build Status](https://travis-ci.com/goffstown-sports-app/Scrape-Calendar-Data.svg?branch=master)](https://travis-ci.com/goffstown-sports-app/Scrape-Calendar-Data)                                                                                                                           | Continous Integration Service |
| Codacy       | [![Codacy Badge](https://api.codacy.com/project/badge/Grade/79e012cb6bc4425ba829dd60aa517c87)](https://app.codacy.com/app/matthewgleich/Scrape-Calendar-Data?utm_source=github.com&utm_medium=referral&utm_content=goffstown-sports-app/Scrape-Calendar-Data&utm_campaign=Badge_Grade_Settings) | Cloud based linter            |

## Description

The scrape calendar data application it made to upload event information to the database. It need to upload this data so the Raspberry Pi connected to the scoreboard knows if there is an event going on at the field. The program will run in either the Google cloud using cloud computing or on a local server.

## Features

Below is a list of all the features of this program:

1. Scrape data from the calendar on Goffstown's athletic website.
2. Upload that data to Firebase Realtime database.

## Requirements

To see working python version look at the .travis.yml
Install the requirements by doing the following:
`pip install -r requirements.txt`

## Usage

Once you have installed the requirements, you can now run the program! You run the program by inputting the following command once you are in the src folder:

`python main.py`

## Contributors

* [Matthew Gleich](https://github.com/Matt-Gleich) (@Matt-Gleich)
