from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling
import os

application = Cling(MediaCling(get_wsgi_application()))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my1.settings')

#application = get_wsgi_application()
