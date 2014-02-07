#!/usr/bin/env python2

from flask.ext.script import Manager
import app

manager = Manager(app.app)

if __name__ == "__main__":
    manager.run()

