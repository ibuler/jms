#!/usr/bin/env python
# coding: utf-8

"""
    connect.py
    ~~~~~~~~~~~
    This script is the jms endpoint for ssh connect.
    User login the server may first running.

    1. Use SSH Authentication. So not achieve socket and self authentication method.
    2. Use paramiko module as a proxy for your ssh connection
    3. Use ...


    :copyright: (c) 2016 by Jumpserver Team.
    :licence: BSD, see LICENSE for more details.

"""

import os
import sys
import paramiko
import select
import socket
import time

try:
    import termios
    import tty
except ImportError:
    print('\033[1;31m仅支持类Unix系统 Only unix like supported.\033[0m')
    time.sleep(3)
    sys.exit()

