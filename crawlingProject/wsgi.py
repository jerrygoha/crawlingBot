"""
현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다.
WSGI를 사용하여 배포하는 방법를 읽어보세요.

WSGI config for crawlingProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawlingProject.settings')

application = get_wsgi_application()
