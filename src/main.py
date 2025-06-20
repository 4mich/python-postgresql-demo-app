import psycopg2
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

# Get environment variables
postgresql_db_name = os.getenv("P_DB_NAME")
postgresql_port = os.getenv("P_PORT")
postgresql_user = os.getenv("P_USER")
postgresql_password = os.getenv("P_PASSWORD")
postgresql_host = os.getenv("P_HOST")


def connect_to_database(db, user, password, host, port):
    try:
        conn = psycopg2.connect(
            database=db,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print(f"[INFO] successfully connected to database {postgresql_db_name}")
    except psycopg2.Error as e:
        print(f"[ERROR] Failed connect to database: {e}")
        exit()


connect_to_database(db=postgresql_db_name,
                    user=postgresql_user,
                    password=postgresql_password,
                    host=postgresql_host,
                    port=postgresql_port
                    )

# Run simple http server
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')

httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()