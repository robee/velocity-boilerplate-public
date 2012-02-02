import os
import sys
import logging
import hashlib

def pass_hash(password):
    return hashlib.sha224(password).hexdigest()