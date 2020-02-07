this is a basic django site following django's tutorial

must run with env var `DJANGO_SECRET_KEY`. can generate with `echo "$(openssl rand -base64 32)"`

Build command: `./build.sh`
start command: `gunicorn mysite.wsgi`