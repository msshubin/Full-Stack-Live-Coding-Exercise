#!/usr/bin/env python
__author__ = 'ms.shubin'
#TODO Need to do this on web

import stackexchange

def find(title):

    user_api_key = 'onRboWY8xfpMSZpI1xeQZg(('

    so = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key, impose_throttling=True)

    return so.search(intitle=title, sort='creation')
