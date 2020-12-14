from lib.state_helper import state_helper

def run():
  representatives_url = 'http://www.legislature.state.al.us/aliswww/ISD/House/ALRepresentatives.aspx'
  senators_url = 'http://www.legislature.state.al.us/aliswww/ISD/Senate/ALSenators.aspx'

if __name__ == "__main__":
  run()

# this site uses javascript for its reps
# need to simulate button clicking
