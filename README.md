# Student-performance-analyser

A Flask application for predicting student performance, tracking student prediction history, and generating staff reports.

## Setup

Use Python 3. Install dependencies and start the application from this directory:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

The trained model is included at `models/student_model.pkl`. To retrain it from the included dataset, run `python train_model.py`.

## Staff account

For a new local database, configure `STAFF_PASSWORD` before starting the application to create the initial staff account. Optionally set `STAFF_EMAIL` and `STAFF_ID`; the email defaults to `staff@college.com` and the ID to `STAFF001`. The password must be supplied through the environment and is never stored in the repository. Set `SECRET_KEY` to a long, random value for a stable session key; if it is omitted, the application generates a temporary key at startup.

The SQLite user database and prediction history are created locally and intentionally excluded from version control.
