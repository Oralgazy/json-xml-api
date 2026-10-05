# JSON -> XML API

POST /convert принимает JSON в теле запроса и возвращает XML.
Массивы превращаются в вложенные элементы <item>.

## Запуск локально
pip install -r requirements.txt
uvicorn main:app

## Запуск в Docker
docker build -t json-xml-api .
docker run --rm -p 8000:8000 json-xml-api

## Пример
curl -X POST http://localhost:8000/convert -H "Content-Type: application/json" --data-binary "@sample.json"