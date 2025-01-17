# Scrape-Calendar-Data

![GitHub release (latest by date)](https://img.shields.io/github/v/release/goffstown-sports-app/Scrape-Calendar-Data) ![GitHub repo size](https://img.shields.io/github/repo-size/goffstown-sports-app/Scrape-Calendar-Data) ![GitHub contributors](https://img.shields.io/github/contributors/goffstown-sports-app/Scrape-Calendar-Data)

## Docker Images

![Docker Pulls](https://img.shields.io/docker/pulls/ghsapp/scrape-calendar-data)

| Tag:   | Arch:   | Description:                      |
| ------ | ------- | --------------------------------- |
| latest | x86     | Latest docker image built         |
| arm    | arm32v7 | Latest docker image built for arm |

## Github Actions

| Action                                                                                                                                                                                      | Action Description                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [![Actions Status](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/workflows/Python-Versions/badge.svg)](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/actions) | Testing for Python 3.6, 3.7, and 3.7-dev |
| [![Actions Status](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/workflows/Docker/badge.svg)](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/actions)          | Testing Docker images                    |
| [![Actions Status](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/workflows/Python-Cron/badge.svg)](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/actions)     | Cron job for the Python-Versions action  |
| [![Actions Status](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/workflows/Docker-Cron/badge.svg)](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/actions)     | Cron job for the Docker action           |
| [![Actions Status](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/workflows/Docker-Hub/badge.svg)](https://github.com/goffstown-sports-app/Scrape-Calendar-Data/actions)      | Pushing Image to Docker Hub              |

## Services

| Service Name | Badge                                                                                                                                                                                                                                                                                           | Description                          |
| -----------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
|         Synk | [![Known Vulnerabilities](https://snyk.io/test/github/goffstown-sports-app/Scrape-Calendar-Data/badge.svg)](https://snyk.io/test/github/goffstown-sports-app/Scrape-Calendar-Data)                                                                                                              | Security Monitoring for dependencies |
|       Codacy | [![Codacy Badge](https://api.codacy.com/project/badge/Grade/79e012cb6bc4425ba829dd60aa517c87)](https://app.codacy.com/app/matthewgleich/Scrape-Calendar-Data?utm_source=github.com&utm_medium=referral&utm_content=goffstown-sports-app/Scrape-Calendar-Data&utm_campaign=Badge_Grade_Settings) | Cloud based linter                   |

## Description

This application scrapes the [Goffstown Athletics Calendar](https://goffstownathletics.com/main/calendar/) for event information and uploads it to the database. It uploads this data so the Raspberry Pi getting information from the scoreboard knows if there is an event going on at the field - i.e. should it be recording or not. This program is currently running in a Docker container on a Raspberry Pi.

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

If you are using docker, then run:

`docker-compose up -d`

