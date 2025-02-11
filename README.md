<div align="center">
  <img src="https://github.com/user-attachments/assets/00e6cad9-4dcc-4454-9a39-38356f746a48" alt="Python Logo" height="100">
</div>

# Python Mini Projects

A collection of simple and fun Python projects designed for beginners and enthusiasts to enhance their programming skills. Each project focuses on a specific concept or application, providing hands-on learning and practical implementation of Python.

## Table of Contents

- [Projects](#projects)
  - [1. Guess The Number](#1-guess-the-number)
  - [2. Password Generator](#2-password-generator)
  - [3. QR Code Generator](#3-qr-code-generator)
  - [4. Rock Paper Scissors](#4-rock-paper-scissors)
  - [5. Slot Machine Game](#5-slot-machine-game)
  - [6. Weather App](#6-weather-app)
  - [7. Pokedex](#7-pokedex)
- [Technologies Used](#technologies-used)
- [How to Run](#how-to-run)
- [License](#license)

## Projects

### 1. Guess The Number

A number guessing game where the computer randomly selects a number between 1 and 100, and the player attempts to guess it.

**Features:**
- Provides hints for smaller or larger guesses.
- Tracks the number of attempts.

**File:** `GuessTheNumber.py`

---

### 2. Password Generator

A terminal-based tool to generate secure passwords of user-defined lengths using random characters.

**Features:**
- Supports letters, digits, and special characters.
- Validates password length input.

**File:** `PasswordGenerator.py`

---

### 3. QR Code Generator

A tool to generate a QR code from user-provided data and save it as an image file.

**Features:**
- Customizable QR code with color settings.
- Generates high-quality QR code images.

**File:** `QRcodeGenerator.py`

---

### 4. Rock Paper Scissors

A fun implementation of the classic Rock-Paper-Scissors game, where the user competes against the computer.

**Features:**
- Real-time comparison of choices.
- Displays results (Win, Lose, Tie).

**File:** `RockPaperScissor.py`

---

### 5. Slot Machine Game

A simple slot machine game where users bet virtual money and spin the reels to test their luck.

**Features:**
- Allows players to add money and place bets.
- Tracks balance and evaluates wins or losses.

**File:** `SlotGame.py`

---

### 6. Weather App

A terminal-based application that fetches and displays current weather data for a specified location.

**Features:**
- Displays temperature, humidity, and weather description.
- Uses an API to fetch real-time data.

**File:** `WeatherApp.py`

---
### 7. Pokedex

A terminal-based tool that fetches information about any Pokémon by name or ID using the PokéAPI.

**Features:**
- Fetches and displays Pokémon details such as types, abilities, stats, and moves.
- Allows users to customize the number of moves displayed.
- Provides links to Pokémon sprite images.

**File:** `Pokedex.py`

---

## Technologies Used

- **Python**: The core programming language for all projects.
- **Libraries**:
  - `random`: For generating random numbers and selections.
  - `string`: For handling character sets.
  - `qrcode`: For creating QR codes.
  - `requests`: For making API calls.
  - `datetime`: For working with dates and times.

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/CodeCraftAyan/Python-Mini-Projects.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Python-Mini-Projects
   ```
3. Run the desired Python file using:
   ```bash
   python <filename>.py
   ```

**Note:** For the Weather App, replace the `api_key` variable with your OpenWeather API key.
**Note:** For the Pokedex, ensure you have an active internet connection to access the PokéAPI.
