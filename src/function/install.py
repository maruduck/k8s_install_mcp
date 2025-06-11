import paramiko
from core import ssh_client, install_commands
from function import utils

class InstallTools:

    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    def update(self, ssh_data: ssh_client):
        log = utils.exec(ssh_data=ssh_data, command="sudo dnf -y update")
        return log

    def set_env(self, ssh_data: ssh_client) -> str:
        log = utils.exec_commands(ssh_data=ssh_data, commands=install_commands.setting_commands)
        return 'settings ok'

    def k8s_master_install(self, ssh_data: ssh_client) -> str:
        utils.exec_commands(ssh_data=ssh_data, commands=install_commands.master_install_commands)
        ssh_data.token = utils.exec(ssh_data=ssh_data, command="cat token.txt")
        return "Master install Complete"

    def k8s_client_install(self, ssh_data: ssh_client, token: str):
        utils.exec_commands(ssh_data=ssh_data, commands=install_commands.client_install_commands)
        utils.exec(command=token)
        return "Client install Complete"

install = InstallTools()