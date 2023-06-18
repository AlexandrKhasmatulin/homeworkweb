from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    def get_html_content(self):
        return """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <div class="container">
        <div class="row mt-5">
            <div class="col-3">
                <div class="card bg-primary" style="height: 40rem;">
                    <div class="card-body text-white">
                        <h3 class="card-title">Меню</h3>
                        <div class="row">
                            <a href="#" class="card-link text-white">Категории</a>
                            <a href="#" class="card-link text-white">Заказы</a>
                            <a href="#" class="card-link text-white">Контакты</a>
                           <select class="form-select" aria-label="Пример выбора по умолчанию">
                               <option selected>Пользователь</option>
                               <option value="1">Профиль</option>
                               <option value="2">Выход</option>
                           </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="card">
                    <div class="card" style="width: 50rem;">
                        <div class="card-body">
                            <h5 style="text-align:center;" class="card-title">Контакты</h5>
                            <div class="container">
                                <div class="row">
                                    <div class="col">
                                        <div class="mb-3">
                                            <label class="form-label">Имя</label>
                                            <input type="text" class="form-control" id="name" >
                                        </div>
                                        <div class="mb-3">
                                            <div class="col-auto">
                                                <label class="form-label">Почта</label>
                                            <div class="input-group">
                                            <div class="input-group-text">@</div>
                                                <input type="text" class="form-control" id="autoSizingInputGroup" >
                                            </div>
                                            </div>
                                        </div>
                                        <div class="mb-3">
                                            <label for="exampleFormControlTextarea1" class="form-label">Сообщение</label>
                                            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                                        </div>
                                    </div>
                                    <div class="col">
                                        <div class="card text-center">
                                        <div class="card-header">Наши Контакты</div>
                                            Для частных лиц
Контакт-центр

+7 495 777-48-88
для звонков по Москве и Московской области
8 800 100-48-88
звонок по России бесплатный
Премиум
Контакт-центр




                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
        </div>
  </body>
</html>"""
        """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
        """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        paige_content = self.get_html_content()
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(paige_content, "utf-8")) # Тело ответа

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
