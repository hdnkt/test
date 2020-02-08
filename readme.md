this is a basic django site following django's tutorial

must run with env var `DJANGO_SECRET_KEY`. you can generate with `echo "$(openssl rand -base64 32)"`

- Build command: `./build.sh`
- start command: `cd mysite && gunicorn mysite.wsgi:application`

This is deployed at https://django-test-9g3f.onrender.com/

You can [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)