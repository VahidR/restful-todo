[![Build Status](https://travis-ci.org/vahidR/restful-todo.svg?branch=master)](https://travis-ci.org/vahidR/restful-todo)

RESTful Todo Application [ARCHIVED]
=========================
A RESTful web-based Todo application in Python and Flask 

Install
========
```
$ python manage.py createall
```

Running
========
```bash
$ python manage.py runserver
```

Test
=====
```bash
$ python manage.py test
```

Remove
========
```bash
$ python manage.py dropall
```


RESTful interactions
====================
**GET the List of todos**
```
curl -u test:test -H "Accept: application/json" -i http://localhost:5000/todos/api/v1.0/todos
```

**GET an individual todo**
```
curl -u test:test -H "Accept: application/json" -i http://localhost:5000/todos/api/v1.0/todo/<ID>
```

**POST a todo**
```
curl -u test:test -H "Content-Type: application/json" -X POST -d '{"title":"Lunch", "body":"Having lunch"}' -i http://localhost:5000/todos/api/v1.0/todo/create 
```

**UPDATE a todo**
```
curl -u test:test -H "Content-Type: application/json" -X PUT -d '{"title":"Dinner", "body":"Having Dinner"}' -i http://localhost:5000/todos/api/v1.0/todo/update/<ID>
```

**DELETE a todo**
```
curl -u test:test -H "Accept: application/json" -X DELETE http://localhost:5000/todos/api/v1.0/todo/delete/<ID>
```
