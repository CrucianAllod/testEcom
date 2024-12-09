import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testEcom.settings')
django.setup()

from forms.models import FormsTemplate

def populate_db():
    templates = [
        {
            "name": "User  Registration",
            "fields": {
                "username": "text",
                "email": "email",
                "password": "text",
                "confirm_password": "text"
            }
        },
        {
            "name": "Contact Us",
            "fields": {
                "name": "text",
                "email": "email",
                "message": "text"
            }
        },
        {
            "name": "Feedback",
            "fields": {
                "email": "email",
                "rating": "text",
                "comments": "text"
            }
        },
        {
            "name": "Event Registration",
            "fields": {
                "event_name": "text",
                "date": "date",
                "attendee_email": "email",
                "phone": "phone"
            }
        }
    ]

    for template in templates:
        try:
            FormsTemplate.objects.create(**template)
            print(f"Successfully created: {template['name']}")
        except Exception as e:
            print(f"Error creating template {template['name']}: {e}")

if __name__ == "__main__":
    populate_db()