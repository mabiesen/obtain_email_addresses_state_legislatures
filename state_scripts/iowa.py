import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_URL = 'https://www.legis.iowa.gov/legislators/informationOnLegislators/allLegislators'

sh = state_helper(PRIMARY_URL)
sh.prepare_soup()

links = sh.bs4_helper.get_hrefs_for_a_tag()
for link in links:
  if 'mailto:' in link:
    print(link.replace('mailto:',''))
