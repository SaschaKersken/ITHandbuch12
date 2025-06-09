import org.w3c.dom.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;

public class XmlParser {
    public static void main(String[] args) {
        // Überprüfen, ob eine Datei als Argument übergeben wurde
        if (args.length < 1) {
            System.err.println("Verwendung: java XmlParser XML-DATEI");
            System.exit(1);
        }

        try {
            // XML-Dokument einlesen
            File xmlFile = new File(args[0]);
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse(xmlFile);

            // Whitespace-Knoten entfernen
            document.getDocumentElement().normalize();

            // Wurzelelement parsen
            parseElement(document.getDocumentElement(), 0);
        } catch (Exception e) {
            System.err.println("Fehler beim Parsen des XML-Dokuments: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static void parseElement(Node node, int indent) {
        String indentStr = " ".repeat(indent);

        // Element-Name ausgeben
        System.out.println(indentStr + "- " + node.getNodeName());

        // Falls das Element Attribute hat, diese ausgeben
        if (node.hasAttributes()) {
            NamedNodeMap attributes = node.getAttributes();
            for (int i = 0; i < attributes.getLength(); i++) {
                Node attr = attributes.item(i);
                System.out.println(indentStr + "  Attribut '" + attr.getNodeName() + "': '" + attr.getNodeValue() + "'");
            }
        }

        // Nur direkten Textinhalt des Elements ausgeben
        StringBuilder directText = new StringBuilder();
        NodeList children = node.getChildNodes();
        for (int i = 0; i < children.getLength(); i++) {
            Node child = children.item(i);
            if (child.getNodeType() == Node.TEXT_NODE) {
                directText.append(child.getTextContent().trim()).append(" ");
            }
        }
    
        // Falls direkter Text vorhanden ist, ausgeben
        String trimmedText = directText.toString().trim();
        if (!trimmedText.isEmpty()) {
            System.out.println(indentStr + "  Text: '" + trimmedText + "'");
        }

        // Rekursiv Kind-Elemente verarbeiten (ohne Text-Knoten)
        for (int i = 0; i < children.getLength(); i++) {
            Node child = children.item(i);
            if (child.getNodeType() == Node.ELEMENT_NODE) {
                parseElement(child, indent + 4);
            }
        }
    }
}
