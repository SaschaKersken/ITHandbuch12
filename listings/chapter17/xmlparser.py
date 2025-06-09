from xml.etree import ElementTree
from sys import argv, exit
import re

# Ein XML-Element rekursiv parsen
def parse_element(element, indent = 0):
    # Name des Tags
    print(f"{indent * ' '}- {element.tag}")
    # Text, falls vorhanden
    if element.text and re.search("\S", element.text):
        print(f"  {indent * ' '}Text: '{element.text.strip()}'")
    # Attribute, falls vorhanden
    for name in element.attrib:
        print(f"  {indent * ' '}Attribut '{name}': '{element.attrib[name]}'")
    # Rekursiver Aufruf für Kind-Elemente, falls vorhanden
    for child in element:
        parse_element(child, indent + 4)

# Diverse Fehler abfangen
if len(argv) < 2:
    print(f"Verwendung: python3 {argv[0]} XML-DATEI")
    exit()
try:
    doc = ElementTree.parse(argv[1])
except FileNotFoundError:
    print("XML-Datei existiert nicht.")
    exit()
except ElementTree.ParseError as e:
    print(f"Parserfehler: {e}")
    exit()
# Wurzelelement des Dokuments parsen
parse_element(doc.getroot())
