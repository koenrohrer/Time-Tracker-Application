from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from dateutil import parser
from database import Database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    db = Database()
    
    if request.method == 'POST':
        if 'clear' in request.form:
            db.clear_database()
            return redirect(url_for('index'))
            
        try:
            date = parser.parse(request.form['date'])
            start_time = parser.parse(f"{request.form['date']} {request.form['start']}")
            end_time = parser.parse(f"{request.form['date']} {request.form['end']}")
            
            if end_time <= start_time:
                return "Error: End time must be after start time", 400
                
            db.add_time_entry(date, start_time, end_time)
            return redirect(url_for('index'))
        except Exception as e:
            return f"Error: {str(e)}", 400
    
    entries = db.get_all_entries()
    weekly_total = db.get_weekly_total()
    return render_template('index.html', entries=entries, weekly_total=weekly_total)

if __name__ == '__main__':
    app.run(debug=True) 