#!/usr/bin/python
# encoding: utf-8

import sys
import requests

from workflow import Workflow


def get_web_data():
  return requests.get("http://localhost:5000/search").json()

def main(wf):
    # Save data from `get_web_data` for 1 seconds under
    # the key ``example``
    data = wf.cached_data('example', get_web_data, max_age=1)
    for datum in data['result']:
        wf.add_item(title = datum['name'], 
                    arg = datum['url'],
                    valid = True,)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))