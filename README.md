# Time Tracker

A simple web application for tracking time entries with a clean, intuitive interface. Built with Python, Flask, and SQLite.

## Features

- **Web Interface**: Clean, modern UI for easy time tracking
- **Time Entry Management**:
  - Add time entries with date, start time, and end time
  - Automatic calculation of hours
  - Clear all entries with a single click
- **Weekly Overview**:
  - Automatic calculation of weekly totals (Monday to Sunday)
  - Real-time updates when adding entries
- **Data Storage**:
  - SQLite database for reliable data persistence
  - Simple and lightweight


## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/time-tracker.git
cd time-tracker
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

### Adding Time Entries

1. In the web interface, fill out the form:
   - Select a date using the date picker
   - Enter start time (HH:MM)
   - Enter end time (HH:MM)
2. Click "Add Entry" to save the time entry
3. The entry will appear in the table below
4. The weekly total will update automatically

### Viewing Entries

- All entries are displayed in a table below the form
- Entries are sorted by date (most recent first)
- Each entry shows:
  - Date
  - Start time
  - End time
  - Total hours

### Weekly Total

- The weekly total is displayed below the entries table
- Automatically calculates hours for the current week (Monday to Sunday)
- Updates in real-time when adding new entries

### Clearing Entries

- Click the red "Clear All" button to remove all entries
- A confirmation dialog will appear to prevent accidental clearing
- The table and weekly total will update immediately

## Command Line Interface

The application also includes a command-line interface for advanced users:

### Adding Entries
```bash
python tracker.py add --date YYYY-MM-DD --start HH:MM --end HH:MM
```

Example:
```bash
python tracker.py add --date 2024-03-15 --start 09:00 --end 17:00
```

### Listing Entries
```bash
python tracker.py list
```

### Clearing Entries
```bash
python tracker.py clear
```

## Project Structure

```
time-tracker/
├── app.py              # Flask web application
├── database.py         # Database operations
├── tracker.py          # Command-line interface
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html     # Main web interface
└── time_tracker.db    # SQLite database (created on first run)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Uses [SQLite](https://www.sqlite.org/) for data storage
- Styled with modern CSS 
