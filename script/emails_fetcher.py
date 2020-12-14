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
from util.states_list import fifty_states_list

import sys
import os

OUTPUT_DIRECTORY = '../output/'
SANITIZED_OUTPUT_DIRECTORY = '../sanitized_output/'

def get_state_email_addresses(state_name, should_sanitize=False):
  ans = eval(f'{state_name}.run()')
  if should_sanitize:
    els = email_list_sanitizer(ans)
    ans = els.sanitize()
  return ans

def get_all_state_email_addresses(should_sanitize=False):
  ret_hash = {}
  for state in fifty_states_list():
    ret_hash[state] = get_state_email_addresses(state, should_sanitize)
  return ret_hash

def save_addresses_to_file(state_name, addresses, should_sanitize=False):
  if should_sanitize:
    filepath = f'{SANITIZED_OUTPUT_DIRECTORY}{state_name}.txt'
  else:
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

def save_all_state_email_addresses(should_sanitize=False):
  state_email_hash = get_all_state_email_addresses(should_sanitize)
  for key in state_email_hash:
    save_addresses_to_file(key, state_email_hash[key], should_sanitize)

if __name__ == "__main__":
  arg = sys.argv[1]
  arg2 = False
  if len(sys.argv) > 2:
    arg2 = sys.argv[2]

  # supported arguments:
  # all - get all state email addresses
  # save - save 
  if arg == 'all':
    get_all_state_email_addresses(arg2)
  elif arg == 'save':
    save_all_state_email_addresses(arg2) 
  elif arg in fifty_states_list():
    get_state_email_addresses(arg, arg2)
  else:
    print("Invalid value supplied.  supply a downcased state name, or 'all'")
