"""API: принимает JSON в теле запроса, возвращает XML."""
import json

from fastapi import FastAPI, HTTPException, Request, Response

from converter import json_to_xml

app = FastAPI(title="JSON to XML converter")


@app.post("/convert")
async def convert(request: Request):
    raw = await request.body()
    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(status_code=400, detail="Тело запроса не является корректным JSON")

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + json_to_xml(data)
    return Response(content=xml, media_type="application/xml")