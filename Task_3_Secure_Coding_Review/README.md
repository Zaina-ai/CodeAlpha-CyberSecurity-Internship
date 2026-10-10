# CodeAlpha — Secure Coding Review

CodeAlpha Cyber Security Internship, Task 3. A small Python/SQLite login system reviewed for four common security weaknesses.

## Files
- `vulnerable_login.py` — deliberately insecure, local-only teaching example
- `secure_login.py` — corrected demonstration
- `SECURITY_REVIEW.md` — findings, evidence, remediation, and limitations
- `test_security.py` — unit tests

## Run
Requires Python 3.10+ and no external packages.

```bash
python -m unittest -v test_security.py
python secure_login.py
```

The vulnerable sample can be run locally with `python vulnerable_login.py` for demonstration. **Never deploy it or use real credentials.**

## Video walkthrough outline
Explain the project objective, show the four findings in `SECURITY_REVIEW.md`, compare vulnerable and secure code, run the tests, and conclude with key security lessons.
