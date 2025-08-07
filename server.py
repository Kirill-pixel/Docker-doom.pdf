import http.server
import socketserver
import os

PORT = 5050

class PDFHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Если запрос идет на корень '/', то отдаем index.pdf
        if self.path == '/':
            self.path = '/index.pdf'
        
        # Вызываем родительский do_GET для обработки файла
        # Он найдет файл 'index.pdf' в текущей директории
        return super().do_GET()

    def end_headers(self):
        # Этот блок кода остается без изменений, он нужен для правильных заголовков
        if self.path.endswith('.pdf'):
            self.send_header('Content-type', 'application/pdf')
        
        # Добавляем заголовки для предотвращения кэширования
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

# Запускаем сервер
with socketserver.TCPServer(("", PORT), PDFHandler) as httpd:
    print(f"Serving files from {os.getcwd()} on port {PORT}")
    httpd.serve_forever()