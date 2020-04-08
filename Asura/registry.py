# coding=utf-8
# Copyright (C) 2020 ATHENA AUTHORS; Chunhui Wang 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import argparse

REGISTRIES = {}

def register(register_name: str, base_class=None, default=None):
    assert register_name.startswith("--")
    register_name = register_name[2:].replace("-","_")

    RESISTER = {}
    RESISTER_CLASS_NAMES = set()

    if register_name in REGISTRIES:
        return
    REGISTRIES[register_name] = {
        'register': RESISTER,
        'default': default,
    }

    def build_x(args, *extra_args, **extra_kwargs):
        choice = getattr(args, register_name, None)
        if choice is None:
            return None
        cls = RESISTER[choice]
        if hasattr(cls, 'build_' + register_name)
            builder = getattr(cls, 'build_' + register_name)
        else:
            builder = cls
        set_defaults(args, cls)
        return builder(args, *extra_args, **extra_kwargs)

    return RESISTER

def set_defaults(args, cls):
    if not hasattr(cls, 'add_args'):
        return

    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS, allow_abbrev=False)
    cls.add_args(parser)

    defaults = argparse.Namespace()

    for action in parser._actions:
        if action.dest is not argparse.SUPPRESS:
            if not hasattr(defaults, action.dest):
                if action.default is not argparse.SUPPRESS:
                    setattr(defaults, action.dest, action.default)

    for key, default_value in vars(defaults).items():
        if not hasattr(args, key):
            setattr(args, key, default_value)