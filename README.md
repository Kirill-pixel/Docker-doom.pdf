# Docker-doom.pdf
Готовый Dockerfile для сборки контейнера
1. Сборка проекта, команда для корневой папки:
   ```
   docker build -t kirillpixel/kirill-project:doom.pdf .
   ```
2. Запуск контейнера:
   ```
   docker run -d -p 5050:5050 --name container-doom.pdf kirillpixel/kirill-project:doom.pdf 
   ```
