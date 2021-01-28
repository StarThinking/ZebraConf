import java.util.*;
import java.text.SimpleDateFormat;

public class HConfRunner extends RunnerCore {
    // run or hypothesis
    private static String MY_TYPE = "";
    private static final int MAX_HYPO_RUN = 20;
    private static final double LONG_TIME_MUL = 2.0;

    public static void main(String[] args) {
        int rc = 0;
        long startTime, endTime, timeElapsed;
        startTime = endTime = timeElapsed = 0; 
        
        final int minArguments = 5;
        int h_list_size = 0;
        String proj = "";
        String u_test = "";
        String h_list = "";

        if (args.length < minArguments) {
            System.out.println("Error: args length is " + args.length);
            System.out.println("HConfRunner [h_list_size] [run|hypothesis] [testProject] [unitTest] [parameter,component,reconfPoint,v1,v2] ...");
            System.exit(1);
        }
      
        // assign arguments
        h_list_size = Integer.valueOf(args[0]);
        MY_TYPE = args[1];
        proj = args[2];
        u_test = args[3];
        StringBuilder sb = new StringBuilder();
        for (int j=4; j < args.length; j++) {
            sb.append(args[j]);
            if (j < (args.length - 1))
                sb.append(" ");
        }
        h_list = sb.toString();

        // display arguments
        System.out.println("my_type=" + MY_TYPE);
        System.out.println("proj=" + proj);
        System.out.println("u_test=" + u_test);
        System.out.println("h_list[" + h_list.split(" ").length + "]=" + h_list);
      
        // create a TestResult with basic test info
        TestResult test_basic = new TestResult(proj, u_test, h_list);
	if (!test_basic.isValid()) {
	    System.out.println("ERROR: invalid TestResult");
	    System.exit(1);
	}

        try { 
	    startTime = System.nanoTime();
            if (MY_TYPE.equals("run")) {
                rc = runTestLogic(h_list_size, test_basic);
            } else if (MY_TYPE.equals("hypothesis")) {
                hypothesisTestLogic(test_basic);
            } else {
                System.out.println("ERROR: wrong MY_TYPE " + MY_TYPE);
            }
            endTime = System.nanoTime();
            timeElapsed = endTime - startTime;
	} catch(Exception e) {
	    System.out.println("ERROR: met exception during test:");
	    e.printStackTrace();
	    // set to 0 to filter out false +
	    rc = 0;
	} finally {
            System.out.println("Total execution time in seconds : " + timeElapsed / 1000000000);
            System.out.println(rc);
	    System.exit(rc);
        }
    }

    private static void hypothesisTestLogic(TestResult test_basic) throws Exception {
	int v1v2FailedCount = 0;
	int v1v1v2v2FailedCount = 0;
        int earlyStopThreshold = 3;
	boolean earlyStop = false;
        int i = 0;

        System.out.println(test_basic.toString());

        for (i=0; i<MAX_HYPO_RUN; i++) {
	    if ( (v1v2FailedCount >= earlyStopThreshold && v1v1v2v2FailedCount == 0) ||
                    (i >= earlyStopThreshold && v1v2FailedCount == 0) ||
                    v1v1v2v2FailedCount >= earlyStopThreshold )  {
		System.out.println("early stop after " + earlyStopThreshold + " is satisfied");
		earlyStop = true;
		break;
	    }

	    TestResult v1v2Test = new TestResult(test_basic);
            v1v2Test.vv_mode = "v1v2";
            runTestCore(v1v2Test);
            if (v1v2Test.ret == RETURN.FAIL) {
                System.out.println("---> v1v2 test failed.");
		System.out.println(v1v2Test.completeInfo());
                v1v2FailedCount ++;
            } else {
                System.out.println("---> v1v2 test suceeded.");
            }

            TestResult v1v1Test = new TestResult(test_basic);
            v1v1Test.vv_mode = "v1v1";
            runTestCore(v1v1Test);
            TestResult v2v2Test = new TestResult(test_basic);
            v2v2Test.vv_mode = "v2v2";
            runTestCore(v2v2Test);
            if (v1v1Test.ret == RETURN.FAIL || v2v2Test.ret == RETURN.FAIL) {
                System.out.println("---> v1v1 or v2v2 test failed.");
		if (v1v1Test.ret == RETURN.FAIL) {
                    System.out.println("v1v1 failed in a hypo test");
		    System.out.println(v1v1Test.completeInfo());
                }
		if (v2v2Test.ret == RETURN.FAIL) {
                    System.out.println("v2v2 failed in a hypo test");
		    System.out.println(v2v2Test.completeInfo());
                }
                v1v1v2v2FailedCount ++;
            } else {
                System.out.println("---> v1v1 and v2v2 test test suceeded.");
            }
        }

	System.out.println("v1v2 failed with probability " + v1v2FailedCount + " out of " + i);
        System.out.println("v1v1v2v2 failed with probability " + v1v1v2v2FailedCount + " out of " + i);

        return;
    }

    private static int runTestLogic(int h_list_size, TestResult test_basic) throws Exception {
        // clone to create v1v2 test and run it
        TestResult v1v2Test = new TestResult(test_basic);
        v1v2Test.vv_mode = "v1v2";
        System.out.println(v1v2Test.toString());
        runTestCore(v1v2Test);
        if (v1v2Test.ret == RETURN.SUCCEED) {
            System.out.println("v1v2 test succeeded, no issue.");
            return 0;
        } else if (v1v2Test.ret == RETURN.FAIL) {
            if (h_list_size > 1) { // return 1 for group test
                System.out.println("always return 1 when group test fails");
                return 1;
            } else {
                TestResult v1v1Test = new TestResult(test_basic);
                v1v1Test.vv_mode = "v1v1";
                runTestCore(v1v1Test);
                if (v1v1Test.ret == RETURN.FAIL) { // invalid
                    System.out.println("invalid value v1");
                    return 0;
                }
            
                TestResult v2v2Test = new TestResult(test_basic);
                v2v2Test.vv_mode = "v2v2";
                runTestCore(v2v2Test);
                if (v2v2Test.ret == RETURN.FAIL) { // invalid
                    System.out.println("invalid value v2");
                    return 0;
                }

                // one-round v1v1 and v2v2 succeeded, let's do hypo test
                System.out.println("v1v2 test failed but v1v1&v2v2 succeeded:");
                System.out.println("---------------------------------------" + MY_TYPE +
                    " report---------------------------------------------");
                System.out.println(v1v2Test.completeInfo());
                return 1;
            }
        }

        System.out.println("ERROR: cannot reach here.");
        return 0;
    }
    
    /* enhancement for revision */ 
    /*private static void hypothesisTestLogic(TestResult test_basic) throws Exception {
	int v1v2FailedCount = 0;
	int v1v1v2v2FailedCount = 0;
        int earlyStopThreshold = 3;
	boolean earlyStop = false;
        int i = 0;

        System.out.println(test_basic.toString());

        for (i=0; i<MAX_HYPO_RUN; i++) {
	    if ( (v1v2FailedCount >= earlyStopThreshold && v1v1v2v2FailedCount == 0) ||
                    (i >= earlyStopThreshold && v1v2FailedCount == 0) ||
                    v1v1v2v2FailedCount >= earlyStopThreshold )  {
		System.out.println("early stop after " + earlyStopThreshold + " is satisfied");
		earlyStop = true;
		break;
	    }

            TestResult v1v1Test = new TestResult(test_basic);
            v1v1Test.vv_mode = "v1v1";
            runTestCore(v1v1Test);
            TestResult v2v2Test = new TestResult(test_basic);
            v2v2Test.vv_mode = "v2v2";
            runTestCore(v2v2Test);
            if (v1v1Test.ret == RETURN.FAIL || v2v2Test.ret == RETURN.FAIL) {
                System.out.println("---> v1v1 or v2v2 test failed.");
		if (v1v1Test.ret == RETURN.FAIL) {
		    System.out.println("v1v1 failed in a hypo test");
		    System.out.println(v1v1Test.completeInfo());
                }
		if (v2v2Test.ret == RETURN.FAIL) {
		    System.out.println("v2v2 failed in a hypo test");
		    System.out.println(v2v2Test.completeInfo());
                }
                v1v1v2v2FailedCount ++;
            } else {
                System.out.println("---> v1v1 and v2v2 test test suceeded.");
            }
	    
            TestResult v1v2Test = new TestResult(test_basic);
            v1v2Test.vv_mode = "v1v2";
            runTestCore(v1v2Test);
            if (v1v2Test.ret == RETURN.FAIL || v1v2Test.running_time >= (LONG_TIME_MUL * Math.max(v1v1Test.running_time, v2v2Test.running_time))) {
		int failed_reason = 0;
		if (v1v2Test.ret != RETURN.SUCCEED) {
		    failed_reason += 1;
		}

		if (v1v2Test.running_time >= (LONG_TIME_MUL * Math.max(v1v1Test.running_time, v2v2Test.running_time))) {
                    System.out.println("v1v2 runs longer failure");
                    System.out.println("v1v2 running time: " + v1v2Test.running_time);
                    System.out.println("v1v1 running time: " + v1v1Test.running_time);
                    System.out.println("v2v2 running time: " + v2v2Test.running_time);
		    failed_reason += 2;
		}
                System.out.println("---> v1v2 test failed because of reason " + failed_reason);
		System.out.println(v1v2Test.completeInfo());
                v1v2FailedCount ++;
            } else {
                System.out.println("---> v1v2 test suceeded.");
            }
        }

	System.out.println("v1v2 failed with probability " + v1v2FailedCount + " out of " + i);
        System.out.println("v1v1v2v2 failed with probability " + v1v1v2v2FailedCount + " out of " + i);

        return;
    }

    private static int runTestLogic(int h_list_size, TestResult test_basic) throws Exception {
        // clone to create real test job
	TestResult v1v1Test = new TestResult(test_basic);
        v1v1Test.vv_mode = "v1v1";
        runTestCore(v1v1Test);

	TestResult v2v2Test = new TestResult(test_basic);
	v2v2Test.vv_mode = "v2v2";
	runTestCore(v2v2Test);
	
        TestResult v1v2Test = new TestResult(test_basic);
        v1v2Test.vv_mode = "v1v2";
	//System.out.println(v1v2Test.toString());
        runTestCore(v1v2Test);

	if (v1v2Test.ret == RETURN.SUCCEED && v1v2Test.running_time < (LONG_TIME_MUL * Math.max(v1v1Test.running_time, v2v2Test.running_time))) {
	    System.out.println("v1v2 test succeeded, no issue.");
	    return 0;
	} else {
	    if (h_list_size > 1) { // return 1 for group test
		System.out.println("always return 1 when group test fails");
		return 1;
	    } else {
		if (v1v1Test.ret == RETURN.FAIL) {
		    System.out.println("v1v1 failed in the run test");
		    return 0;
		}
		
		if (v2v2Test.ret == RETURN.FAIL) {
		    System.out.println("v2v2 failed in the run test");
		    return 0;
		}

		int failed_reason = 0;
		if (v1v2Test.ret != RETURN.SUCCEED) {
		    failed_reason += 1;
		}

		if (v1v2Test.running_time >= (LONG_TIME_MUL * Math.max(v1v1Test.running_time, v2v2Test.running_time))) {
                    System.out.println("v1v2 runs longer failure");
                    System.out.println("v1v2 running time: " + v1v2Test.running_time);
                    System.out.println("v1v1 running time: " + v1v1Test.running_time);
                    System.out.println("v2v2 running time: " + v2v2Test.running_time);
		    failed_reason += 2;
		}

	      	// one-round v1v1 and v2v2 succeeded, let's do hypo test
                System.out.println("v1v2 test failed because of reason " + failed_reason + " but v1v1&v2v2 succeeded:");
                System.out.println("---------------------------------------" + MY_TYPE +
                    " report---------------------------------------------");
                System.out.println(v1v2Test.completeInfo());
                return 1;
		
	    }
	}
    }*/
    
}
