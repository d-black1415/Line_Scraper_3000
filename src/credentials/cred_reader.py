import sys


class CredentialReader:

    @staticmethod
    def read_cred_row(index):
        if len(sys.argv) <= 1:
            print('Please provide a credential filepath as the first command line argument to this program.')
            sys.exit(1)
        try:
            cred_f = open(sys.argv[1], 'r')
        except OSError:
            print("Please provide a valid credential filepath. File not found under: {}".format(sys.argv[1]))
            sys.exit(1)
        with cred_f:
            line_list = cred_f.read().splitlines()
            return line_list[index].split(',')
