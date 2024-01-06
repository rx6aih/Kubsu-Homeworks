#!/usr/bin/env python3
import http.server
import socketserver
import os

# Устанавливаем директорию, содержащую ваши CGI-скрипты
cgi_directory = os.path.join(os.getcwd(), 'cgi-bin')

# Создаем сервер с поддержкой CGI
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = [cgi_directory]

# Задаем порт (в данном случае, 8000)
port = 8080

# Запускаем сервер
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port}")
    httpd.serve_forever()
