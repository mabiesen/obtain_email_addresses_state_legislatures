import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

PRIMARY_REPRESENTATIVES_URL =  'https://www.ilga.gov/house/'
PRIMARY_SENATORS_URL = 'https://www.ilga.gov/senate/'

# it seems that only house members list email addresses :(
# need to drill into reps to see email
#... but it seems they are nesting tds, i cant get to the nested td...
#..... and it seems likely that house email detail are created via javascript
# can possibly work around the issue using regex.

#rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
#rep_sh.prepare_soup()

#links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
#links = rep_sh.html_helper.get_full_urls_from_hrefs(links)
#for link in links:
# if 'MemberID=' in link and 'Rep.asp?' in link:
#    massaged_link = ('https://' + link).replace('./','/')
#    tmp_rep_sh = state_helper(massaged_link)
#    tmp_rep_sh.prepare_soup()
#    texts = tmp_rep_sh.bs4_helper.get_text_for_tds()
#    for text in texts:
#      if '@' in text and len(text) < 70:
#        print(text)