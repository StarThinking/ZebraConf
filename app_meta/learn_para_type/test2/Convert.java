import javassist.*;
import javassist.expr.*;

public class Convert {
    public static void main(String[] args) {
	try {
            ClassPool classPool = ClassPool.getDefault();
            CtClass greetCtClass = classPool.get("Greet");
            
            greetCtClass.instrument(new ExprEditor() {
                @Override
                public void edit(FieldAccess fieldAccess) throws CannotCompileException {
                    if (fieldAccess.getFieldName().equals("knowncount")) {
                        fieldAccess.replace(" { System.out.println(\"A read operation on a field is encountered \"); $_ = $proceed($$); } ");
                    }
                }
            });
             
            CtField f = new CtField(CtClass.intType, "z", greetCtClass);
            f.setModifiers(Modifier.STATIC | Modifier.PUBLIC);
            greetCtClass.addField(f);
           
            CtMethod[] allMethods = greetCtClass.getMethods();
	    for (CtMethod cm : allMethods) {
		//System.out.println("cm name: " + cm.getName());
		if (cm.getName().equals("get") || cm.getName().equals("getBoolean")) {
		    System.out.println("cm name: " + cm.getName());
		    cm.insertAfter( "System.out.println( $_ );");
		}
	    }

            greetCtClass.writeFile("./gen");
	} catch(Exception e) {
	    e.printStackTrace();
	}
    }
}
