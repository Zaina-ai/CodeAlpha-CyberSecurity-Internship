"""Defensive login demonstration with parameterized queries and salted PBKDF2 hashes."""
import hashlib
import hmac
import os
import sqlite3
import time
from getpass import getpass

ITERATIONS = 600_000
MAX_ATTEMPTS = 3

def hash_password(password, salt=None):
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, ITERATIONS)
    return salt.hex(), digest.hex()

def verify_password(password, salt_hex, expected_hex):
    candidate = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt_hex), ITERATIONS)
    return hmac.compare_digest(candidate, bytes.fromhex(expected_hex))

def run_demo():
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE users (username TEXT PRIMARY KEY, salt TEXT NOT NULL, password_hash TEXT NOT NULL)')
    demo_password = os.environ.get('DEMO_PASSWORD') or getpass('Set demo account password: ')
    if not demo_password:
        print('Password must not be empty')
        return
    salt, digest = hash_password(demo_password)
    conn.execute('INSERT INTO users VALUES (?, ?, ?)', ('demo', salt, digest))
    for attempt in range(MAX_ATTEMPTS):
        username = input('Username: ')
        password = getpass('Password: ')
        row = conn.execute('SELECT salt, password_hash FROM users WHERE username = ?', (username,)).fetchone()
        if row and verify_password(password, row[0], row[1]):
            print('Login successful')
            break
        print('Login failed')
        if attempt < MAX_ATTEMPTS - 1:
            time.sleep(1)
    else:
        print('Too many attempts; session ended')
    conn.close()

if __name__ == '__main__':
    run_demo()
