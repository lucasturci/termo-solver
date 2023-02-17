# Termo Puzzle Solver

This repository contains an app that solves the "Termo" web hosted puzzle game using Selenium and is containerized with Docker and Docker Compose. Termo is hosted in (https://term.ooo), and is a brazilian version of the famous wordle game. After solving the current day's word, this app also pushes it to a database used for storing each day solutions, which then is read by http://sougaia.com/termo, a clone of the game where you can play any day's word

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lucasturci/termo-puzzle-solver.git
    ```

2. Build the Docker image:
    
    ```bash
    cd termo-puzzle-solver
    docker build -t termo-puzzle-solver .
    ```

## Usage

To run the app, use Docker Compose:

```bash
docker-compose up
```

This will start the app, which will then solve the Termo puzzle game and output the solution to the console.

Note: To push to the database, you must have the credentials in a `./database-credentials.json` file. For just solving the app, you can ignore the raised exception (*TODO: Implement a flag to update to database*)

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.