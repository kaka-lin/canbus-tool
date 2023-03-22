#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QGuiApplication
from src import main

if __name__ == "__main__":
    mode = ''
    # use: python3 canbus_tool.py prod
    if len(sys.argv) == 2:
        mode = sys.argv[1]

    if hasattr(sys, "frozen"):
        # running in a bundle
        root_dir = os.path.dirname(os.path.abspath(sys.executable))
        mode = 'prod'
    else:
        # running live
        root_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QGuiApplication(sys.argv)
    main.run(app, root_dir, mode)
