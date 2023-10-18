#!/bin/bash
echo 'sleeping 10 secs' 
sleep 20

flask db init

flask db migrate -m "initial migrate"

flask db upgrade

#serv de aplicaciones que corre Flask app
#interfaz de serv. web q sirve app web y facilita las webapps de python
gunicorn app:app --bind 0.0.0.0:5030