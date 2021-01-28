/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.hadoop.test;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.lang.management.LockInfo;
import java.lang.management.ManagementFactory;
import java.lang.management.MonitorInfo;
import java.lang.management.ThreadInfo;
import java.lang.management.ThreadMXBean;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;

import org.apache.hadoop.util.StringUtils;
import org.junit.runner.notification.Failure;
import org.junit.runner.notification.RunListener;

import org.junit.runner.Description;
import org.junit.runner.Result;
import java.io.File;
import java.io.BufferedWriter;
import java.io.FileWriter;
import org.apache.commons.lang3.exception.ExceptionUtils;

import java.util.List;

/**
 * JUnit run listener which prints full thread dump into System.err
 * in case a test is failed due to timeout.
 */
public class TimedOutTestsListener extends RunListener {

  static final String TEST_TIMED_OUT_PREFIX = "test timed out after";
  
  private static String INDENT = "    ";

  private final PrintWriter output;
  
  public String controllerRootDir = "/root/ZebraConf/runner/";
  public String resultDirName = controllerRootDir + "shared/test_results/";
  public String warnDirName = controllerRootDir + "shared/warn_results/";
  public String SEPERATOR = "@@@";
  public String globalTestName = "";
  public int unitTestCounterInClass = 0;

  public TimedOutTestsListener() {
    this.output = new PrintWriter(System.err);
  }
  
  public TimedOutTestsListener(PrintWriter output) {
    this.output = output;
  }

  private void writeFile(String testName, String failureMessage, String stackTrace, String result) throws Exception {
      System.out.println("msx-listener INFO: writeFile, the original testName is " + testName);
      File theFile = null;
      if (testName.equals("")) {
          Date date = new Date();
          SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss");
          String dateTime = "Warn-" + formatter.format(date);
          theFile = new File(warnDirName + dateTime);
      } else {
          String nameRemovePara = testName.split("\\[")[0];
          System.out.println("msx-listener INFO: nameRemovePara = " + nameRemovePara);
          theFile = new File(resultDirName + nameRemovePara);
      }

      if (!theFile.exists()) {
          System.out.println("msx-listener INFO: write result to file " + theFile);
          BufferedWriter writer = new BufferedWriter(new FileWriter(theFile)); 
          writer.write(testName + SEPERATOR + result + SEPERATOR + failureMessage + SEPERATOR + stackTrace + SEPERATOR);
          writer.flush();
          writer.close();
      } else {
          System.out.println("msx-listener INFO: file existed " + theFile);
      }
  }

  private String getTestName(String className, String methodName) throws Exception {
      if (className == null || methodName == null || className.equals("") || methodName.equals("")) {
          if (!globalTestName.equals("") && !globalTestName.equals("#")) {
              System.out.println("msx-listener WARN: using globalTestName " + globalTestName);
              return globalTestName;
          } else {
              System.out.println("msx-listener ERROR: unable to obtain test name!");
              return "";
          } 
      }
      return className + "#" + methodName;
  }

  private static void printStackTrace(StackTraceElement[] stack) {
    if (stack != null) {
        System.out.println("msx-stack stack.length = " + (stack.length-1));
        for (int i = 1; i < stack.length; i++) {
            StackTraceElement s = stack[i];
            System.out.println("\tmsx-stack at " + s.getClassName() + "." + s.getMethodName() +
            "(" + s.getFileName() + ":" + s.getLineNumber() + ")");
        }
    }
  }

  private void succeed(String testName, Description description) {
      try {
          String failureMessage = "none";
          String stackTrace = "none";
          String result = "1";
          writeFile(testName, failureMessage, stackTrace, result);
          System.out.println("msx-listener succeed");
          //showStartStack();
          //reset();
      } catch (Exception e) {
          e.printStackTrace();
      }
  }

  private void failed(String testName, Failure failure) throws Exception {
      try {
      String failureMessage = failure.getMessage();
      String stackTrace = ExceptionUtils.getStackTrace(failure.getException());
      String result = "-1";
      writeFile(testName, failureMessage, stackTrace, result);
      System.out.println("msx-listener failed");
      System.out.println("msx-listener failureMessage: " + failureMessage);
      System.out.println("msx-listener stackTrace: " + stackTrace);
      //showStartStack();
      //reset();
      } catch (Exception e) {
          e.printStackTrace();
      }
  }

  @Override
  public void testStarted(Description description) throws java.lang.Exception {
      globalTestName = description.getClassName() + "#" + description.getMethodName();
      System.out.println("msx-listener test started " + globalTestName);
      if (unitTestCounterInClass > 0) { // perform reset
          System.out.println("msx-listener perform reset as unitTestCounterInClass " + unitTestCounterInClass + " is larger than zero");
          //reset();
      } else {
          System.out.println("msx-listener unitTestCounterInClass = " + unitTestCounterInClass);
      }
      unitTestCounterInClass++;
  }

  @Override
  public void testFinished(Description description) throws Exception {
      String testName = getTestName(description.getClassName(), description.getMethodName());
      System.out.println("msx-listener testfinished " + testName);
      succeed(testName, description);
  }
  
  @Override
  public void testIgnored(Description description) throws Exception {
      String testName = getTestName(description.getClassName(), description.getMethodName());
      System.out.println("msx-listener test Ignored " + testName);
      succeed(testName, description);
  }
   
  public void myTestFailure(Failure failure) throws Exception{
      Description description = failure.getDescription();
      String testName = getTestName(description.getClassName(), description.getMethodName());
      System.out.println("msx-listener test Failure " + testName);
      failed(testName, failure);
  }

  @Override
  public void testAssumptionFailure(Failure failure) {
      try {
          Description description = failure.getDescription();
          String testName = getTestName(description.getClassName(), description.getMethodName());
          System.out.println("msx-listener testAssumptionFailure " + testName);
          failed(testName, failure);
      } catch(Exception e) {
          e.printStackTrace();
      }
  }
   
  @Override // Called before any tests have been run.
  public void testRunStarted(Description description) throws Exception {
      System.out.println("msx-listener all testRunStarted");
  }

  @Override // Called when all tests have finished
  public void testRunFinished(Result result) throws Exception {
      System.out.println("msx-listener all testRunFinished");
  }

  @Override
  public void testFailure(Failure failure) throws Exception {
    myTestFailure(failure);
    if (failure != null && failure.getMessage() != null 
        && failure.getMessage().startsWith(TEST_TIMED_OUT_PREFIX)) {
      output.println("====> TEST TIMED OUT. PRINTING THREAD DUMP. <====");
      output.println();
      output.print(buildThreadDiagnosticString());
    }
  }
  
  public static String buildThreadDiagnosticString() {
    StringWriter sw = new StringWriter();
    PrintWriter output = new PrintWriter(sw);
    
    DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss,SSS");
    output.println(String.format("Timestamp: %s", dateFormat.format(new Date())));
    output.println();
    output.println(buildThreadDump());
    
    String deadlocksInfo = buildDeadlockInfo();
    if (deadlocksInfo != null) {
      output.println("====> DEADLOCKS DETECTED <====");
      output.println();
      output.println(deadlocksInfo);
    }

    return sw.toString();
  }

  static String buildThreadDump() {
    StringBuilder dump = new StringBuilder();
    Map<Thread, StackTraceElement[]> stackTraces = Thread.getAllStackTraces();
    for (Map.Entry<Thread, StackTraceElement[]> e : stackTraces.entrySet()) {
      Thread thread = e.getKey();
      dump.append(String.format(
          "\"%s\" %s prio=%d tid=%d %s\njava.lang.Thread.State: %s",
          thread.getName(),
          (thread.isDaemon() ? "daemon" : ""),
          thread.getPriority(),
          thread.getId(),
          Thread.State.WAITING.equals(thread.getState()) ? 
              "in Object.wait()" :
              StringUtils.toLowerCase(thread.getState().name()),
          Thread.State.WAITING.equals(thread.getState()) ?
              "WAITING (on object monitor)" : thread.getState()));
      for (StackTraceElement stackTraceElement : e.getValue()) {
        dump.append("\n        at ");
        dump.append(stackTraceElement);
      }
      dump.append("\n");
    }
    return dump.toString();
  }
  
  static String buildDeadlockInfo() {
    ThreadMXBean threadBean = ManagementFactory.getThreadMXBean();
    long[] threadIds = threadBean.findMonitorDeadlockedThreads();
    if (threadIds != null && threadIds.length > 0) {
      StringWriter stringWriter = new StringWriter();
      PrintWriter out = new PrintWriter(stringWriter);
      
      ThreadInfo[] infos = threadBean.getThreadInfo(threadIds, true, true);
      for (ThreadInfo ti : infos) {
        printThreadInfo(ti, out);
        printLockInfo(ti.getLockedSynchronizers(), out);
        out.println();
      }
      
      out.close();
      return stringWriter.toString();
    } else {
      return null;
    }
  }
  
  private static void printThreadInfo(ThreadInfo ti, PrintWriter out) {
    // print thread information
    printThread(ti, out);

    // print stack trace with locks
    StackTraceElement[] stacktrace = ti.getStackTrace();
    MonitorInfo[] monitors = ti.getLockedMonitors();
    for (int i = 0; i < stacktrace.length; i++) {
      StackTraceElement ste = stacktrace[i];
      out.println(INDENT + "at " + ste.toString());
      for (MonitorInfo mi : monitors) {
        if (mi.getLockedStackDepth() == i) {
          out.println(INDENT + "  - locked " + mi);
        }
      }
    }
    out.println();
  }

  private static void printThread(ThreadInfo ti, PrintWriter out) {
    out.print("\"" + ti.getThreadName() + "\"" + " Id="
        + ti.getThreadId() + " in " + ti.getThreadState());
    if (ti.getLockName() != null) {
      out.print(" on lock=" + ti.getLockName());
    }
    if (ti.isSuspended()) {
      out.print(" (suspended)");
    }
    if (ti.isInNative()) {
      out.print(" (running in native)");
    }
    out.println();
    if (ti.getLockOwnerName() != null) {
      out.println(INDENT + " owned by " + ti.getLockOwnerName() + " Id="
          + ti.getLockOwnerId());
    }
  }

  private static void printLockInfo(LockInfo[] locks, PrintWriter out) {
    out.println(INDENT + "Locked synchronizers: count = " + locks.length);
    for (LockInfo li : locks) {
      out.println(INDENT + "  - " + li);
    }
    out.println();
  }
  
}
