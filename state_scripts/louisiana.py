import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_REPRESENTATIVES_URL = 'https://house.louisiana.gov/H_Reps/H_Reps_Email'
PRIMARY_SENATORS_URL = 'http://senate.la.gov/Senators/Offices.asp'

rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
rep_sh.prepare_soup()
sen_sh = state_helper(PRIMARY_SENATORS_URL)
sen_sh.prepare_soup()

rep_texts = rep_sh.bs4_helper.get_text_for_span_tags()
for text in rep_texts:
  if '@' in text:
    print(text)

sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
for link in sen_links:
  if 'mailto:' in link:
    print(link.replace('mailto:',''))
