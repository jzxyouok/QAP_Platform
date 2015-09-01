#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pexpect
import sys
import os

conf = {
    "user": "root",
    "host": "61.158.108.30",
    "port": 10086,
    "password": "Jyjxxzx88393896",
    "dest": "/data/projects/QAP_Server",
    "exclude": [".idea", ".git"]
}

if __name__ == "__main__":
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    # 切换工作目录到项目根目录
    os.chdir(os.path.join(dirname, "../"))
    # 文件同步命令
    excl = " ".join(["--exclude " + item for item in conf["exclude"]])
    cmd = "rsync -e 'ssh -p %d' -aP %s . %s@%s:%s" % (conf['port'], excl, conf["user"], conf["host"], conf["dest"])
    # 通过pexpect自动执行
    print cmd
    child = pexpect.spawn(cmd)
    child.expect('password:')
    child.sendline(conf['password'])
    child.interact()
