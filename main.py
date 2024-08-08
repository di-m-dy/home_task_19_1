"""
Гляавный модуль для запуска
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

from config import HOST, PORT, static_files_path


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    @staticmethod
    def __send_index():
        """Метод возварщает главную страничку"""
        with open(static_files_path('index.html')) as file:
            page = file.read()
        return page

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.__send_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((HOST, PORT), MyServer)
    print("Server started http://%s:%s" % (HOST, PORT))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
