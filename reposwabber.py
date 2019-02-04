from repo import DockerRepository
import argparse


def get_config():
    parser = argparse.ArgumentParser(description='Utility to remove dead dead docker images')
    parser.add_argument('-r', '--repository', help='Repository URL', default='', required=True)
    parser.add_argument('-u', '--user', help='Docker repository user id', default='')
    parser.add_argument('-p', '--password', help='Docker repository user password', default='')
    args = parser.parse_args()
    config = {}
    config['repository'] = args.repository
    if args.user != '':
        config['user'] = args.user
    if args.password != '':
        config['password'] = args.password
    return config


program_config = get_config()
repo = DockerRepository('https://mark-xps-15-9550/v2/_catalog', 'username', 'password')


