"""INTENTIONALLY INSECURE demo. Run only with synthetic data locally."""
import sqlite3

DB = ':memory:'
ADMIN_PASSWORD = 'admin123'  # Finding 1: hardcoded credential

def run_demo():
    conn = sqlite3.connect(DB)
    conn.execute('CREATE TABLE users (username TEXT, password TEXT)')
    conn.execute('INSERT INTO users VALUES (?, ?)', ('demo', 'password123'))  # Finding 2: plaintext
    username = input('Username: ')
    password = input('Password: ')
    query = f"SELECT username FROM users WHERE username = '{username}' AND password = '{password}'"  # Finding 3: SQL injection
    try:
        print('Login successful' if conn.execute(query).fetchone() else 'Login failed')
    except sqlite3.Error as exc:
        print('Database error:', exc)
    # Finding 4: no attempt limit / lockout
    conn.close()

if __name__ == '__main__':
    run_demo()
