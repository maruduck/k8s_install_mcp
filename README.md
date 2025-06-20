# MCP를 활용한 kubernetes 자동화 설치

Rocky Linux 환경에서 kubernetes 자동화 설치 기능을 갖춘 MCP 에이전트입니다.

## 설치 환경

- Rocky-8.10-x86_64-minimal.iso
- Virtual Box
- kubernetes 1.29

## MCP 환경 설정

### git clone

```bash
$ git clone https://github.com/maruduck/k8s_install_mcp.git
```

- uv 실행

```json
{
    "mcpServers": {
        "k8s": {
            "requestTimeout": 12000000000,
            "command": "uv",
            "args": ["run", "--directory $(clone 경로)\\k8s_install_mcp", "k8s-install-mcp"]
        }  
    }
}
```

- python venv 실행

```bash
$ python -m venv venv
$ venv\Scripts\activate # Mac은 source venv/bin/activate
$ pip install uv
$ uv pip install -r requirements.txt
```

```json
{
    "mcpServers": {
        "k8s": {
            "requestTimeout": 12000000000,
            "command": "$(클론 위치)\\k8s_install_mcp\\.venv\\Scripts\\python.exe",
            "args": ["$(클론 위치)\\k8s_install_mcp\\src\\main.py"]
        }
    }
}
```

- uvx 사용

```json
{
    "mcpServers": {
        "k8s": {
            "requestTimeout": 12000000000,
            "command": "uvx",
            "args": ["k8s-install-mcp"]
        }
    }
}

```


## 설치 예시

---

### 환경 설정

sudo 권한 부여
```bash
$ visudo  
# 반드시 마지막 줄에 입력할 것
# 다른 설정의 우선순위에 밀릴 수 있음
(사용자명) ALL=(ALL)  NOPASSWD: ALL 
```

타임 아웃 에러 발생 가능성이 있으므로 미리 update를 수행한 후 실행할 것
```bash
$ dnf update -y
```

### Master node 설치
```
k8s 도구를 사용하여 127.0.0.1 호스트 104 포트에서 $(username) 사용자 1234 비밀번호로 k8s 마스터 설치해줘 
```

### Client node 설치
```
k8s 도구를 사용하여 127.0.0.1 호스트 103 포트에서 $(username) 사용자 1234 비밀번호로 node1 노드 이름으로 k8s 클라이언트 설치해줘 
```



## 함수 목록

- master_set_ssh
  - master 노드 ssh 정보 설정
- client_set_ssh
  - client 노드 ssh 정보 설정
- master_token
  - master의 kubeadm join 명령어($HOME의 token.txt에 저장) 반환
- connect_test
  - ssh 연결 테스트
- exec
  - 명령어 실행
- update
  - dnf update 실행
- setting_env
  - k8s 설치 환경 설정
- k8s_master_install
  - master 노드 설치
- k8s_client_install
  - client 노드 설치
- k8s_client_token
  - master token.txt 명령어(kubeadm join) 실행