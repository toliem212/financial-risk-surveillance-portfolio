from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_TOP_LEVEL = {"src", "app", "schema", "config", "data", "tests", ".github", ".streamlit"}
SECRET_PATTERNS = [
    re.compile(r"postgres(?:ql)?://[^\s<]+", re.I),
    re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"SUPABASE_SERVICE_ROLE_KEY\s*=\s*[^\s<]+"),
    re.compile(r"OPENAI_API_KEY\s*=\s*[^\s<]+"),
]

problems: list[str] = []
for name in FORBIDDEN_TOP_LEVEL:
    if (ROOT / name).exists():
        problems.append(f"forbidden production path: {name}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.name in {".env", "secrets.toml"}:
        problems.append(f"forbidden secret file: {path.relative_to(ROOT)}")
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            problems.append(f"possible secret in {path.relative_to(ROOT)}")

if problems:
    print("PUBLIC REPO CHECK: FAIL")
    for problem in problems:
        print(f"- {problem}")
    raise SystemExit(1)

print("PUBLIC REPO CHECK: PASS")
