# MCP를 활용한 kubernetes 자동화 설치

---

Rocky Linux 환경에서 kubernetes 자동화 설치 기능을 갖춘 MCP 에이전트입니다.

## 설치 환경

---

- Rocky-8.10-x86_64-minimal.iso
- Virtual Box


## MCP 환경 설정

---

```json
{
    "mcpServers": {
        "k8s": {
            "request_timeout": "6000000",
            "command": "C:\\dev\\k8s_install_mcp\\.venv\\Scripts\\python.exe",
            "args": ["C:\\dev\\k8s_install_mcp\\src\\main.py"]
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
127.0.0.1:104로 root 사용자 1234 비밀번호로 k8s 마스터 노드 설치해줘  
```

### Client node 설치
```

```
