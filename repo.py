import requests

V2_URL = '/v2'
V2_CATALOG_URL = '/v2/_catalog'


class DockerRepository:
    _repo_url = ""
    _user = ""
    _password = ""

    def __init__(self, repo_url, user, password):
        self._repo_url = repo_url
        self._user = user
        self._password = password

    @property
    def repo_url(self):
        return self._repo_url

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    def login(self):
        return

    def list_repos(self):
        return

    def list_tags(self, repo):
        return

    def is_v2_repo(self):
        resp = requests.get(self._repo_url + '/v2/', auth=(self._user, self._password), verify=False)
        return resp.ok

