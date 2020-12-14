from state_scripts import alabama
from state_scripts import alaska
from state_scripts import arizona
from state_scripts import arkansas
from state_scripts import california
from state_scripts import colorado
from state_scripts import connecticut
from state_scripts import delaware
from state_scripts import florida
from state_scripts import georgia
from state_scripts import hawaii
from state_scripts import idaho
from state_scripts import illinois
from state_scripts import indiana
from state_scripts import iowa
from state_scripts import kansas
from state_scripts import kentucky
from state_scripts import louisiana
from state_scripts import maine
from state_scripts import maryland
from state_scripts import massachusetts
from state_scripts import michigan
from state_scripts import minnesota
from state_scripts import mississippi
from state_scripts import missouri
from state_scripts import montana
from state_scripts import nebraska
from state_scripts import nevada
from state_scripts import new_hampshire
from state_scripts import new_jersey
from state_scripts import new_mexico
from state_scripts import new_york
from state_scripts import north_carolina
from state_scripts import north_dakota
from state_scripts import ohio
from state_scripts import oklahoma
from state_scripts import oregon
from state_scripts import pennsylvania
from state_scripts import rhode_island
from state_scripts import south_carolina
from state_scripts import south_dakota
from state_scripts import tennessee
from state_scripts import texas
from state_scripts import utah
from state_scripts import vermont
from state_scripts import virginia
from state_scripts import washington
from state_scripts import west_virginia
from state_scripts import wisconsin
from state_scripts import wyoming

from util.email_list_sanitizer import email_list_sanitizer

import sys
import os

OUTPUT_DIRECTORY = '../output/'

def get_state_email_addresses(state_name, should_sanitize=False):
  ans = eval(f'{state_name}.run()')
  if should_sanitize:
    els = email_list_sanitizer.new(ans)
    ans = els.sanitize()
  return ans

def save_addresses_to_file(state_name, addresses):
  filepath = f'{OUTPUT_DIRECTORY}{state_name}.txt'
  try:
    os.remove(filepath)
  except OSError:
    pass
  with open(filepath, 'w') as f:
    if addresses is None:
      f.write('None')
    else:
      f.write('\n'.join(addresses))

def get_all_state_email_addresses():
  ret_hash = {}
  for state in FIFTY_STATES:
    ret_hash[state] = get_state_email_addresses(state) 
  return ret_hash

def save_all_state_email_addresses():
  state_email_hash = get_all_state_email_addresses()
  for key in state_email_hash:
    save_addresses_to_file(key, state_email_hash[key])

FIFTY_STATES = ['alabama',
                'alaska',
                'arizona',
                'arkansas',
                'california',
                'colorado',
                'connecticut',
                'delaware',
                'florida',
                'georgia',
                'hawaii',
                'idaho',
                'illinois',
                'indiana',
                'iowa',
                'kansas',
                'kentucky',
                'louisiana',
                'maine',
                'maryland',
                'massachusetts',
                'michigan',
                'minnesota',
                'mississippi',
                'missouri',
                'montana',
                'nebraska',
                'nevada',
                'new_hampshire',
                'new_jersey',
                'new_mexico',
                'new_york',
                'north_carolina',
                'north_dakota',
                'ohio',
                'oklahoma',
                'oregon',
                'pennsylvania',
                'rhode_island',
                'south_carolina',
                'south_dakota',
                'tennessee',
                'texas',
                'utah',
                'vermont',
                'virginia',
                'washington',
                'west_virginia',
                'wisconsin',
                'wyoming']

if __name__ == "__main__":
  arg = sys.argv[1]
  if arg == 'all':
    get_all_state_email_addresses()
  elif arg == 'save':
    save_all_state_email_addresses() 
  elif arg in FIFTY_STATES:
    get_state_email_addresses(arg)
  else:
    print("Invalid value supplied.  supply a downcased state name, or 'all'")
