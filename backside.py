#!/usr/bin/env python
__author__ = 'ms.shubin'
#TODO Need to do this on web

import stackexchange
import sys

sys.path.append('.')
sys.path.append('..')

try:
    get_input = raw_input
except NameError:
    get_input = input

user_api_key = 'onRboWY8xfpMSZpI1xeQZg(('


so = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key, impose_throttling=True)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        term = get_input('Please provide a search term:')
    else:
        term = ' '.join(sys.argv[1:])
    print('Searching for %s...' % term, )
    sys.stdout.flush()

    qs = so.search(intitle=term)

    print('\r--- questions with "%s" in title ---' % (term))

    for q in qs:
        try:
            print('%s %s %s %s' % (q.creation_date.strftime("%d.%m.%Y"), q.title, q.owner.display_name, '!Here the answer!' if q.answer_count > 0 else 'No answers'))
        except:
            print('%s %s %s' % (q.creation_date.strftime("%d.%m.%Y"), q.title, '!Here the answer!' if q.answer_count > 0 else 'No answers'))

