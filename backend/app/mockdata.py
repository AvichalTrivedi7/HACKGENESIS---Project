# Minimal mock data for demo
students = {
"2023001": {
"name": "Riya Sharma",
"role": "student",
"library": ["AI Handbook (Due: Sept 30)", "Maths II (Due: Sept 30)"],
"exams": ["DSA - Oct 10", "DBMS - Oct 15", "OS - Oct 20"],
"courses": ["DSA", "DBMS", "OS", "AI"],
"grades": {"DSA": "A", "DBMS": "B+", "OS": "A-", "AI": "A"},
"notifications": ["ERP updated with exam schedule", "Library dues pending"]
},
"2023002": {
"name": "Aman Verma",
"role": "student",
"library": ["Networks (Due: Sept 28)"],
"exams": ["ML - Oct 12", "Stats - Oct 16"],
"courses": ["ML", "Stats", "Networks"],
"grades": {"ML": "A-", "Stats": "B", "Networks": "B+"},
"notifications": ["Fee payment due", "Library: Networks book due soon"]
}
}


admins = {
"admin1": {
"name": "Prof. Gupta",
"role": "admin",
"permissions": ["view_all_students", "update_announcements"]
}
}