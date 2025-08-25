import os
import httpx
from typing import Tuple

MODE = os.getenv("JUDGE_MODE", "mock").lower()
JUDGE0_URL = os.getenv("JUDGE0_URL", "").rstrip("/")
LANG_PY = int(os.getenv("JUDGE0_LANG_PY", 71))
LANG_JAVA = int(os.getenv("JUDGE0_LANG_JAVA", 62))

class Judge:
    @staticmethod
    async def run(language: str, code: str, stdin: str) -> Tuple[str, int]:
        """Return (stdout, time_ms). In mock mode, echoes input."""
        if MODE == "mock" or not JUDGE0_URL:
            return stdin.strip(), 0  # echo mode
        lang_id = LANG_PY if language == "python" else LANG_JAVA
        payload = {
            "language_id": lang_id,
            "source_code": code,
            "stdin": stdin,
        }
        url = f"{JUDGE0_URL}/submissions?base64_encoded=false&wait=true"
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(url, json=payload)
            r.raise_for_status()
            data = r.json()
            return (data.get("stdout") or "", int((data.get("time") or 0) * 1000))
