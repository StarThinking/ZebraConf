import javassist.*;
import javassist.expr.*;
import java.util.*;

public class Convert {

    private static List<String> myGetMethods = new ArrayList<String>();

    static {
	myGetMethods.add("org.apache.hadoop.conf.Configuration.get(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getTrimmed(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getRaw(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.get(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getInt(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getInts(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getLong(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getLongBytes(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getFloat(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getDouble(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getBoolean(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getEnum(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getTimeDuration(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getTimeDurationHelper(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getTimeDurations(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getStorageSize(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getPattern(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getRange(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getStringCollection(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getStrings(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getTrimmedStringCollection(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getTrimmedStrings(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getClassByName(");
	myGetMethods.add("org.apache.hadoop.conf.Configuration.getClassByNameOrNull(");
    }
   
    public static void main(String[] args) {
	try {
            ClassPool classPool = ClassPool.getDefault();
            CtClass greetCtClass = classPool.get("org.apache.hadoop.conf.Configuration");
            
            CtMethod[] allMethods = greetCtClass.getMethods();
	    for (CtMethod cm : allMethods) {
		if (cm.isEmpty())
		    continue;
		for (String get : myGetMethods) {
		    if (cm.getLongName().startsWith(get)) {
		    	    //System.out.println("cm name: " + cm.getLongName());
			//cm.insertAfter( "LOG.info( \"msx-conf return value \" + $_ );");
			cm.insertAfter( "prerunFetchReturnValue(name, String.valueOf($_));");
			//cm.insertAfter("System.out.println(\"msx-conf message from javassist\");");
			//cm.insertAfter( "System.out.println( \"its \" + $_ );");
			//cm.insertAfter( "System.exit(-1);");
			break;
		    }
		}
	    }

            greetCtClass.writeFile("./gen");
	} catch(Exception e) {
	    e.printStackTrace();
	}
    }
}
