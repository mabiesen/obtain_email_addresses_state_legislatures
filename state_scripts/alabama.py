from lib.state_helper import state_helper

def run():
  PRIMARY_REPRESENTATIVES_URL = 'http://www.legislature.state.al.us/aliswww/ISD/House/ALRepresentatives.aspx'
  PRIMARY_SENATORS_URL = 'http://www.legislature.state.al.us/aliswww/ISD/Senate/ALSenators.aspx'

if __name__ == "__main__":
  run()

# this site uses javascript for its reps
# need to simulate button clicking
