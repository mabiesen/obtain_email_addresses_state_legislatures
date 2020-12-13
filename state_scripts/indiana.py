import os
import sys
sys.path.append(os.getcwd() + '/..')

from state_helper import state_helper

HOUSE_DEMOCRATS_URL = 'https://indianahousedemocrats.org/members'
HOUSE_REPUBLICANS_URL = 'https://www.indianahouserepublicans.com/members/'
SENATE_DEMOCRATS_URL = 'https://www.indianasenatedemocrats.org/senators/'
SENATE_REPUBLICANS_URL = 'https://www.indianasenaterepublicans.com/senators'

# house dems do not appear to expose email addresses
# senate dems appear to use javascript to populate email address

#hd_sh = state_helper(HOUSE_DEMOCRATS_URL)
#hd_sh.prepare_soup()
hr_sh = state_helper(HOUSE_REPUBLICANS_URL)
hr_sh.prepare_soup()
#sd_sh = state_helper(SENATE_DEMOCRATS_URL)
#sd_sh.prepare_soup()
sr_sh = state_helper(SENATE_REPUBLICANS_URL)
sr_sh.prepare_soup()


hr_links = hr_sh.bs4_helper.get_hrefs_for_class('member-link')
for link in hr_links:
  massaged_link = 'https://' + hr_sh.html_helper.base_url + '/' + link
  temp_sh = state_helper(massaged_link)
  temp_sh.prepare_soup()
  links = temp_sh.bs4_helper.get_hrefs_for_a_tag()
  for s_link in links:
    if 'mailto:' in s_link:
      print(s_link.replace('mailto:',''))

#sd_links = sd_sh.bs4_helper.get_hrefs_for_class('eg-senators-grid-element-24')
#for link in sd_links:
#  temp_sh = state_helper(link)
#  temp_sh.prepare_soup()
#  links = temp_sh.bs4_helper.get_hrefs_for_a_tag()
#  for s_link in links:
#    print(s_link)
#    if 'mailto:' in s_link:
#      print(s_link.replace('mailto:',''))

sr_links = sr_sh.bs4_helper.get_hrefs_for_a_tags_in_div_by_class('senator-item')
for link in sr_links:
  temp_sh = state_helper('https://' + sr_sh.html_helper.base_url + link)
  temp_sh.prepare_soup()
  links = temp_sh.bs4_helper.get_hrefs_for_a_tag()
  for s_link in links:
    if 'mailto:' in s_link:
      print(s_link.replace('mailto:',''))
