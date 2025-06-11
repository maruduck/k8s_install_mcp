# MCP를 활용한 kubernetes 자동화 설치

---

## 설치 환경

- Rocky-8.10-x86_64-minimal.iso
- Virtual Box

---

## 환경 설정
```json
{
    "mcpServers": {
        "k8s": {
            "MCP_TIMEOUT": "6000000",
            "request_timeout": "6000000",
            "streaming_timeout": "30000000",
            "command": "C:\\dev\\k8s_install_mcp\\.venv\\Scripts\\python.exe",
            "args": ["C:\\dev\\k8s_install_mcp\\src\\main.py"]
        }
    }
}
```



## 설치 예시

타임 아웃 에러 발생 가능성이 있으므로 미리 update를 수행한 후 실행할 것
```bash
$ dnf update -y
```

```
127.0.0.1:104로 root 사용자 1234 비밀번호로 k8s 마스터 노드 설치해줘  
```

