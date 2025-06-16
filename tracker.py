#!/usr/bin/env python3
import argparse
from datetime import datetime
from dateutil import parser as date_parser
from database import Database

def parse_datetime(date_str, time_str):
    """Combine date and time strings into a datetime object."""
    return date_parser.parse(f"{date_str} {time_str}")

def add_entry(args):
    """Add a new time entry."""
    try:
        date = parse_datetime(args.date, "00:00")
        start_time = parse_datetime(args.date, args.start)
        end_time = parse_datetime(args.date, args.end)

        if end_time <= start_time:
            print("Error: End time must be after start time")
            return

        db = Database()
        entry_id, hours = db.add_time_entry(date, start_time, end_time)
        print(f"Added time entry: {date.date()} - {hours:.2f} hours")

    except ValueError as e:
        print(f"Error: Invalid date or time format - {e}")
    except Exception as e:
        print(f"Error: {e}")

def list_entries(args):
    """List all time entries."""
    try:
        db = Database()
        entries = db.get_all_entries()
        
        if not entries:
            print("No time entries found.")
            return

        print("\nTime Entries:")
        print("-" * 50)
        print(f"{'Date':<12} {'Start':<8} {'End':<8} {'Hours':<8}")
        print("-" * 50)
        
        for entry in entries:
            start_dt = datetime.strptime(entry['start_time'], '%Y-%m-%d %H:%M')
            end_dt = datetime.strptime(entry['end_time'], '%Y-%m-%d %H:%M')
            print(f"{entry['date']:<12} "
                  f"{start_dt.strftime('%H:%M'):<8} "
                  f"{end_dt.strftime('%H:%M'):<8} "
                  f"{entry['hours']:.2f}")
        
        total_hours = db.get_total_hours()
        print("-" * 50)
        print(f"Total hours: {total_hours:.2f}")

    except Exception as e:
        print(f"Error: {e}")

def clear_database(args):
    """Clear all entries from the database."""
    try:
        db = Database()
        db.clear_database()
        print("All time entries have been cleared from the database.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Time Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a time entry")
    add_parser.add_argument("--date", required=True, help="Date (YYYY-MM-DD)")
    add_parser.add_argument("--start", required=True, help="Start time (HH:MM)")
    add_parser.add_argument("--end", required=True, help="End time (HH:MM)")

    # List command
    subparsers.add_parser("list", help="List all time entries")

    # Clear command
    subparsers.add_parser("clear", help="Clear all time entries from the database")

    args = parser.parse_args()

    if args.command == "add":
        add_entry(args)
    elif args.command == "list":
        list_entries(args)
    elif args.command == "clear":
        clear_database(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 