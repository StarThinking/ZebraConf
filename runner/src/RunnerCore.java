import java.io.File;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class RunnerCore {
    protected static String systemRootDir = "/root/ZebraConf/runner/";
    protected static BufferedWriter runLogWriter = null;

    /* shared files */
    private static String testResultDirName = systemRootDir + "shared/test_results";
    private static String vvModeFileName = systemRootDir + "shared/reconf_vvmode";
    private static String hListFileName = systemRootDir + "shared/reconf_h_list";

    public enum RETURN {
        SUCCEED,FAIL
    }

    public static class TestResult {
        // test info
        public String proj = "";
        public String u_test = "";
        public String h_list = "";

        public String vv_mode = "none";

        // test result info
        public RETURN ret = RETURN.FAIL; // 1: succeed -1:failed, assign failed as default
        public String failureMessage = "";
        public String stackTrace = "";
	public long running_time = 0;

        public static final int NumOfFieldsFromFile = 4;

        public TestResult() {
            this("", "", "");
        }

        public TestResult(TestResult o) {
            this(o.proj, o.u_test, o.h_list);
        }

        public TestResult(String proj, String u_test, String h_list) {
            this.proj = proj;
            this.u_test = u_test;
            this.h_list = h_list;
        }

        @Override
        public String toString() {
            return "proj: " + proj + "\n" +
                "u_test: " + u_test + "\n" +
                "h_list: " + h_list;
        }

        public String completeInfo() {
            return this.toString() + "\n" +
                "vv_mode: " + vv_mode + "\n" +
                "result: " + ret + "\n" +
                "failureMessage: " + failureMessage + "\n" +
                "stackTrace: " + stackTrace + "\n";
        }

        public static TestResult getTestResultByName(List<TestResult> list, String name) {
            for (TestResult t : list) {
                if (t.u_test.equals(name))
                    return t;
            }
            // error
            System.out.println("Error: name " + name + " cannot be found in the list");
            return null;
        }

        public static List<String> getTestNames(List<TestResult> list) {
            List<String> names = new ArrayList<String>();
            for (TestResult t : list)
                names.add(t.u_test);
            return names;
        }

        public boolean isValid() {
            if (!proj.equals("hdfs") && !proj.equals("yarn") && !proj.equals("mapreduce") &&
                !proj.equals("hadoop-tools") && !proj.equals("hbase")) {
        	    System.out.println("ERROR: wrong proj " + proj);
        	    return false;
            }

            if (u_test == null || u_test.equals("")) {
        	    System.out.println("ERROR: wrong unit test " + u_test);
                return false;
            }

            if (!vv_mode.equals("none") && !vv_mode.equals("v1v1") && !vv_mode.equals("v2v2") &&
                !vv_mode.equals("v1v2")) {
        	    System.out.println("ERROR: wrong vv_mode " + vv_mode);
                return false;
            }
            return true;
        }
    }

    private static void updateTestResult(List<TestResult> testResultList) {
        String SEPERATOR = "@@@";
        File testResultDir = new File(testResultDirName);
        List<String> updatedTests = new ArrayList<String>();
        try {
            for (File f : testResultDir.listFiles()) {
                if (f.isFile()) {
                    //System.out.println("updating test result for " + f.getName());
                    BufferedReader reader = new BufferedReader(new FileReader(f));
                    String buffer = "";
                    StringBuilder sb = new StringBuilder("");  
                    buffer = reader.readLine();
                    while (buffer != null) {
                        sb.append(buffer + System.lineSeparator());
                        buffer = reader.readLine();
                    }
                    reader.close();
                    String[] contents = sb.toString().trim().split(SEPERATOR);
                    if (contents.length != TestResult.NumOfFieldsFromFile) {
                        System.out.println("ERROR: the content for " + f.getName() + " is wrong, length = "
                            + contents.length);
                        System.out.println("Content: ");
                        System.out.println(sb.toString());
                        continue;
                    } else {
                        String testName = contents[0];
                        TestResult testResult = TestResult.getTestResultByName(testResultList, testName);
                        if (testResult == null) {
                            System.out.println("ERROR: cannot find testResult by test name " + testName);
                            continue;
                        } else {
                            if (contents[1].equals("1"))
                                testResult.ret = RETURN.SUCCEED;
                            else 
                                testResult.ret = RETURN.FAIL;
                            testResult.failureMessage = contents[2];
                            testResult.stackTrace = contents[3];
                            updatedTests.add(testName);
                            //System.out.println(testResult.completeInfo());
                        }
                    }
                }
            }
            List<String> allTestNames = TestResult.getTestNames(testResultList);
            for (String t : allTestNames) {
                boolean found = false;
                for (String updated : updatedTests) {
                    if (t.equals(updated)) {
                        found = true;
                    }
                    if (found)
                        break;
                }
                if (!found) {
                    System.out.println("WARN: test " + t + " has not been updated !");
                }
            }
	} catch (Exception e) {
	    System.out.println("WARN: something went wrong with listener, but it is ok");
	}
    }
    
    private static void runMvnCmd(TestResult tr) throws Exception {
        int exitCode = -1;
        boolean isTimeout = false;
	long startTime = 0, endTime = 0, totalTime = 0;
        Process process = null;
        //String systemLogSavingDir = "/root/reconf_test_gen/target";
        String systemLogSavingDir = "none";
        ProcessBuilder builder = new ProcessBuilder();
        builder.command("/root/ZebraConf/app_meta/run_mvn_test.sh", tr.proj, tr.u_test, systemLogSavingDir);
	// set start time
	startTime = System.nanoTime();
        process = builder.start();
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line = "";
        while ((line = reader.readLine()) != null) {
    	    ;
    	    //System.out.println(line);
        }
        reader.close();
        if(!process.waitFor(1200, TimeUnit.SECONDS)) { // timeout - kill the process.
    	    System.out.println("WARN: wait process timeout!");
            isTimeout = true;
	    process.destroy(); // consider using destroyForcibly instead
        }
        
	exitCode = process.exitValue();
        if (isTimeout) {
            exitCode = -1;
        }
       
        List<TestResult> testResultList = new ArrayList<TestResult>();
        testResultList.add(tr);
        updateTestResult(testResultList);

        // override result with cmd exit code
        if ((exitCode == 0 && tr.ret == RETURN.FAIL) || (exitCode != 0 && tr.ret == RETURN.SUCCEED)) {
            System.out.println("WARN: conflict exitCode = " + exitCode + " but tr.result = " + tr.ret);
        }
       
        // update test result
        if (exitCode == 0) {
    	    tr.ret = RETURN.SUCCEED;
        } else {
    	    tr.ret = RETURN.FAIL;
        }
	// set end time
	endTime = System.nanoTime();
	totalTime = endTime - startTime;
	System.out.println(tr.vv_mode + " running time = " + totalTime);
	tr.running_time = totalTime;
    }

    // update directly at TestResult tr
    public static void runTestCore(TestResult tr) throws Exception {
        try {
            // clean before and after each test
            cleanUpSharedFiles();
            setupTestTuple(tr);
            runMvnCmd(tr);
        } catch (Exception e) {
	    if (e instanceof InterruptedException) {
                System.out.println("ERROR: runTestCore throw InterruptedException");
	    }
	    throw e;
        } 
    }
 
    private static void setupTestTuple(TestResult tr) throws Exception {
        BufferedWriter writer = null;
        writer = new BufferedWriter(new FileWriter(new File(hListFileName)));
        writer.write(tr.h_list);
        writer.close();
       
        writer = new BufferedWriter(new FileWriter(new File(vvModeFileName)));
        writer.write(tr.vv_mode);
        writer.close();
    }

    private static void cleanUpSharedFiles() throws Exception {
       File testResultDir = new File(testResultDirName);
       for (File testResult : testResultDir.listFiles()) {
           if (testResult.isFile()) {
               testResult.delete();
           }
       }
       TestResult empty = new TestResult();
       setupTestTuple(empty);
    }
}
