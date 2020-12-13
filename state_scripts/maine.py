from lib.state_helper import state_helper

PRIMARY_REPRESENTATIVES_URL = 'https://legislature.maine.gov/house/house/MemberProfiles/ListEmail'
PRIMARY_SENATORS_URL = 'https://legislature.maine.gov/senate/senators/9536'
#PRIMARY_SENATORS_URL = 'https://legislature.maine.gov/uploads/visual_edit/130th-senate-member-list-2.xlsx'

#senators xlsx file is bunk, does not contain email addresses
# the primary link suggests we should get email addresses in the excel file...

rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
rep_addrs = rep_sh.get_mailto_addresses()
for addr in rep_addrs:
  print(addr)

sen_sh = state_helper(PRIMARY_SENATORS_URL)
sen_sh.prepare_soup()
sen_links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
for link in sen_links:
  if '/senate/district' in link:
    temp_sh = state_helper('https://' + sen_sh.html_helper.base_url + link)
    temp_addrs = temp_sh.get_mailto_addresses()
    for addr in temp_addrs:
      print(addr)
