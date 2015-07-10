Galex
======

Django app deployed on production:
-----------------------------------
http://protected-journey-8694.herokuapp.com/

Full Stack:
------------
- FrontEnd, UI: jQuery, Ajax, HTML/CSS
- Middlewear, API: Django Rest Framework
- Backend: PostGre (Prod), SQLite3 (Dev)
 
Environment:
-------------
- Python virtualenv
- Heroku App Deployment Cloud (versioning: requirements.txt and Running the server: Procfile)
- Gunicorn WebServer

Model, Template, Views:
------------------------
- https://github.com/cjgiridhar/galex/blob/master/journal/models.py
- https://github.com/cjgiridhar/galex/tree/master/journal/templates/journal
- https://github.com/cjgiridhar/galex/blob/master/journal/views.py

Admin Page
-----------
- Used it to create users and add articles
- https://github.com/cjgiridhar/galex/blob/master/journal/admin.py

Rest APIs:
-----------
- List: http://protected-journey-8694.herokuapp.com/api/articles/
- Detail: http://protected-journey-8694.herokuapp.com/api/articles/1/
- JSON Serializer: https://github.com/cjgiridhar/galex/blob/master/journal/serializers.py
- Docs: http://protected-journey-8694.herokuapp.com/docs/


Exception Handling and Logging:
--------------------------------
- https://github.com/cjgiridhar/galex/blob/master/journal/views.py
- Default level: Debug (Not to be done on Prod but added here for getting logs of heroku)
- Exceptions like: Http404, ObjectDoesNotExist used


Non Functional Requirements:
------------------------------
- Performance: File based caching of views (Article list refreshed every 10 mins and Detail every 15 mins), Template fragmented caching for sidebar
- Scaling: Gunicorn works on multiple worker processes (eliminates GIL), Setting on Heroku dynamo is WEB_CONCURRENCY=3
- Memory Handling: Used --max-requests 1200 on unicorn to restart a worker once 1200 requests are done
- Async requests: Could also work with gevent (greenlets) for better handling of I/O requests
- Throttling of Requests: UserRateThrottle for Rest APIs


Testing:
----------
- https://github.com/cjgiridhar/galex/blob/master/journal/tests.py


To be done
-----------
- Security: Authentication, Authorization for Rest APIs & CSRF token
- Template inheritance can be done & carousel to be added in What Read Next
