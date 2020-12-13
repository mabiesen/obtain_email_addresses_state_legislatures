from lib.state_helper import state_helper

PRIMARY_URL = 'https://www.arkleg.state.ar.us/Legislators/List'

# this url contains both senate and house

all_sh = state_helper(PRIMARY_URL)
all_sh.prepare_soup()
hrefs = all_sh.bs4_helper.get_hrefs_for_a_tag()
for href in hrefs:
  if 'mailto' in href:
    if '?' not in href: # preventing capturing webmaster email
      print(href.replace('mailto:',''))
