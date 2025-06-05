import paramiko
from core import ssh_client, install_commands

class InstallTools:

    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)


    async def exec(self, ssh_data: ssh_client, commands: list) -> list:

        log = []
        self.ssh.connect(hostname=ssh_data.hostname,
                         port=ssh_data.port,
                         username=ssh_data.username,
                         password=ssh_data.pwd,
                         allow_agent=False,
                         look_for_keys=False)
        try:
            for command in commands:
                stdin, stdout, error = self.ssh.exec_command(command)

                if stdout.channel.recv_exit_status() == 0:
                    txt = stdout.read().decode()
                    if txt:
                        log.append( stdout.read().decode() )
                else:
                    log.append( error.read().decode() )
                    break
        finally:
            self.ssh.close()
            return log

    async def k8s_master_install(self, ssh_data: ssh_client) -> str:

        await self.exec(ssh_data=ssh_data, commands=install_commands.master_install_commands)
        return "Master install Complete"

    async def k8s_client_install(self, ssh_data: ssh_client):
        await self.exec(ssh_data=ssh_data, commands=install_commands.client_install_commands)
        return "Client install Complete"

install = InstallTools()