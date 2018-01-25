#!/usr/bin/python
import sys
import logging
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, dir_path)

from app import app as application
