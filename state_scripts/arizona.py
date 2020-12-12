import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_URL = 'https://www.azleg.gov/memberroster/'

# both senators and representative email addresses on this page
# however, the email addresses are not accessible.... link takes you to new page
# BUT
# I had discovered that the usernames on this page correspond with email addresses
# that end in 'azleg.gov'
# "The email address is built by combining the legislator's userId and @azleg.gov. For example a legislator with a userId of jjones, would be jjones@azleg.gov"

all_sh = state_helper(PRIMARY_URL)

all_text_for_links = all_sh.bs4_helper.get_text_for_a_tag()
for link in all_text_for_links:
  if 'Email' in link:
    print(link.replace('Email: ','').lower() + '@azleg.gov')
