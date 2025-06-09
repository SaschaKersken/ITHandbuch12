from xml.etree import ElementTree

doc = ElementTree.parse('iris-elements.xml')
root = doc.getroot()
irises = []
for iris in root.findall('iris'):
    irises.append([
        float(iris.attrib['sepal-length']),
        float(iris.attrib['sepal-width']),
        float(iris.attrib['petal-length']),
        float(iris.attrib['petal-width']),
        iris.attrib['type']
    ])
print(f"{len(irises)} Datensätze importiert.")
print(irises[0])
print(irises[50])
print(irises[100])
