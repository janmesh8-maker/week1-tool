# Study Session Advisor

Study Session Advisor is a simple Python command-line program that helps students decide what type of study session they can have based on the amount of time available.

The program validates the user's input and recommends a quick review, focused study session, deep study session, or a longer study session with breaks.

## Setup

Create a virtual environment:

    python -m venv .venv

Activate it on Windows:

    .venv\Scripts\activate

Install the requirements:

    pip install -r requirements.txt

## Run

Run the program using:

    python study_advisor.py

## Example

    How many minutes do you have available to study? 90
    You have 90 minutes available. Recommendation: Deep study session.

## Known Limitations

The program only accepts whole numbers between 1 and 480 minutes. It does not create a detailed study schedule or track completed study sessions.