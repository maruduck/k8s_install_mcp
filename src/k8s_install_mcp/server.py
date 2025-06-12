from mcp.server.fastmcp import FastMCP
from core import ssh_master_data, ssh_client_data, SshClient
from function import utils, install

mcp = FastMCP('k8s')

@mcp.tool()
def set_master_ssh(self, hostname: str, pwd: str, username='root', port=22) -> str:
    """master ssh 정보 설정"""
    return ssh_master_data.update_ssh_client(hostname=hostname, pwd=pwd, username=username, port=port)

@mcp.tool()
def master_token(self) -> str:
    """토큰 반환"""
    return ssh_master_data.get_token()

@mcp.tool()
def notice(self, type: str, message: str) -> str:
    """연결 테스트하기"""
    if type == 'master':
        return utils.notify(ssh_data=ssh_master_data, message=message)
    return utils.notify(ssh_data=ssh_client_data, message=message)


@mcp.tool()
def exec(self,type: str, command: str) -> str:
    """커맨드 실행하기"""
    if type == 'master':
        return utils.exec(ssh_data=ssh_master_data, command=command)
    return utils.exec(ssh_data=ssh_client_data, command=command)


@mcp.tool()
def update(self, type: str) -> list:
    """dnf update: 장시간 걸리므로 계속 기다릴것 """
    if type == 'master':
        return install.update(ssh_data=ssh_master_data)
    return install.update(ssh_data=ssh_client_data)

@mcp.tool()
def setting_env(self, type: str) -> str:
    """setting env: k8s 환경 설정"""
    if type == 'master':
        return install.set_env(ssh_data=ssh_master_data)
    return install.set_env(ssh_data=ssh_client_data)


@mcp.tool()
def k8s_master_install(self) -> str:
    """update, setting env 수행 후 kubernetes(k8s) master 자동화 설치: 장시간 걸리므로 계속 기다릴것"""
    install.k8s_master_install(ssh_data=ssh_master_data)
    return "설치 완료"


@mcp.tool()
def set_client_ssh(self, hostname: str, pwd: str, username='root', port=22) -> list:
    """client ssh 정보 설정"""
    ssh_client_data.update_ssh_client(hostname=hostname, pwd=pwd, username=username, port=port)
    return ssh_client_data

@mcp.tool()
def k8s_client_install(self) -> list:
    """update, setting env 수행 후  kubernetes(k8s) client 자동화 설치하기"""
    return install.k8s_client_install(ssh_data=ssh_client_data, token=ssh_master_data.get_token())


def main():
    print('server test')
    mcp.run()