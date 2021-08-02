
import getopt
import sys


class mysql2postgres:
    def __init__(self):
        self.host = None

    def handle_args(self,argv):
        inputfile = ''
        outputfile = ''
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print('test.py -i <inputfile> -o <outputfile>')
            self.help()
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('test.py -i <inputfile> -o <outputfile>')
                self.help()
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        print('Input file is "', inputfile)
        print('Output file is "', outputfile)

    def help(self):
        print("m2p mysql to postgres migration tool")
        print("")
        print("m2p")

    def test(self):
        pass
