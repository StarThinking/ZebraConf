package com.tianshouzhi;

import javassist.*;
 
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
 
public class UserGenerator {
    public static void main(String[] args) throws Exception {
        ClassPool classPool = ClassPool.getDefault();
        //定义User类
        CtClass ctClassUser = classPool.makeClass("com.tianshouzhi.User");
 
        //定义name字段
        CtClass fieldType = classPool.get("java.lang.String");//字段类型
        String name = "name";//字段名称
        CtField ctFieldName=new CtField(fieldType, name,ctClassUser);
        ctFieldName.setModifiers(Modifier.PRIVATE);//设置访问修饰符
        ctClassUser.addField(ctFieldName, CtField.Initializer.constant("javasssit"));//添加name字段，赋值为javassist
 
        //定义构造方法
        CtClass[] parameters = new CtClass[]{classPool.get("java.lang.String")};//构造方法参数
        CtConstructor constructor=new CtConstructor(parameters,ctClassUser);
        String body = "{this.name=$1;}";//方法体 $1表示的第一个参数
        constructor.setBody(body);
        ctClassUser.addConstructor(constructor);
 
        //setName getName方法
        ctClassUser.addMethod(CtNewMethod.setter("setName",ctFieldName));
        ctClassUser.addMethod(CtNewMethod.getter("getName",ctFieldName));
 
        //toString方法
        CtClass returnType = classPool.get("java.lang.String");
        String methodName = "toString";
        CtMethod toStringMethod=new CtMethod(returnType, methodName, null,ctClassUser);
        toStringMethod.setModifiers(Modifier.PUBLIC);
        String methodBody = "{return \"name=\"+$0.name;}";//$0表示的是this
        toStringMethod.setBody(methodBody);
        ctClassUser.addMethod(toStringMethod);
 
        //代表class文件的CtClass创建完成，现在将其转换成class对象
        Class clazz = ctClassUser.toClass();
        Constructor cons = clazz.getConstructor(String.class);
        Object user = cons.newInstance("wangxiaoxiao");
        Method toString = clazz.getMethod("toString");
        System.out.println(toString.invoke(user));
 
        ctClassUser.writeFile(".");//在当前目录下，生成com/tianshouzhi/User.class文件
    }
}
