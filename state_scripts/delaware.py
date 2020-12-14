from lib.state_helper import state_helper

def run():
  PRIMARY_REPRESENTATIVES_URL = 'https://legis.delaware.gov/Chambers/House/AssemblyMembers'
  PRIMARY_SENATORS_URL = 'https://legis.delaware.gov/Chambers/Senate/AssemblyMembers'

#  these url's display links to senators
# they do not  directly expose senator email  addresses; for that
# we need to go to each senator/rep's page
# having problems though.....
# seems the table we need to inspect is using javascript

#rep_sh = state_helper(PRIMARY_REPRESENTATIVES_URL)
#sen_sh = state_helper(PRIMARY_SENATORS_URL)

#all_rep_links = rep_sh.bs4_helper.get_hrefs_for_a_tag()
#all_rep_links = rep_sh.html_helper.get_full_urls_from_hrefs(all_rep_links)
#for link in all_rep_links:
#  print(link)
