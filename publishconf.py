#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://100shapes.com'

PRODUCTION = True

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

GOOGLE_ANALYTICS = "UA-27923958-2"

# USe S3 bucket
ASSET_URL = 'http://media.100shapes.com/assets'
