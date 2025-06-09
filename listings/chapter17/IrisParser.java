import org.w3c.dom.*;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

public class IrisParser {
    public static List<Iris> parse() {
        var result = new ArrayList<Iris>();
        try {
            File irisFile = new File("iris-elements.xml");
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse(irisFile);
            document.getDocumentElement().normalize();
            // Die iris-Knoten sind Kind-Elemente des Wurzelknotens
            var root = document.getDocumentElement();
            var children = root.getChildNodes();
            for (int i = 0; i < children.getLength(); i++) {
                var iris = children.item(i);
                if (iris.getNodeType() != Node.ELEMENT_NODE) {
                    continue;
                }
                result.add(extractIrisFeatures(iris.getChildNodes()));
            }
        } catch (Exception e) {
            System.err.println("Fehler beim Parsen des XML-Dokuments: " + e.getMessage());
            e.printStackTrace();
        }
        return result;
    }
                
    private static Iris extractIrisFeatures(NodeList featureNodes) {
        var rawFeatures = new HashMap<String, String>();
        for (int i = 0; i < featureNodes.getLength(); i++) {
            var feature = featureNodes.item(i);
            rawFeatures.put(feature.getNodeName(), feature.getTextContent().trim());
        }
        return new Iris(
            Float.parseFloat(rawFeatures.get("sepal-length")),
            Float.parseFloat(rawFeatures.get("sepal-width")),
            Float.parseFloat(rawFeatures.get("petal-length")),
            Float.parseFloat(rawFeatures.get("petal-width")),
            rawFeatures.get("type")
        );
    }

    public static void main(String[] args) {
        var irises = parse();
        System.out.println("SEPAL LENGTH\tSEPAL WIDTH\tPETAL LENGTH\tPETAL WIDTH\tTYPE");
        irises.forEach(iris -> {
            System.out.println(iris.sepalLength() + "\t\t" + iris.sepalWidth() + "\t\t" + iris.petalLength() + "\t\t" + iris.petalWidth() + "\t\t" + iris.type());
        });
    }
}
