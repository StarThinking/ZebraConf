import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;

public class ReadXMLFile {

    private static final String ELEMENT_NAME = "property";
  
    public static void getAllParameters(String xmlPath) {
        try {
    	    File xmlFile = new File(xmlPath);
    	    DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
    	    DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
    	    Document doc = dBuilder.parse(xmlFile);
    
    	    doc.getDocumentElement().normalize();
    	    //System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
    
    	    NodeList nList = doc.getElementsByTagName(ELEMENT_NAME);
    	    for (int i=0; i<nList.getLength(); i++) {
    	        Node nNode = nList.item(i);
    	        if (nNode.getNodeType() == Node.ELEMENT_NODE) {
    	    	    Element eElement = (Element) nNode;
    	    	    //System.out.println("name : " + eElement.getElementsByTagName("name").item(0).getTextContent());
    	    	    //System.out.println("value : " + eElement.getElementsByTagName("value").item(0).getTextContent());
    	    	    //System.out.println("");
		    System.out.println(eElement.getElementsByTagName("name").item(0).getTextContent());
    	        }
    	    }
    	    //System.out.println("number of " + ELEMENT_NAME + " is " + nList.getLength());
        } catch (Exception e) {
    	    e.printStackTrace();
        }
    }
    
    public static void getParameterValue(String xmlPath) {
        try {
    	    File xmlFile = new File(xmlPath);
    	    DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
    	    DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
    	    Document doc = dBuilder.parse(xmlFile);
    
    	    doc.getDocumentElement().normalize();
    	    //System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
    
    	    NodeList nList = doc.getElementsByTagName(ELEMENT_NAME);
    	    for (int i=0; i<nList.getLength(); i++) {
    	        Node nNode = nList.item(i);
    	        if (nNode.getNodeType() == Node.ELEMENT_NODE) {
    	    	    Element eElement = (Element) nNode;
    	    	    System.out.print(eElement.getElementsByTagName("name").item(0).getTextContent());
		    if (eElement.getElementsByTagName("value").item(0) != null) {
			System.out.print(" " + eElement.getElementsByTagName("value").item(0).getTextContent());
		    }
    	    	    System.out.println("");
    	        }
    	    }
    	    //System.out.println("number of " + ELEMENT_NAME + " is " + nList.getLength());
        } catch (Exception e) {
    	    e.printStackTrace();
        }
    }
    
    public static void getNoDefaultValueParameters(String xmlPath) {
        try {
    	    File xmlFile = new File(xmlPath);
    	    DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
    	    DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
    	    Document doc = dBuilder.parse(xmlFile);
    
    	    doc.getDocumentElement().normalize();
    	    //System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
    
    	    NodeList nList = doc.getElementsByTagName(ELEMENT_NAME);
    	    for (int i=0; i<nList.getLength(); i++) {
    	        Node nNode = nList.item(i);
    	        if (nNode.getNodeType() == Node.ELEMENT_NODE) {
    	    	    Element eElement = (Element) nNode;
		    if (eElement.getElementsByTagName("value").item(0) == null ||
				eElement.getElementsByTagName("value").item(0).getTextContent().equals("")) {
    	    	        System.out.println(eElement.getElementsByTagName("name").item(0).getTextContent());
		    }
    	        }
    	    }
    	    //System.out.println("number of " + ELEMENT_NAME + " is " + nList.getLength());
        } catch (Exception e) {
    	    e.printStackTrace();
        }
    }
 
    public static void discriptionContainsEnable(String xmlPath, String parameter) {
        try {
    	    File xmlFile = new File(xmlPath);
    	    DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
    	    DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
    	    Document doc = dBuilder.parse(xmlFile);
    
    	    doc.getDocumentElement().normalize();
    	    //System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
    
    	    NodeList nList = doc.getElementsByTagName(ELEMENT_NAME);
    	    for (int i=0; i<nList.getLength(); i++) {
		Node nNode = nList.item(i);
		if (nNode.getNodeType() == Node.ELEMENT_NODE) { 
    	            Element eElement = (Element) nNode;
		    if (!eElement.getElementsByTagName("name").item(0).getTextContent().equals(parameter))
		        continue;
	            if (eElement.getElementsByTagName("description").item(0) != null) {
			String desc = eElement.getElementsByTagName("description").item(0).getTextContent();
			if (desc.contains("Enable") || desc.contains("Disable") || desc.contains("enable") || desc.contains("disable")) { 
			    System.out.print("yes");
			} else {
			    System.out.print("no");
			}
	            }
		}
    	    }
    	    //System.out.println("number of " + ELEMENT_NAME + " is " + nList.getLength());
        } catch (Exception e) {
    	    e.printStackTrace();
        }
    }

    public static void main(String args[]) { 
	String xmlPath = args[0];
	String cmd = args[1];
        String argument = "";
	if (args.length == 3)
 	    argument = args[2];
	
	switch (cmd) {
	    case "getNoDefaultValueParameters":
		getNoDefaultValueParameters(xmlPath);
	        break;
	    case "getParameterValue":
		getParameterValue(xmlPath);
		break;
	    case "getAllParameters":
		getAllParameters(xmlPath);
		break;
	    case "discriptionContainsEnable":
		discriptionContainsEnable(xmlPath, argument);
		break;
	    default:
		System.out.println("Error: wrong cmd " + cmd);
	}
	//getAllParameters(xmlPath);
    }
}
