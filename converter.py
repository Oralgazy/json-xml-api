"""Преобразование JSON-объекта в XML."""
import re
import xml.etree.ElementTree as ET


def _tag(name):
    """Имя тега XML: недопустимые символы заменяем на _, начало не с цифры."""
    name = re.sub(r"[^\w.\-]", "_", str(name), flags=re.UNICODE)
    if not name or not (name[0].isalpha() or name[0] == "_"):
        name = "_" + name
    return name


def _text(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _fill(parent, value):
    """Рекурсивно заполняет элемент parent значением value."""
    if isinstance(value, dict):
        for key, val in value.items():
            _fill(ET.SubElement(parent, _tag(key)), val)
    elif isinstance(value, list):
        for val in value:
            _fill(ET.SubElement(parent, "item"), val)
    elif value is not None:
        parent.text = _text(value)


def json_to_xml(data, root="root"):
    """JSON (dict/list/значение) -> строка XML."""
    element = ET.Element(_tag(root))
    _fill(element, data)
    ET.indent(element)  # отступы для читаемости
    return ET.tostring(element, encoding="unicode")