# Шпаргалка по Docker

<a href="https://www.youtube.com/watch?v=_uZQtRyF6Eg&t=1725s&ab_channel=BogdanStashchuk">Туториал</a>

<a href="https://docs.docker.com/engine/install/ubuntu/">Docker engine для Ubuntu</a>

<a href="https://itsecforu.ru/2018/04/12/%D0%BA%D0%B0%D0%BA-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-docker-%D0%B1%D0%B5%D0%B7-sudo-%D0%BD%D0%B0-ubuntu/">Как использовать docker без sudo на ubuntu</a>

<a href="https://hub.docker.com/">DockerHub</a>

## Основные команды

> Проверить версию Докера <br>
> Показывет информацию о клиенте и сервере
>```shell
>   docker version
>```

> Список всех контейнеров присутствующих в Докере
>```shell
>   docker ps -a
>```

> Список локальных образов
>```shell
>   docker images
>```

> Создать и запустить контейнер
>```shell
>   docker run IMAGE-NAME
>```
> Равносильно команде с тэгом
>```shell
>   docker run IMAGE-NAME:latest
>```

> Запуск контейнера в фоновом режиме с помощью флага -d
>```shell
>   docker run -d IMAGE-NAME
>```

> Удалить контейнер
>```shell
>   docker rm CONTAINERS-NAME-OR-ID
>```

> Активировать контейнер
>```shell
>   docker start CONTAINERS-NAME-OR-ID
>```

> Остановить контейнер
>```shell
>   docker stop CONTAINERS-NAME-OR-ID
>```

> Остановить контейнер принудительно
>```shell
>   docker kill CONTAINERS-NAME-OR-ID
>```

> Удалить все остановленные контейнеры
>```shell
>   docker container prune
>```

> Информация о контейнере
>```shell
>   docker inspect CONTAINERS-NAME-OR-ID
>```

> Выполнить команду в **запущенном** контейнере
>```shell
>   docker exec -it CONTAINERS-NAME-OR-ID PROCESS-NAME
>```

> Создать контейнер с именем с помощью --name
>```shell
>   docker run --name YourCustomName IMAGE-NAME
>```

> Mapping портов с помощью -p "public"
>```shell
>   docker run -p YourPort:CONTAINERS-PORT IMAGE-NAME
>```
> PS Порт контейнеров можно узнать с помощью *docker ps -a*

> Mapping томов с помощью -v "volume"
>```shell
>   docker run -v YourDirPath:ContainerDirPath IMAGE-NAME
>```

## Основные действия сделанные в процессе туториала

> Создаем и запускаем контейнер по образу <a href="https://hub.docker.com/_/hello-world">hello-world</a>, который выведет инструкцию о том, как Докер создает контейнер из DockerHub 
>```shell
>   docker run hello-world
>```
>![Image alt](https://github.com/NemoZon/MDimages/raw/main/docker/ss0.png)

> Проверяем наличие контейнера
>```shell
>   docker ps -a
>```
>![Image alt](https://github.com/NemoZon/MDimages/raw/main/docker/ss1.png)

> Удаляем контейнер
>```shell
>   docker rm a178cffcf5af
>```

> Создадим контейнер <a href="https://hub.docker.com/_/busybox">busybox</a>
>```shell
>   docker run busybox
>```
> Контейнер автоматически остановлен, из за того, что его процесс/вывод ни куда не передается

> Подключимся к процессу с помощью опций -i "интерактивный" и -t "терминал"
>```shell
>   docker run -it busybox
>```

> Команда введеная внутри оболочки выведет ID контейнера
>```shell
>   hostname
>```

> Команда введеная внутри оболочки выведет IP контейнера
>```shell
>   hostname -i
>```

> Команда введеная внутри оболочки для выхода из контейнера
>```shell
>   exit
>```

> Создадим контейнер <a href="https://hub.docker.com/_/nginx">nginx</a>
>```shell
>   docker run -d nginx
>```
> Без флага -d терминал подключится автоматически к логам nginx

> Ищем ip адрес контейнера
>```shell
>   docker inspect 4d8fd273c4b2 | grep IPAddress
>```
> В моем случае это 172.17.0.2, подключиться к этому адресу пока что нельзя, для этого нужно выполнить **mapping портов**

> Запустим оболочку bash внутри контейнера nginx
>```shell
>   docker exec -it 4d8fd273c4b2 bash 
>```

> Перейдем в папку, в которой находится index.html
>```shell
>   cd /usr/share/nginx/html
>   cat index.html
>```
> Этот файл будет передан всем клиентам, которые будут подключаться к сервису nginx с tcp портом 80

> Останавливаем и удаляем все контейнеры
>```shell
>   exit
>   docker stop 4d8fd273c4b2
>   docker container prune
>```

> Создаем новый контейнер с внешним портом 8080 для порта контейнера 80 и именем my_nginx в фоновом режиме
>```shell
>   docker run -d --name my_nginx -p 8080:80 nginx
>```
> Теперь если перейти по localhost:8080 в вашем браузере вы увидете тот самый index.html, но если мы захотим изменить этот файл, нам потребуется выполнить **mapping томов**

> Создаю папку nginx и файл index.html с базовым кодом

> Остановлю и удалю все ранее созданные контейнеры
>```shell
>   docker stop 371fad22e7b3
>   docker container prune
>```

> Создадим новый контейнер с мепингом портов и томов в фоновом режиме
>```shell
>   docker run -v ${PWD}:/usr/share/nginx/html -p 8080:80 -d nginx
>```
> *Я использую переменную ${PWD}, так как нахожусь в папке nginx <br>
> Перейдем на localhost:8080 и убедимся, что страница поменялась

> Перейдем в bash контейнера и убедимся, что index.html берется из папки nginx
>```shell
>   docker exec -it 44db02c2c35e bash
>   cd /usr/share/nginx/html/
>   cat index.html
>```
> ![Image alt](https://github.com/NemoZon/MDimages/raw/main/docker/ss2.png)

> Так же я создал script.js и style.css, которые так же присутствуют в /usr/share/nginx/html контейнера