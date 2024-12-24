# Football Player Management System

This project is a simple football player management system that allows coaches to add, search, delete, and edit player information stored in a CSV file. Fans can only search for player information.

## Features

- **Add Player**: Coaches can add a new player's information including backnumber, name, team, and age.
- **Search Player**: Both coaches and fans can search for a player by backnumber, name, team, or age.
- **Delete Player**: Coaches can delete a player's information by backnumber.
- **Edit Player**: Coaches can edit a player's information by backnumber.

## Requirements

- Python 3.x
- `csv` module
- `replit` module
- `prettytable` module

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run the `finalproject.py` script.

```bash
python finalproject.py
```

## How to Use

### As a Coach

1. Start the program and enter `yes` when prompted.
2. Select `coach` and enter the password `2135647`.
3. Choose an action: add, search, delete, or edit a player.
4. Follow the prompts to complete the action.

### As a Fan

1. Start the program and enter `yes` when prompted.
2. Select `fan`.
3. Choose to search for a player by backnumber, name, team, or age.
4. Enter the search criteria to view the player's information.

## CSV File Format

The player information is stored in a CSV file named `About_player.csv` with the following columns:

- `backnumber`
- `name`
- `team`
- `age`

Example:

```plaintext
backnumber,name,team,age
1,son,spar,29
4,harry,spar,25
4,Arker,Myanmar,29
2,messi,psg,39
5,Son,Brazil,23
```

## License

This project is licensed under the MIT License.