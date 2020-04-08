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
import sys
from Asura import  utils


def get_preprocessing_parser():
    pass

def get_parser(descript):
    #to import optional user models
    usr_parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
    usr_parser.add_argument("--user-dir", default=None)
    usr_args, _ = usr_parser.parse_known_args()
    utils.import_user_module(usr_args)

    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--no-progress-bar', action='store_true', help='disable progress bar')
    parser.add_argument('--log-interval', type=int, default=1000, metavar='N',
                        help='log progress every N batches (when progress bar is disabled)')
    parser.add_argument('--log-format', default=None, help='log format to use',
                        choices=['json', 'none', 'simple', 'tqdm'])
    parser.add_argument('--tensorboard-logdir', metavar='DIR', default='',
                        help='path to save logs for tensorboard, should match --logdir '
                             'of running tensorboard (default: no tensorboard logging)')
    parser.add_argument('--seed', default=1, type=int, metavar='N',
                        help='pseudo random number generator seed')
    parser.add_argument('--cpu', action='store_true', help='use CPU instead of CUDA')
    parser.add_argument('--fp16', action='store_true', help='use FP16')
    parser.add_argument('--memory-efficient-fp16', action='store_true',
                        help='use a memory-efficient version of FP16 training; implies --fp16')
    parser.add_argument('--fp16-no-flatten-grads', action='store_true',
                        help='don\'t flatten FP16 grads tensor')
    parser.add_argument('--fp16-init-scale', default=2 ** 7, type=int,
                        help='default FP16 loss scale')
    parser.add_argument('--fp16-scale-window', type=int,
                        help='number of updates before increasing loss scale')
    parser.add_argument('--fp16-scale-tolerance', default=0.0, type=float,
                        help='pct of updates that can overflow before decreasing the loss scale')
    parser.add_argument('--min-loss-scale', default=1e-4, type=float, metavar='D',
                        help='minimum FP16 loss scale, after which training is stopped')
    parser.add_argument('--threshold-loss-scale', type=float,
                        help='threshold FP16 loss scale from below')
    parser.add_argument('--user-dir', default=None,
                        help='path to a python module containing custom extensions (tasks and/or architectures)')
    parser.add_argument('--empty-cache-freq', default=0, type=int,
                        help='how often to clear the PyTorch CUDA cache (0 to disable)')
    parser.add_argument('--all-gather-list-size', default=16384, type=int,
                        help='number of bytes reserved for gathering stats from workers')

