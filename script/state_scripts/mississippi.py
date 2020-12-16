from state_scripts.lib.state_helper import state_helper

def run():
  representatives_url = 'http://www.legislature.ms.gov/legislators/representatives/'
  senators_url = 'http://www.legislature.ms.gov/legislators/senators/'

# pretty sure the rep links are loaded with javascript.....
# cant find them even with phantomjs + selenium
# attempted a 1 second timeout, did nothing

#  sen_sh = state_helper(senators_url, True)
#  sen_sh.prepare_soup()
#  links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
#  for link in links:
#    print(link)

if __name__ == "__main__":
  run()
