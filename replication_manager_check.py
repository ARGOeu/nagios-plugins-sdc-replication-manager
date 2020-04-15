#!/usr/bin/python

import json
import sys
import requests
import argparse

##{u'test_mode': u'false', u'enable_populate': u'false', u'datetime': u'20200411T21:42:26', u'configIsValid': u'true', u'version': u'1.0.43', u'edmo_code': u'269'}


# ##############################################################################
# Replication Manager Client  #
# ##############################################################################


def ValidateValues(arguments):
        """ Validate values - input values """

        if arguments.timeout <= 0:
            print("\nInvalid timeout value: %s\n" % arguments.timeout)
            print_help()
            exit()

        if arguments.hostname is None:
            print("\nNo hostname provided\n")
            print_help()
            exit()

        if not arguments.hostname.startswith("http"):
            print("\nNo schema supplied with hostname, did you mean https://%s?\n" % arguments.hostname)
            print_help()
            exit()


def print_help():
        """ Print help values."""

        print("usage: replication_manager_check.py -H  -r")
        print("--- ---- ---- ---- ---- ---- ----\n")
        print("main arguments:")
        print("-H hostname")
        print("\n")
        print("optional arguments:")
        print(" -h, --help  show this help message and exit")
        print("-r replication manager path")
        print("-p port")
        print("-t timeout")
        print("-v verbose")

def debugValues(arguments):
    """ Print debug values.
        Args:
            arguments: the input arguments
    """
    if arguments.debug:
        print("[debugValues] - hostname: %s" % arguments.hostname)
    if arguments.rpath != '':
        print("[debugValues] - rpath: %s" % arguments.rpath)
    if arguments.port != '':
        print("[debugValues] - port: %s" % arguments.port)
    if arguments.timeout != '':
        print("[debugValues] - timeout: %s" % arguments.timeout)


def checkHealth(URL, arguments):
    """ Check service status.
        Args:
           URL : service hostname
           timeout : how long should we wait for a response from the server
    """
    response = None
    iif arguments.rpath is None: :
        u = URL + "api/api_v1/status"
    else: 
        u = URL + arguments.rpath + "api/api_v1/status"

    if arguments.debug:
        print("[debugValues] - finalPath: %s" % u)
    timeout = arguments.timeout
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url=u, timeout=timeout, headers=headers)

        #############ERROR handlibg ##############
    except requests.exceptions.SSLError:
        description = "WARNING - Invalid SSL certificate"
        exit_code = 1
        return description, exit_code
    except requests.exceptions.ConnectionError:
        description = "CRITICAL - Service unreachable"
        exit_code = 2
        return description, exit_code
    except Exception as e:
        description = 'UNKNOWN - {0}'.format(str(e))
        exit_code = 3
        return description, exit_code

    if response is None:
        description = "UNKNOWN - Status unknown"
        exit_code = 3
        return description, exit_code

    if response.status_code == 404:
        description = "CRITICAL - Endpoint not found"
        exit_code = 2
        return description, exit_code
    if response.status_code != 200:
        description = "WARNING - Unexpected status code %s" % response.status_code
        exit_code = 1
        return description, exit_code

    content = response.json()
    if arguments.debug:
       print content
    todos = json.loads(response.text)
    if 'configIsValid' not in todos:
        description ='CRITICAL - Field configIsValid is missing from the response {0}'.format(str(todos))
        exit_code = 1
        return description, exit_code

    if todos["configIsValid"] == False:
        description ='CRITICAL - Field configIsValid is false'
        exit_code = 2
        return description, exit_code

    description = "OK - Service reachable"
    exit_code = 0
    return description, exit_code

def printResult(description, exit_code):
    """ Print the predefined values
        Args:
            description: the nagios description
            exit_code: the code that should be returned to nagios
    """

    print(description)
    sys.exit(exit_code)

def main():

    parser = argparse.ArgumentParser(description='Replication Manager probe '
                                                 'Supports healthcheck.')
    parser.add_argument("--hostname", "-H", help='The Hostname of Replication service')
    parser.add_argument("--rpath", "-r")
    parser.add_argument("--port", "-p", type=int)
    parser.add_argument("--timeout", "-t", metavar="seconds", help="Timeout in seconds. Must be greater than zero", type=int, default=30)
    parser.add_argument("--verbose", "-v", dest='debug', help='Set verbosity level', action='count', default=0)

    arguments = parser.parse_args()

    ValidateValues(arguments)

    if arguments.debug:
       debugValues(arguments)
    URL = arguments.hostname
    if arguments.port is not None:
        URL += ":%s" % arguments.port

    description, exit_code = checkHealth(URL, arguments)
    printResult(description, exit_code)

if __name__ == "__main__":
    main()

