#!/usr/bin/env python

import os
from app import create_app, db
from app.models import Todo
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Todo=Todo)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def createall():
  """ creats the table."""
  db.create_all()

@manager.command
def dropall():
  """ drop the table."""
  db.drop_all()


if __name__ == '__main__':
    manager.run()
