import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_SENATORS_URL = 'http://www.kslegislature.org/li/b2019_20/chamber/senate/roster/'
PRIMARY_REPRESENTATIVES_URL = 'http://www.kslegislature.org/li/b2019_20/chamber/house/roster/'

sen_sh = state_helper(PRIMARY_SENATORS_URL)
sen_sh.prepare_soup()
rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
rep_sh.prepare_soup()

rep_links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
for link in rep_links:
  if 'mailto:' in link:
    print(link.replace('mailto:',''))

sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
for link in sen_links:
  if 'mailto:' in link:
    print(link.replace('mailto:',''))
