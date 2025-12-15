## DevOps Python Mini Projects

This repository contains three small Python scripts that cover common DevOps use cases. These scripts are written in a simple and readable way and can be easily understood and modified by beginners.

## Q1. Password Strength Checker
Description

In DevOps, security is very important, and one of the basic security practices is using strong passwords. This script checks whether a given password meets standard strength requirements.

## Features

Checks minimum password length (at least 8 characters)

Verifies presence of both uppercase and lowercase letters

Ensures at least one digit (0–9)

Ensures at least one special character (such as ! @ # $ %)

Returns a boolean result and gives clear feedback to the user

## How It Works

The script defines a function called check_password_strength() which takes the password as input and validates it against the defined rules. The user is prompted to enter a password, and the script displays whether the password is strong or weak along with the reason.

## screenshot

<img width="297" height="47" alt="password_check screenshot" src="https://github.com/user-attachments/assets/23d2ef51-6e80-437f-99b2-192515c1781a" />



## Q2. CPU Health Monitoring Script
## Description

As a DevOps engineer, monitoring system health is a routine task. This script continuously monitors CPU usage and raises an alert when the usage crosses a defined threshold.

Features

Continuously checks CPU usage of the local system

Displays an alert if CPU usage exceeds 80%

Runs indefinitely until manually stopped

Includes basic error handling to avoid script crashes

## Prerequisites

The script uses the psutil library. Install it using:

pip install psutil
How It Works

The script uses psutil.cpu_percent() inside a loop to fetch CPU usage. If the usage goes beyond the threshold, an alert message is printed on the console.

## screenshot

<img width="278" height="140" alt="cpu_usage_scrrenshot" src="https://github.com/user-attachments/assets/9125603f-6382-4b36-9008-67d8d42c709d" />


<img width="362" height="223" alt="cpu_load_screenshot" src="https://github.com/user-attachments/assets/5d94d6ea-9804-460f-811c-c3986144ac0f" />


## Q4. File Backup Script
## Description

Regular backups are essential in DevOps to prevent data loss. This script copies files from a source directory to a destination directory and ensures file name uniqueness.

Features

Takes source and destination directories as command-line arguments

Copies all files from source to destination

Appends a timestamp if a file with the same name already exists

Handles errors such as missing directories

## Script Name

backup.py

## Usage
python backup.py /path/to/source /path/to/destination
How It Works

The script checks if both source and destination directories exist. While copying files, it verifies whether a file with the same name already exists in the destination. If it does, a timestamp is added to the file name before copying.

## Screenshot

<img width="1450" height="145" alt="backup_screenshot" src="https://github.com/user-attachments/assets/7ef92265-fa56-4002-a9ab-5df475208c9c" />

