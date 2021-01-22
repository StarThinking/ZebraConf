package msx.thread;

import java.util.List;
import java.util.Map;
import java.util.ArrayList;

class Multi extends Thread {  
    public void run() {  
        System.out.println("Child Thread is running...");  
        System.out.println("Child Current Thread ID is " + Thread.currentThread().getId() + 
            " Name is " + Thread.currentThread().getName());
    } 

    private static void printStackTrace(StackTraceElement[] stack) {
        if (stack != null) {
            System.out.println("stack.length = " + stack.length);
            for (int i = 1; i < stack.length; i++) {
                StackTraceElement s = stack[i];
                System.out.println("\tat " + s.getClassName() + "." + s.getMethodName() + 
            	"(" + s.getFileName() + ":" + s.getLineNumber() + ")");
            }
        }
    }

    public static void main(String args[]) throws Exception {  
        System.out.println("Parent Current Thread ID is " + Thread.currentThread().getId() + 
            " Name is " + Thread.currentThread().getName());
        Multi t1 = new Multi(); 
        t1.setName("Child Thread");
        System.out.println("Thread Relation: " + Thread.currentThread().getId() + " -> " + t1.getId());
        t1.start();

	System.out.println("startStackMap:");
        Map<Long, StackTraceElement[]> startStackMap = Thread.getStartStackMap();
        for (Long tid : startStackMap.keySet()) {
	    System.out.println("tid = " + tid);
	    printStackTrace(startStackMap.get(tid));
        }
	
	System.out.println("initStackMap:");
        Map<Long, StackTraceElement[]> initStackMap = Thread.getInitStackMap();
        for (Long tid : initStackMap.keySet()) {
	    System.out.println("tid = " + tid);
	    printStackTrace(initStackMap.get(tid));
        }
    }  
}  
