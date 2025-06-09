from xml.etree import ElementTree

doc = ElementTree.parse('iris-elements.xml')
root = doc.getroot()
irises = []
for iris in root.findall('iris'):
    irises.append([
        float(iris[1].text),
        float(iris[2].text),
        float(iris[3].text),
        float(iris[4].text),
        iris[0].text
    ])
print(f"{len(irises)} Datensätze importiert.")
print(irises[0])
print(irises[50])
print(irises[100])
