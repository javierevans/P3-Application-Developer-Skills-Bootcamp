# Castle Chess Tournament Manager

## Overview

The Castle Chess Tournament Manager is a Python console application that allows chess clubs to manage tournaments from start to finish. The application works completely offline and stores all club, player, and tournament data using JSON files.

## Features

- Create and manage chess tournaments
- Register players from existing clubs
- Generate first-round pairings
- Automatically generate pairings for future rounds
- Record match results
- Update player scores automatically
- Display tournament standings
- Generate tournament reports
- Save and load tournament data using JSON
- Run completely offline

---

## Project Structure

```
commands/
data/
models/
screens/
manage_clubs.py
requirements.txt
README.md
```

- **commands/** – Handles application commands.
- **models/** – Contains the Player, Match, Round, Tournament, and Club classes.
- **screens/** – Contains the user interface screens.
- **data/** – Stores club and tournament JSON files.

---

## Requirements

- Python 3.10 or newer
- pip

---

## Installation

Clone the repository:

```bash
git clone https://github.com/javierevans/P3-Application-Developer-Skills-Bootcamp.git
```

Move into the project directory:

```bash
cd P3-Application-Developer-Skills-Bootcamp
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Program

Run the application from the project directory:

```bash
python manage_clubs.py
```

---

## Running Flake8

To check the project for PEP 8 compliance:

```bash
python -m flake8 models commands screens manage_clubs.py
```

---

## Generating the Flake8 HTML Report

Install flake8-html if it is not already installed:

```bash
pip install flake8-html
```

Generate the report:

```bash
python -m flake8 models commands screens manage_clubs.py \
--format=html \
--htmldir=flake8_report
```

After the command finishes, open:

```
flake8_report/index.html
```

to view the report.

---

## Technologies Used

- Python
- JSON
- Object-Oriented Programming (OOP)
- Command Pattern
- MVC-inspired architecture
- Flake8
- flake8-html

---

## Author

**Javier Evans**

GitHub:
https://github.com/javierevans/P3-Application-Developer-Skills-Bootcamp
