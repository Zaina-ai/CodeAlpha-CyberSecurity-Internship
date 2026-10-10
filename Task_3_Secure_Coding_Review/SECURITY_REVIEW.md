# Secure Coding Review — Python Login System

**Internship:** CodeAlpha Cyber Security — Task 3  
**Scope:** Local, intentionally vulnerable Python/SQLite demonstration; no real users or production systems.

## Method
Manual source-code review of `vulnerable_login.py`, comparison against `secure_login.py`, and unit tests for password hashing. Findings are limited to this demonstration.

| ID | Finding | Evidence | Risk | Remediation |
|---|---|---|---|---|
| F1 | Hardcoded credential | `ADMIN_PASSWORD = 'admin123'` | Exposes a secret to anyone reading the source | Remove embedded secrets; collect a demo password at runtime or use a properly managed secret |
| F2 | Plaintext password storage | `INSERT INTO users VALUES ... ('demo', 'password123')` | Database disclosure reveals usable passwords | Store unique salts and slow password hashes (PBKDF2-HMAC-SHA256) |
| F3 | SQL injection | SQL built with an f-string containing user input | Input may change query logic and bypass authentication | Use SQLite parameterized queries (`?` placeholders) |
| F4 | Unlimited login attempts | Single authentication path has no failure threshold; rerunning allows retries | Enables repeated password guessing | Cap attempts per session and delay retries; production systems additionally need persistent account/IP rate limiting |

## Corrected implementation
`secure_login.py` uses parameterized queries, random salts, PBKDF2-HMAC-SHA256 with 600,000 iterations, constant-time hash comparison, hidden password entry, and three attempts per run. It uses an in-memory database and does not represent a production authentication service.

## How to reproduce safely
1. Install Python 3.10+; no external packages needed.
2. Run `python vulnerable_login.py` with synthetic inputs only. Do not expose it to a network.
3. Run `python secure_login.py`; choose a demo password and test success/failure.
4. Run `python -m unittest -v test_security.py`.

## Limitations and next steps
The secure example is educational. Real deployment would need persistent rate limiting across sessions, a vetted authentication framework, secure session management, audit logging, MFA, and secure password-reset flows. Do not deploy the vulnerable version.

## Testing Results

The applications were tested locally using Python and
SQLite in Visual Studio Code.

| Test | Observed Result | Status |
|---|---|---|
| Vulnerable login with valid credentials | Login successful | Passed |
| SQL injection against vulnerable login | Authentication bypassed | Vulnerability confirmed |
| Secure login with valid credentials | Login successful | Passed |
| SQL injection against secure login | Login failed | Attack rejected |
| Automated password-security tests | 3 tests passed | Passed |

The SQL injection test demonstrated that the vulnerable
application accepted malicious input without requiring
the correct password. The secure implementation rejected
the same input. All three automated password-security
tests passed.

## Conclusion
Four security issues were identified through manual review. The revised implementation demonstrates practical mitigations and the included tests check password hashing behavior.
