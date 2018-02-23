#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QGuiApplication
from src import main

app = QGuiApplication(sys.argv)
main.run(app)
