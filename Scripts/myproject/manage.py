#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.mail import send_mail


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Code to send email
    send_mail(
        'Subject here',
        'Here is the message.',
        '2020engineerahsan@gmail.com',
        ['syedahsannoori@gmail.com'],
        fail_silently=False,
    )

    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()