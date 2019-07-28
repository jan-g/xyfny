from __future__ import print_function

import sys

from xyppy.vterm import NeedInput

from xyppy.zenv import Env, step
import xyppy.blorb as blorb
import xyppy.ops as ops
from xyppy.debug import err


def make_env(file):
    with open(file, 'rb') as f:
        mem = f.read()
    if blorb.is_blorb(mem):
        mem = blorb.get_code(mem)
    env = Env(mem, None)

    if env.hdr.version not in [1,2,3,4,5,7,8]:
        err('unsupported z-machine version: '+str(env.hdr.version))

    return env


def run(file):
    env = make_env(file)
    line = None
    while True:
        print(do_step(env, line))
        line = input("> ")


def do_step(env, next_line=None):
    env.screen.output = []
    if next_line is not None:
        env.screen.buffer.append(next_line)
    try:
        while True:
            step(env)
    except NeedInput as e:
        print(e)
        pass
    result = ''.join(env.screen.output).splitlines()
    #while len(result) > 0 and result[-1].startswith(">"):
    #    result = result[:-1]
    env.screen.output = []
    return '\n'.join(result)
