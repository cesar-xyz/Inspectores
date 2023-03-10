from datetime import datetime


# helpers for models.py

def set_fotografia_path(instance, filename):
    return 'padron/inspector/{0}---{1}'.format(datetime.now().strftime('%Y-%m-%d--%H-%M'), filename)
