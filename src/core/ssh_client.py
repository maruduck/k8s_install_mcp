import json

class SshClient:
    def __init__(self, hostname='127.0.0.1', pwd='1234', port = 22, username='root'):
        self.token = ''
        self.hostname = hostname
        self.port = port
        self.pwd = pwd
        self.username = username

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, indent=4)

    def update_ssh_client(self, hostname: str, pwd: str, port: int, username: str) -> str:
        self.hostname = hostname
        self.port = port
        self.pwd = pwd
        self.username = username

        return self.to_json()

ssh_master_data = SshClient()
ssh_client_data = []