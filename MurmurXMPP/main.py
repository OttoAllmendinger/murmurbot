import optparse
from MurmurBot import MurmurBot

def main():
    parser = optparse.OptionParser()
    parser.add_option("--ice", "-i")
    parser.add_option("--username", "-u")
    parser.add_option("--password", "-p")

if __name__=="__main__":
    main()
