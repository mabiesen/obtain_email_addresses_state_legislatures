import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_REPRESENTATIVES_URL = 'http://akleg.gov/house.php'
PRIMARY_SENATORS_URL = 'http://akleg.gov/senate.php'

# each of these pages has mail-to links included in primary page

rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
sen_sh = state_helper(PRIMARY_SENATORS_URL)

rep_links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
for link in rep_links:
  if 'mailto:' in link:
    print(link.replace('mailto:',''))

sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
for link in sen_links:
  if 'mailto:' in link:
    print(link.replace('mailto:',''))
