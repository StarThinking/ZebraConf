package msx.instrument;

import javassist.*;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
 
public class Instrumentor {
    public static void main(String[] args) throws Exception {
        ClassPool classPool = ClassPool.getDefault();
        //classPool.importPackage("java.lang.System");
        CtClass iClass = classPool.get("java.lang.Thread");
        
        CtField iField = new CtField(CtClass.intType, "msx_tmp", iClass);
        iField.setModifiers(Modifier.STATIC | Modifier.PUBLIC);
        iClass.addField(iField);

        //CtMethod iMethod = iClass.getDeclaredMethod("start");
        //method.insertBefore("System.out.println(\"hello from Instrumentor: \" + Thread.currentThread().getId());");
        //iMethod.insertBefore("java.lang.System.out.println(\"hello\");");
        //iMethod.insertBefore("msx_tmp=\"111\";");
        iClass.writeFile("/root/javassist_study/thread/gen/");
    }
}
