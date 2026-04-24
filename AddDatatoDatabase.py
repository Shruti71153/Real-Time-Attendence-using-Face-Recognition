import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realtimeattendence-d4775-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2105088":
        {
            "name": "Rohan",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    "2105105":
        {
            "name": "Ankit",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    "2105766":
        {
            "name": "Ajay",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    "2105821":
        {
            "name": "Samudrneel",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 5,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    "21051663":
        {
            "name": "Mrighanshu",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    "2105001":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2016,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)