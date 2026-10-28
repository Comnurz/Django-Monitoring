# Django-Monitoring
Django monitoring web application
This project runs on Python 3.11 with Django 5.2 LTS.

server.py runs on your server which you want to collect data from.

Run this command in your server terminal:

```
pip install -r serverrequirements.txt
```

Run this command in your local terminal:

```
pip install -r requirements.txt
python manage.py makemigrations monitor
python manage.py migrate
python manage.py runserver
```

## Configuration

Before use, configure the following environment variables on the monitoring app
side (local). A `.env`-style approach or shell exports work:

- `DJANGO_SECRET_KEY` - long random secret (required in production)
- `DEBUG` - `1` for development, `0` for production
- `ALLOWED_HOSTS` - comma-separated list, e.g. `localhost,127.0.0.1,yourdomain`
- `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` - credentials for alert emails

On the server side (the agent), set:

- `MONITORING_URL` - base URL of the monitoring app, e.g.
  `https://monitor.example.com/en` (defaults to `http://localhost:8000/en`)

## Token-based server registration

The server agent authenticates with a per-server token instead of sending
passwords on every request.

1. On the monitoring app, create a user account and a server via the web UI.
2. On the server to be monitored, run:

   ```
   python register.py
   ```

   Enter your monitoring-app username, password, and the server name. This
   exchanges the credentials **once** for a token stored locally in
   `servertoken.txt` (mode `0600`) and starts `server.py` in the background.

3. `server.py` now posts RAM/CPU/Disk metrics to `/api/dbsave/` every 60
   seconds using `Authorization: Token <key>`. The server identity is derived
   from the token server-side; no credentials are sent per-request.

## Notes

- The old plaintext-password `GET /user` endpoint has been removed. Use
  `POST /api/register/` instead.
- `serverid.txt` is replaced by `servertoken.txt`.
