import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_URL = 'https://leg.colorado.gov/legislators'

# this link contains both house and senate
# it is in a data table
# to their kudos, they do have an excel output; but ideally this is csv

all_sh = state_helper(PRIMARY_URL)
addresses = all_sh.bs4_helper.get_text_for_tds()
for address in addresses:
  if  '@' in address:
    print(address.strip())
