from state_scripts.lib.state_helper import state_helper

def run():
  primary_url = 'https://www.legis.nd.gov/files/resource/miscellaneous/legislatormergeinformation.xls'

  sh = state_helper(primary_url)
  addrs = sh.parse_xls_file_column_by_index(0,6)
  for addr in addrs:
    print(addr)

  return addrs

# Im not finding anything for state representatives!!!

if __name__ == "__main__":
  run()
