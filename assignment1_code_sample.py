import os
import pymysql
from urllib.request import urlopen

# QWSAP A05: Security Misconfiguration
# Hard coded credentials, possible fix would be to use environmental variable.
db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

# OWSAP A03: Injection
# No validation is performed on user input.
def get_user_input():
    user_input = input('Enter your name: ')
    return user_input


# NG - OWASP A03: Injection
# Sends the request directly to the server making it vulnerable to
# SQL injection. I've found that using a more secure library would assist in
# making this function work without this vulnerability.
def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')


# NG - OWASP A02: Cryptographic Failures
# HTTP is used instead of HTTPS which does not encrypt the data.
# A better solution is to use HTTPS

# NG - OWASP A08: Software and Data Integrity Failures
# There are no checks to make sure that the data coming in is secure.
# TO fix this we would want to verify the security of the incoming data.
def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

# OWSAP A03: Injection
# The String query uses untrusted data which can allow SQL injection.
def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
