from lib.state_helper import state_helper

def run():
  primary_url = 'https://www.legis.iowa.gov/legislators/informationOnLegislators/allLegislators'

  sh = state_helper(primary_url)
  sh_addrs = sh.get_mailto_addresses()
  for addr in sh_addrs:
    print(addr)
  return sh_addrs

if __name__ == "__main__":
  run()
