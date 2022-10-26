#!/usr/bin/env/python3

import os 
import json 
import shutil # For copy and overwrite operations 
from subprocess import PIPE, run 
import sys

"""
1. 
Grabbing the source dir and the target dir (relative to the current path) as CLI arguments 
So that we will know where to store the games that we find and where to look for them 
"""

if __name__ == "__main__": # Executing the main script only if we run the script directly and not via import to other script (we would be able to import functions and classes only)
    print(sys.argv)
    