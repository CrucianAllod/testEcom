import requests

url = 'http://web:8000/api/sendForm/'

test_data = [
    [
        {"name": "username", "value": "testuser"},
        {"name": "email", "value": "test@example.com"},
        {"name": "password", "value": "securepassword"},
        {"name": "confirm_password", "value": "securepassword"}
    ],
    [
        {"name": "username", "value": "testuser"},
        {"name": "email", "value": "invalid_email"},
        {"name": "confirm_password", "value": "differentpassword"}
    ],
    [
        {"name": "name", "value": "John Doe"},
        {"name": "email", "value": "john@example.com"},
        {"name": "message", "value": "Hello, I have a question."}
    ],
    [
        {"name": "name", "value": "testuser"},
        {"name": "email", "value": "invalid_email"},
        {"name": "message", "value": "Hello, I have a question."}
    ],
    [
        {"name": "email", "value": "feedback@example.com"},
        {"name": "rating", "value": "5"},
        {"name": "comments", "value": "Great service!"}
    ],
    [
        {"name": "email", "value": "invalid_email"},
        {"name": "rating", "value": "not_a_number"},
        {"name": "comments", "value": ""}
    ],
    [
        {"name": "event_name", "value": "Tech Conference"},
        {"name": "date", "value": "2024-05-01"},
        {"name": "attendee_email", "value": "attendee@example.com"},
        {"name": "phone", "value": "+79001234567"}
    ],
    [
        {"name": "event_name", "value": ""},
        {"name": "date", "value": "invalid_date"},
        {"name": "attendee_email", "value": "invalid_email"},
        {"name": "phone", "value": "not_a_phone"}
    ],
    [
        {"name": "username", "value": "newuser"},
        {"name": "email", "value": "newuser@example.com"},
        {"name": "extra_field", "value": "This is an extra field not in any template."}
    ]
]

for i, data in enumerate(test_data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Тест {i + 1}: {response.status_code} - {response.json()}")
    else:
        print(f"Тест {i + 1}: {response.status_code} - {response.text}")