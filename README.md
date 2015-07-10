Galex
======

Django app deployed on production:
http://protected-journey-8694.herokuapp.com/

Stack:
FrontEnd, UI - jQuery, Ajax, HTML/CSS
Middlewear, API - Django Rest Framework
Backend - PostGre (Prod), SQLite3 (Dev)
 
Environment:
Python virtualenv
Heroku App Server
Gunicorn WebServer


Model:
https://github.com/cjgiridhar/galex/blob/master/journal/models.py


Template:
https://github.com/cjgiridhar/galex/tree/master/journal/templates/journal


Views:
https://github.com/cjgiridhar/galex/blob/master/journal/views.py


REST API:
List: http://protected-journey-8694.herokuapp.com/api/articles/
Detail: http://protected-journey-8694.herokuapp.com/api/articles/1/
JSON Serializer: https://github.com/cjgiridhar/galex/blob/master/journal/serializers.py

API Docs:
http://protected-journey-8694.herokuapp.com/docs/


Exception Handling and Logging:
https://github.com/cjgiridhar/galex/blob/master/journal/views.py


Non Functional Requirements:
Performance: File based caching of views (Article list refreshed every 10 mins and Detail every 15 mins), Template fragmented caching for sidebar
Scaling: Gunicorn works on multiple worker processes (eliminates GIL), Setting on Heroku dynamo is WEB_CONCURRENCY=3
Memory Handling: Used --max-requests 1200 on unicorn to restart a worker once 1200 requests are done
Async requests: Could also work with gevent (greenlets) for better handling of I/O requests
Throttling of Requests: UserRateThrottle for rest apis


Testing:
https://github.com/cjgiridhar/galex/blob/master/journal/tests.py
