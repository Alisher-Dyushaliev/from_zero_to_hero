# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/login of ISP manager/data/www/domen/mysite')
sys.path.insert(1, '/var/www/login of ISP manager/data/venv/lib/python3.10.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()