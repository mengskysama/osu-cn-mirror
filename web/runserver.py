#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author mengskysama

from web import app


from datetime import datetime
from copy import copy
import calendar


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)