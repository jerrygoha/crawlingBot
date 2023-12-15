#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티 입니다.
#manage.py 에 대한 자세한 정보는 django-admin and manage.py 에서 확인할 수 있습니다.

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawlingProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
