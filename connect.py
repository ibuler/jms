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
import datetime

try:
    import termios
    import tty
except ImportError:
    print('\033[1;31m仅支持类Unix系统 Only unix like supported.\033[0m')
    time.sleep(3)
    sys.exit()


username = 'root'
password = 'redhat'
host = '192.168.244.129'
port = 22

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')


def color_print(msg, color='red', exit=False):
    """
    Print colorful string.
    颜色打印字符或者退出
    """
    color_msg = {'blue': '\033[1;36m{0}\033[0m',
                 'green': '\033[1;32m{0}\033[0m',
                 'yellow': '\033[1;33m{0}\033[0m',
                 'red': '\033[1;31m{0}\033[0m',
                 'title': '\033[30;42m{0}\033[0m',
                 'info': '\033[32m{0}\033[0m'}
    msg = color_msg.get(color, 'red').format(msg)
    print(msg)
    if exit:
        time.sleep(2)
        sys.exit()
    return msg


class TTY:
    def __init__(self, host='127.0.0.1', port=22, username='root', password=''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh = None
        self.chan = None
        self.__get_chan()

    def __get_chan(self):
        """
        使用paramiko模块与后端ssh建立channel
        paramiko的channel其实是与后面ssh server建立了一个tcp长连接,输入都会发送到后面的主机上
        :return: None
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.host,
                        port=self.port,
                        username=self.username,
                        password=self.password)
        except (paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException):
            color_print('连接服务器失败', exit=True)
        self.ssh = ssh
        self.chan = ssh.invoke_shell(term='xterm')

    def __get_log_f(self):
        now = datetime.datetime.now()
        date_today = now.strftime('%Y%m%d')
        time_now = now.strftime('%H%M%S')
        log_today_dir = os.path.join(LOG_DIR, date_today)
        log_filename = os.path.join(log_today_dir, '{host}-{port}-{username}-{date}{time}.log'.format(
            host=self.host, port=self.port, username=self.username, date=date_today, time=time_now,
        ))
        if not os.path.isdir(log_today_dir):
            os.mkdir(log_today_dir, mode=0o777)
        log_f = open(log_filename, 'a')
        return log_f

    def posix_shell(self):
        log_f = self.__get_log_f()
        old_tty = termios.tcgetattr(sys.stdin)
        try:
            # 设置tty为raw模式, 不再使用已经设置好的tty, tty需要由我们来重新控制
            tty.setraw(sys.stdin.fileno())
            tty.setcbreak(sys.stdin.fileno())
            self.chan.settimeout(0.0)

            while True:
                try:
                    r, w, e = select.select([self.chan, sys.stdin], [], [])
                except:
                    pass

                if self.chan in r:
                    try:
                        recv_data = self.chan.recv(1024).decode('utf8')
                        if len(recv_data) == 0:
                            break
                        sys.stdout.write(recv_data)
                        sys.stdout.flush()
                        # 记录输入输出到日志
                        log_f.write(recv_data)
                    except socket.timeout:
                        print('Timeout')
                if sys.stdin in r:
                    x = os.read(sys.stdin.fileno(), 1024)
                    if len(x) == 0:
                        break
                    self.chan.send(x)

        finally:
            # 最终将原来的tty返回给用户
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
            log_f.close()


if __name__ == '__main__':
    tty_ = TTY(host=host, port=port, username=username, password=password)
    tty_.posix_shell()