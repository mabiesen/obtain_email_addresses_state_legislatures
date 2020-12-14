from state_scripts.lib.state_helper import state_helper

def run():
  representatives_url = 'http://www.legislature.ms.gov/legislators/representatives/'
  senators_url = 'http://www.legislature.ms.gov/legislators/senators/'

# pretty sure the rep links are loaded with javascript.....
# cant find them

#sen_sh = state_helper(representatives_url)
#sen_sh.prepare_soup()
#links = sen_sh.bs4_helper.get_hrefs_for_a_tag()
#for link in links:
#  print(link)

if __name__ == "__main__":
  run()
