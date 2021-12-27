import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080


def center_str(s: str, f: str = None) -> str:
	return (" " + s + " ").center(os.get_terminal_size().columns, f or "-")

class Server(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		with open("html/index.html", "rb") as file:
			self.wfile.write(file.read())


def main():
	server = HTTPServer((HOST, PORT), Server)

	print()
	print(center_str(f"Server Running at http://{HOST}:{PORT}", "="))
	print(center_str('PRESS CTRL + C TO CLOSE', "-"))
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.server_close()
		print(center_str("Server Closed"))


if __name__ == "__main__":
	main()
