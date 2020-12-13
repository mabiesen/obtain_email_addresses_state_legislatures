import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_REPRESENTATIVES_URL = 'https://house.louisiana.gov/H_Reps/H_Reps_Email'
PRIMARY_SENATORS_URL = 'http://senate.la.gov/Senators/Offices.asp'

rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
sen_sh = state_helper(PRIMARY_SENATORS_URL)

rep_texts = rep_sh.bs4_helper.get_text_for_span_tags()
for text in rep_texts:
  if '@' in text:
    print(text)

sen_addrs = sen_sh.get_mailto_addresses()
for addr in sen_addrs:
  print(addr)
