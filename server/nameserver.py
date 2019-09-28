#!/usr/bin/python3

#################################################################
# Users can register their name/ip by connecting to this server #
#################################################################

from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

DEFAULT_PORT = 8000

def usage(progname):
    print("python {} [options]".format(progname))
    print("options:")
    print("\t-h\tPrint this help message and exit")
    print("\t-p <port>\tRun on the specified port")
    print("\t\t(Defaults to port {})".format(DEFAULT_PORT))

def parse_args(argv):
    parsed = {"port" : DEFAULT_PORT}
    lastarg = None
    for arg in argv[1:]:
        if lastarg == '-p':
            parsed['port'] = int(arg)
            lastarg = None
        elif lastarg == None:
            if arg == '-p':
                lastarg = arg
            elif arg == '-h' or arg == '-?':
                usage(argv[0])
                exit(0)
            else:
                print("Unrecognized argument '{}'".format(arg))
                usage(argv[0])
                exit(1)
        else:
            print("Unrecognized argument '{} {}'".format(lastarg, arg))
            usage(argv[0])
            exit(1)
    return parsed

def run_server():
    parsed_args = parse_args(argv)
    port = parsed_args['port']
    host = '' # all available interfaces

    print("Running on port {}".format(port))

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        print('Server connected to by {}'.format(address))
        while True:
            data = connection.recv(1024)
            if not data: break
            connection.send(b'Echo => ' + data)
        connection.close()
        print('Closed connection to {}'.format(address))

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nServer exiting now...")
