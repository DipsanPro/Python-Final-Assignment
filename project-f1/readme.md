# F1 Timing Board

This project is a Python application that processes F1 lap timing data and displays various statistics about the drivers and their performance.

## Features

- Display all fastest laps
- Display overall average lap time
- Display driver averages
- Display results with driver names and teams
- Display lap counts

Ensure you have the required files in the files-f1 directory:
f1_drivers.txt: Contains driver information (code, name, team)
Timing files (e.g., lap_times_1.txt): Contains lap timing data

## Usage

Run the main.py script with a timing file as an argument:

Example:

python ./project-f1/main.py ./files-f1/lap_times_1.txt

## Output
    After running the script, you will be presented with a menu to choose from various options. 
    Depending on your choice, the script will display:

    -All fastest laps for each driver
    -Overall average lap time
    -Average lap times for each driver
    -Detailed results including driver names, teams, fastest lap, and average 
        lap  time
    -Lap counts for each driver
The location of the race will also be displayed in the results.

Thank You.