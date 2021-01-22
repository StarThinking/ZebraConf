
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
	long time1 = System.nanoTime();
	System.out.println("before create child thread " + time1);
        Multi t1 = new Multi(); 
	long time2 = System.nanoTime();
	System.out.println("after create child thread " + time2);
        System.out.println("Thread Relation: " + Thread.currentThread().getId() + " -> " + t1.getId());
        //t1.start();
	List<Long[]> threadRelation = getThreadInitRelation();
	for (Long[] r : threadRelation) {
	    if (r[2] >= time1 && r[2] <= time2) 
	    System.out.println("thread " + r[0] + " creates thread " + r[1] + " at time " + r[2]);
	}
    }  
}  
