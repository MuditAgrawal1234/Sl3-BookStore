"""
WSGI config for bookstore project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_wsgi_application()