/*
 * Copyright (c) 1994, 2016, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.  Oracle designates this
 * particular file as subject to the "Classpath" exception as provided
 * by Oracle in the LICENSE file that accompanied this code.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */

package java.lang;

import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
import java.lang.ref.WeakReference;
import java.security.AccessController;
import java.security.AccessControlContext;
import java.security.PrivilegedAction;
import java.util.Map;
import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.locks.LockSupport;
import sun.nio.ch.Interruptible;
import sun.reflect.CallerSensitive;
import sun.reflect.Reflection;
import sun.security.util.SecurityConstants;

// msx
import java.util.List;
import java.util.ArrayList;
import java.io.*;

/**
 * A <i>thread</i> is a thread of execution in a program. The Java
 * Virtual Machine allows an application to have multiple threads of
 * execution running concurrently.
 * <p>
 * Every thread has a priority. Threads with higher priority are
 * executed in preference to threads with lower priority. Each thread
 * may or may not also be marked as a daemon. When code running in
 * some thread creates a new <code>Thread</code> object, the new
 * thread has its priority initially set equal to the priority of the
 * creating thread, and is a daemon thread if and only if the
 * creating thread is a daemon.
 * <p>
 * When a Java Virtual Machine starts up, there is usually a single
 * non-daemon thread (which typically calls the method named
 * <code>main</code> of some designated class). The Java Virtual
 * Machine continues to execute threads until either of the following
 * occurs:
 * <ul>
 * <li>The <code>exit</code> method of class <code>Runtime</code> has been
 *     called and the security manager has permitted the exit operation
 *     to take place.
 * <li>All threads that are not daemon threads have died, either by
 *     returning from the call to the <code>run</code> method or by
 *     throwing an exception that propagates beyond the <code>run</code>
 *     method.
 * </ul>
 * <p>
 * There are two ways to create a new thread of execution. One is to
 * declare a class to be a subclass of <code>Thread</code>. This
 * subclass should override the <code>run</code> method of class
 * <code>Thread</code>. An instance of the subclass can then be
 * allocated and started. For example, a thread that computes primes
 * larger than a stated value could be written as follows:
 * <hr><blockquote><pre>
 *     class PrimeThread extends Thread {
 *         long minPrime;
 *         PrimeThread(long minPrime) {
 *             this.minPrime = minPrime;
 *         }
 *
 *         public void run() {
 *             // compute primes larger than minPrime
 *             &nbsp;.&nbsp;.&nbsp;.
 *         }
 *     }
 * </pre></blockquote><hr>
 * <p>
 * The following code would then create a thread and start it running:
 * <blockquote><pre>
 *     PrimeThread p = new PrimeThread(143);
 *     p.start();
 * </pre></blockquote>
 * <p>
 * The other way to create a thread is to declare a class that
 * implements the <code>Runnable</code> interface. That class then
 * implements the <code>run</code> method. An instance of the class can
 * then be allocated, passed as an argument when creating
 * <code>Thread</code>, and started. The same example in this other
 * style looks like the following:
 * <hr><blockquote><pre>
 *     class PrimeRun implements Runnable {
 *         long minPrime;
 *         PrimeRun(long minPrime) {
 *             this.minPrime = minPrime;
 *         }
 *
 *         public void run() {
 *             // compute primes larger than minPrime
 *             &nbsp;.&nbsp;.&nbsp;.
 *         }
 *     }
 * </pre></blockquote><hr>
 * <p>
 * The following code would then create a thread and start it running:
 * <blockquote><pre>
 *     PrimeRun p = new PrimeRun(143);
 *     new Thread(p).start();
 * </pre></blockquote>
 * <p>
 * Every thread has a name for identification purposes. More than
 * one thread may have the same name. If a name is not specified when
 * a thread is created, a new name is generated for it.
 * <p>
 * Unless otherwise noted, passing a {@code null} argument to a constructor
 * or method in this class will cause a {@link NullPointerException} to be
 * thrown.
 *
 * @author  unascribed
 * @see     Runnable
 * @see     Runtime#exit(int)
 * @see     #run()
 * @see     #stop()
 * @since   JDK1.0
 */
public
class Thread implements Runnable {
    /* Make sure registerNatives is the first thing <clinit> does. */
    private static native void registerNatives();
    static {
        registerNatives();
	// msx
	//loadServerClasses();
    }

    private volatile String name;
    private int            priority;
    private Thread         threadQ;
    private long           eetop;

    /* Whether or not to single_step this thread. */
    private boolean     single_step;

    /* Whether or not the thread is a daemon thread. */
    private boolean     daemon = false;

    /* JVM state */
    private boolean     stillborn = false;

    /* What will be run. */
    private Runnable target;

    /* The group of this thread */
    private ThreadGroup group;

    /* The context ClassLoader for this thread */
    private ClassLoader contextClassLoader;

    /* The inherited AccessControlContext of this thread */
    private AccessControlContext inheritedAccessControlContext;

    /* For autonumbering anonymous threads. */
    private static int threadInitNumber;
    private static synchronized int nextThreadNum() {
        return threadInitNumber++;
    }

    /* ThreadLocal values pertaining to this thread. This map is maintained
     * by the ThreadLocal class. */
    ThreadLocal.ThreadLocalMap threadLocals = null;

    /*
     * InheritableThreadLocal values pertaining to this thread. This map is
     * maintained by the InheritableThreadLocal class.
     */
    ThreadLocal.ThreadLocalMap inheritableThreadLocals = null;

    /*
     * The requested stack size for this thread, or 0 if the creator did
     * not specify a stack size.  It is up to the VM to do whatever it
     * likes with this number; some VMs will ignore it.
     */
    private long stackSize;

    /*
     * JVM-private state that persists after native thread termination.
     */
    private long nativeParkEventPointer;

    /*
     * Thread ID
     */
    private long tid;

    /* For generating thread ID */
    private static long threadSeqNumber;

    /* Java thread status for tools,
     * initialized to indicate thread 'not yet started'
     */

    private volatile int threadStatus = 0;


    private static synchronized long nextThreadID() {
        return ++threadSeqNumber;
    }

    /**
     * The argument supplied to the current call to
     * java.util.concurrent.locks.LockSupport.park.
     * Set by (private) java.util.concurrent.locks.LockSupport.setBlocker
     * Accessed using java.util.concurrent.locks.LockSupport.getBlocker
     */
    volatile Object parkBlocker;

    /* The object in which this thread is blocked in an interruptible I/O
     * operation, if any.  The blocker's interrupt method should be invoked
     * after setting this thread's interrupt status.
     */
    private volatile Interruptible blocker;
    private final Object blockerLock = new Object();

    /* Set the blocker field; invoked via sun.misc.SharedSecrets from java.nio code
     */
    void blockedOn(Interruptible b) {
        synchronized (blockerLock) {
            blocker = b;
        }
    }

    /**
     * The minimum priority that a thread can have.
     */
    public final static int MIN_PRIORITY = 1;

   /**
     * The default priority that is assigned to a thread.
     */
    public final static int NORM_PRIORITY = 5;

    /**
     * The maximum priority that a thread can have.
     */
    public final static int MAX_PRIORITY = 10;

    /**
     * Returns a reference to the currently executing thread object.
     *
     * @return  the currently executing thread.
     */
    public static native Thread currentThread();

    /**
     * A hint to the scheduler that the current thread is willing to yield
     * its current use of a processor. The scheduler is free to ignore this
     * hint.
     *
     * <p> Yield is a heuristic attempt to improve relative progression
     * between threads that would otherwise over-utilise a CPU. Its use
     * should be combined with detailed profiling and benchmarking to
     * ensure that it actually has the desired effect.
     *
     * <p> It is rarely appropriate to use this method. It may be useful
     * for debugging or testing purposes, where it may help to reproduce
     * bugs due to race conditions. It may also be useful when designing
     * concurrency control constructs such as the ones in the
     * {@link java.util.concurrent.locks} package.
     */
    public static native void yield();

    /**
     * Causes the currently executing thread to sleep (temporarily cease
     * execution) for the specified number of milliseconds, subject to
     * the precision and accuracy of system timers and schedulers. The thread
     * does not lose ownership of any monitors.
     *
     * @param  millis
     *         the length of time to sleep in milliseconds
     *
     * @throws  IllegalArgumentException
     *          if the value of {@code millis} is negative
     *
     * @throws  InterruptedException
     *          if any thread has interrupted the current thread. The
     *          <i>interrupted status</i> of the current thread is
     *          cleared when this exception is thrown.
     */
    public static native void sleep(long millis) throws InterruptedException;

    /**
     * Causes the currently executing thread to sleep (temporarily cease
     * execution) for the specified number of milliseconds plus the specified
     * number of nanoseconds, subject to the precision and accuracy of system
     * timers and schedulers. The thread does not lose ownership of any
     * monitors.
     *
     * @param  millis
     *         the length of time to sleep in milliseconds
     *
     * @param  nanos
     *         {@code 0-999999} additional nanoseconds to sleep
     *
     * @throws  IllegalArgumentException
     *          if the value of {@code millis} is negative, or the value of
     *          {@code nanos} is not in the range {@code 0-999999}
     *
     * @throws  InterruptedException
     *          if any thread has interrupted the current thread. The
     *          <i>interrupted status</i> of the current thread is
     *          cleared when this exception is thrown.
     */
    public static void sleep(long millis, int nanos)
    throws InterruptedException {
        if (millis < 0) {
            throw new IllegalArgumentException("timeout value is negative");
        }

        if (nanos < 0 || nanos > 999999) {
            throw new IllegalArgumentException(
                                "nanosecond timeout value out of range");
        }

        if (nanos >= 500000 || (nanos != 0 && millis == 0)) {
            millis++;
        }

        sleep(millis);
    }

    /**
     * Initializes a Thread with the current AccessControlContext.
     * @see #init(ThreadGroup,Runnable,String,long,AccessControlContext,boolean)
     */
    private void init(ThreadGroup g, Runnable target, String name,
                      long stackSize) {
        init(g, target, name, stackSize, null, true);
    }

    /**
     * Initializes a Thread.
     *
     * @param g the Thread group
     * @param target the object whose run() method gets called
     * @param name the name of the new Thread
     * @param stackSize the desired stack size for the new thread, or
     *        zero to indicate that this parameter is to be ignored.
     * @param acc the AccessControlContext to inherit, or
     *            AccessController.getContext() if null
     * @param inheritThreadLocals if {@code true}, inherit initial values for
     *            inheritable thread-locals from the constructing thread
     */
    private void init(ThreadGroup g, Runnable target, String name,
                      long stackSize, AccessControlContext acc,
                      boolean inheritThreadLocals) {
        if (name == null) {
            throw new NullPointerException("name cannot be null");
        }

        this.name = name;

        Thread parent = currentThread();
        SecurityManager security = System.getSecurityManager();
        if (g == null) {
            /* Determine if it's an applet or not */

            /* If there is a security manager, ask the security manager
               what to do. */
            if (security != null) {
                g = security.getThreadGroup();
            }

            /* If the security doesn't have a strong opinion of the matter
               use the parent thread group. */
            if (g == null) {
                g = parent.getThreadGroup();
            }
        }

        /* checkAccess regardless of whether or not threadgroup is
           explicitly passed in. */
        g.checkAccess();

        /*
         * Do we have the required permissions?
         */
        if (security != null) {
            if (isCCLOverridden(getClass())) {
                security.checkPermission(SUBCLASS_IMPLEMENTATION_PERMISSION);
            }
        }

        g.addUnstarted();

        this.group = g;
        this.daemon = parent.isDaemon();
        this.priority = parent.getPriority();
        if (security == null || isCCLOverridden(parent.getClass()))
            this.contextClassLoader = parent.getContextClassLoader();
        else
            this.contextClassLoader = parent.contextClassLoader;
        this.inheritedAccessControlContext =
                acc != null ? acc : AccessController.getContext();
        this.target = target;
        setPriority(priority);
        if (inheritThreadLocals && parent.inheritableThreadLocals != null)
            this.inheritableThreadLocals =
                ThreadLocal.createInheritedMap(parent.inheritableThreadLocals);
        /* Stash the specified stack size in case the VM cares */
        this.stackSize = stackSize;

        /* Set thread ID */
        tid = nextThreadID();   

	// msx
        if (initStackMap.get(this.tid) == null) {
	    initStackMap.put(this.tid, Thread.currentThread().getStackTrace());
	}
    }

    /**
     * Throws CloneNotSupportedException as a Thread can not be meaningfully
     * cloned. Construct a new Thread instead.
     *
     * @throws  CloneNotSupportedException
     *          always
     */
    @Override
    protected Object clone() throws CloneNotSupportedException {
        throw new CloneNotSupportedException();
    }

    /**
     * Allocates a new {@code Thread} object. This constructor has the same
     * effect as {@linkplain #Thread(ThreadGroup,Runnable,String) Thread}
     * {@code (null, null, gname)}, where {@code gname} is a newly generated
     * name. Automatically generated names are of the form
     * {@code "Thread-"+}<i>n</i>, where <i>n</i> is an integer.
     */
    public Thread() {
        init(null, null, "Thread-" + nextThreadNum(), 0);
    }

    /**
     * Allocates a new {@code Thread} object. This constructor has the same
     * effect as {@linkplain #Thread(ThreadGroup,Runnable,String) Thread}
     * {@code (null, target, gname)}, where {@code gname} is a newly generated
     * name. Automatically generated names are of the form
     * {@code "Thread-"+}<i>n</i>, where <i>n</i> is an integer.
     *
     * @param  target
     *         the object whose {@code run} method is invoked when this thread
     *         is started. If {@code null}, this classes {@code run} method does
     *         nothing.
     */
    public Thread(Runnable target) {
        init(null, target, "Thread-" + nextThreadNum(), 0);
    }

    /**
     * Creates a new Thread that inherits the given AccessControlContext.
     * This is not a public constructor.
     */
    Thread(Runnable target, AccessControlContext acc) {
        init(null, target, "Thread-" + nextThreadNum(), 0, acc, false);
    }

    /**
     * Allocates a new {@code Thread} object. This constructor has the same
     * effect as {@linkplain #Thread(ThreadGroup,Runnable,String) Thread}
     * {@code (group, target, gname)} ,where {@code gname} is a newly generated
     * name. Automatically generated names are of the form
     * {@code "Thread-"+}<i>n</i>, where <i>n</i> is an integer.
     *
     * @param  group
     *         the thread group. If {@code null} and there is a security
     *         manager, the group is determined by {@linkplain
     *         SecurityManager#getThreadGroup SecurityManager.getThreadGroup()}.
     *         If there is not a security manager or {@code
     *         SecurityManager.getThreadGroup()} returns {@code null}, the group
     *         is set to the current thread's thread group.
     *
     * @param  target
     *         the object whose {@code run} method is invoked when this thread
     *         is started. If {@code null}, this thread's run method is invoked.
     *
     * @throws  SecurityException
     *          if the current thread cannot create a thread in the specified
     *          thread group
     */
    public Thread(ThreadGroup group, Runnable target) {
        init(group, target, "Thread-" + nextThreadNum(), 0);
    }

    /**
     * Allocates a new {@code Thread} object. This constructor has the same
     * effect as {@linkplain #Thread(ThreadGroup,Runnable,String) Thread}
     * {@code (null, null, name)}.
     *
     * @param   name
     *          the name of the new thread
     */
    public Thread(String name) {
        init(null, null, name, 0);
    }

    /**
     * Allocates a new {@code Thread} object. This constructor has the same
     * effect as {@linkplain #Thread(ThreadGroup,Runnable,String) Thread}
     * {@code (group, null, name)}.
     *
     * @param  group
     *         the thread group. If {@code null} and there is a security
     *         manager, the group is determined by {@linkplain
     *         SecurityManager#getThreadGroup SecurityManager.getThreadGroup()}.
     *         If there is not a security manager or {@code
     *         SecurityManager.getThreadGroup()} returns {@code null}, the group
     *         is set to the current thread's thread group.
     *
     * @param  name
     *         the name of the new thread
     *
     * @throws  SecurityException
     *          if the current thread cannot create a thread in the specified
     *          thread group
     */
    public Thread(ThreadGroup group, String name) {
        init(group, null, name, 0);
    }

    /**
     * Allocates a new {@code Thread} object. This constructor has the same
     * effect as {@linkplain #Thread(ThreadGroup,Runnable,String) Thread}
     * {@code (null, target, name)}.
     *
     * @param  target
     *         the object whose {@code run} method is invoked when this thread
     *         is started. If {@code null}, this thread's run method is invoked.
     *
     * @param  name
     *         the name of the new thread
     */
    public Thread(Runnable target, String name) {
        init(null, target, name, 0);
    }

    /**
     * Allocates a new {@code Thread} object so that it has {@code target}
     * as its run object, has the specified {@code name} as its name,
     * and belongs to the thread group referred to by {@code group}.
     *
     * <p>If there is a security manager, its
     * {@link SecurityManager#checkAccess(ThreadGroup) checkAccess}
     * method is invoked with the ThreadGroup as its argument.
     *
     * <p>In addition, its {@code checkPermission} method is invoked with
     * the {@code RuntimePermission("enableContextClassLoaderOverride")}
     * permission when invoked directly or indirectly by the constructor
     * of a subclass which overrides the {@code getContextClassLoader}
     * or {@code setContextClassLoader} methods.
     *
     * <p>The priority of the newly created thread is set equal to the
     * priority of the thread creating it, that is, the currently running
     * thread. The method {@linkplain #setPriority setPriority} may be
     * used to change the priority to a new value.
     *
     * <p>The newly created thread is initially marked as being a daemon
     * thread if and only if the thread creating it is currently marked
     * as a daemon thread. The method {@linkplain #setDaemon setDaemon}
     * may be used to change whether or not a thread is a daemon.
     *
     * @param  group
     *         the thread group. If {@code null} and there is a security
     *         manager, the group is determined by {@linkplain
     *         SecurityManager#getThreadGroup SecurityManager.getThreadGroup()}.
     *         If there is not a security manager or {@code
     *         SecurityManager.getThreadGroup()} returns {@code null}, the group
     *         is set to the current thread's thread group.
     *
     * @param  target
     *         the object whose {@code run} method is invoked when this thread
     *         is started. If {@code null}, this thread's run method is invoked.
     *
     * @param  name
     *         the name of the new thread
     *
     * @throws  SecurityException
     *          if the current thread cannot create a thread in the specified
     *          thread group or cannot override the context class loader methods.
     */
    public Thread(ThreadGroup group, Runnable target, String name) {
        init(group, target, name, 0);
    }

    /**
     * Allocates a new {@code Thread} object so that it has {@code target}
     * as its run object, has the specified {@code name} as its name,
     * and belongs to the thread group referred to by {@code group}, and has
     * the specified <i>stack size</i>.
     *
     * <p>This constructor is identical to {@link
     * #Thread(ThreadGroup,Runnable,String)} with the exception of the fact
     * that it allows the thread stack size to be specified.  The stack size
     * is the approximate number of bytes of address space that the virtual
     * machine is to allocate for this thread's stack.  <b>The effect of the
     * {@code stackSize} parameter, if any, is highly platform dependent.</b>
     *
     * <p>On some platforms, specifying a higher value for the
     * {@code stackSize} parameter may allow a thread to achieve greater
     * recursion depth before throwing a {@link StackOverflowError}.
     * Similarly, specifying a lower value may allow a greater number of
     * threads to exist concurrently without throwing an {@link
     * OutOfMemoryError} (or other internal error).  The details of
     * the relationship between the value of the <tt>stackSize</tt> parameter
     * and the maximum recursion depth and concurrency level are
     * platform-dependent.  <b>On some platforms, the value of the
     * {@code stackSize} parameter may have no effect whatsoever.</b>
     *
     * <p>The virtual machine is free to treat the {@code stackSize}
     * parameter as a suggestion.  If the specified value is unreasonably low
     * for the platform, the virtual machine may instead use some
     * platform-specific minimum value; if the specified value is unreasonably
     * high, the virtual machine may instead use some platform-specific
     * maximum.  Likewise, the virtual machine is free to round the specified
     * value up or down as it sees fit (or to ignore it completely).
     *
     * <p>Specifying a value of zero for the {@code stackSize} parameter will
     * cause this constructor to behave exactly like the
     * {@code Thread(ThreadGroup, Runnable, String)} constructor.
     *
     * <p><i>Due to the platform-dependent nature of the behavior of this
     * constructor, extreme care should be exercised in its use.
     * The thread stack size necessary to perform a given computation will
     * likely vary from one JRE implementation to another.  In light of this
     * variation, careful tuning of the stack size parameter may be required,
     * and the tuning may need to be repeated for each JRE implementation on
     * which an application is to run.</i>
     *
     * <p>Implementation note: Java platform implementers are encouraged to
     * document their implementation's behavior with respect to the
     * {@code stackSize} parameter.
     *
     *
     * @param  group
     *         the thread group. If {@code null} and there is a security
     *         manager, the group is determined by {@linkplain
     *         SecurityManager#getThreadGroup SecurityManager.getThreadGroup()}.
     *         If there is not a security manager or {@code
     *         SecurityManager.getThreadGroup()} returns {@code null}, the group
     *         is set to the current thread's thread group.
     *
     * @param  target
     *         the object whose {@code run} method is invoked when this thread
     *         is started. If {@code null}, this thread's run method is invoked.
     *
     * @param  name
     *         the name of the new thread
     *
     * @param  stackSize
     *         the desired stack size for the new thread, or zero to indicate
     *         that this parameter is to be ignored.
     *
     * @throws  SecurityException
     *          if the current thread cannot create a thread in the specified
     *          thread group
     *
     * @since 1.4
     */
    public Thread(ThreadGroup group, Runnable target, String name,
                  long stackSize) {
        init(group, target, name, stackSize);
    }
  
    // msx
    private static Map startStackMap = new HashMap<Long, StackTraceElement[]>();
    private static Map initStackMap = new HashMap<Long, StackTraceElement[]>();
    private static Map<Long, String> tidComponentMap = new HashMap<Long, String>();
    private static Map<String, List<Long>> componentTidListMap = new HashMap<String, List<Long>>();
    private static Map<String, List<String>> componentClassListMap = new HashMap<String, List<String>>();  

    private static void loadServerClasses4ApplicationHistoryServer() {
	List<String> classList = new ArrayList<String>();
	componentClassListMap.put("ApplicationHistoryServer", classList);
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryClientService");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryManager");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryReader");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryWriter");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryManagerOnTimelineStore");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.FileSystemApplicationHistoryStore");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryStore");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AboutPage");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AHSController");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AppAttemptPage");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AppPage");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AHSWebApp");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AboutBlock");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AHSErrorsAndWarningsPage");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.ContainerPage");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AHSLogsPage");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AHSWebServices");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.AHSView");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.JAXBContextResolver");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.webapp.NavBlock");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.NullApplicationHistoryStore");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryServer");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.ApplicationHistoryManagerImpl");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ApplicationHistoryData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ApplicationFinishData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ContainerFinishData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ContainerHistoryData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.impl.pb.ApplicationAttemptFinishDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.impl.pb.ApplicationStartDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.impl.pb.ContainerStartDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.impl.pb.ApplicationFinishDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.impl.pb.ContainerFinishDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.impl.pb.ApplicationAttemptStartDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ApplicationAttemptStartData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ContainerStartData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ApplicationStartData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ApplicationAttemptHistoryData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.records.ApplicationAttemptFinishData");
	classList.add("org.apache.hadoop.yarn.server.applicationhistoryservice.MemoryApplicationHistoryStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.TimelineReader");
	classList.add("org.apache.hadoop.yarn.server.timeline.util.LeveldbUtils");
	classList.add("org.apache.hadoop.yarn.server.timeline.recovery.LeveldbTimelineStateStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.recovery.MemoryTimelineStateStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.recovery.TimelineStateStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.recovery.records.TimelineDelegationTokenIdentifierData");
	classList.add("org.apache.hadoop.yarn.server.timeline.security.TimelineACLsManager");
	classList.add("org.apache.hadoop.yarn.server.timeline.security.TimelineV1DelegationTokenSecretManagerService");
	classList.add("org.apache.hadoop.yarn.server.timeline.security.authorize.TimelinePolicyProvider");
	classList.add("org.apache.hadoop.yarn.server.timeline.TimelineWriter");
	classList.add("org.apache.hadoop.yarn.server.timeline.TimelineStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.GenericObjectMapper");
	classList.add("org.apache.hadoop.yarn.server.timeline.RollingLevelDB");
	classList.add("org.apache.hadoop.yarn.server.timeline.EntityIdentifier");
	classList.add("org.apache.hadoop.yarn.server.timeline.MemoryTimelineStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.TimelineDataManagerMetrics");
	classList.add("org.apache.hadoop.yarn.server.timeline.webapp.TimelineWebServices");
	classList.add("org.apache.hadoop.yarn.server.timeline.webapp.CrossOriginFilterInitializer");
	classList.add("org.apache.hadoop.yarn.server.timeline.NameValuePair");
	classList.add("org.apache.hadoop.yarn.server.timeline.TimelineStoreMapAdapter");
	classList.add("org.apache.hadoop.yarn.server.timeline.RollingLevelDBTimelineStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.package-info");
	classList.add("org.apache.hadoop.yarn.server.timeline.TimelineDataManager");
	classList.add("org.apache.hadoop.yarn.server.timeline.KeyValueBasedTimelineStore");
	classList.add("org.apache.hadoop.yarn.server.timeline.LeveldbTimelineStore");
    }

    private static void loadServerClasses4NodeManager() {
	List<String> classList = new ArrayList<String>();
	componentClassListMap.put("NodeManager", classList);
	classList.add("org.apache.hadoop.yarn.server.nodemanager.collectormanager.NMCollectorService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.collectormanager.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.LocalDirsHandlerService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.util.CgroupsLCEResourcesHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.util.ProcessIdFileReader");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.util.NodeManagerBuilderUtils");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.util.NodeManagerHardwareUtils");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.util.DefaultLCEResourcesHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.util.LCEResourcesHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServicesEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxiliaryServiceWithCustomClassLoader");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServicesEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.SignalContainersLauncherEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainerCleanup");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.RecoveredContainerLaunch");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainersLauncher");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.AbstractContainersLauncher");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.RecoverPausedContainerLaunch");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainerRelaunch");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainersLauncherEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainerLaunch");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.launcher.ContainersLauncherEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.runtime.ContainerExecutionException");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.runtime.ContainerRuntimeConstants");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.runtime.ContainerRuntime");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.runtime.ContainerRuntimeContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerReInitEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerResourceEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerExitEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerDiagnosticsUpdateEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ResourceMappings");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerInitEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerPauseEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerResourceFailedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.SlidingWindowRetryPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.Container");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerKillEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.UpdateContainerTokenEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerResumeEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerResourceLocalizedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerState");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.container.ContainerEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainerStartMonitoringEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainerMetrics");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainerStopMonitoringEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ChangeMonitoringContainerResourceEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.monitor.ContainersMonitorEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.NonAggregatingLogHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.event.LogHandlerTokenUpdatedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.event.LogHandlerAppFinishedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.event.LogHandlerContainerFinishedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.event.LogHandlerAppStartedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.event.LogHandlerEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.event.LogHandlerEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.loghandler.LogHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationState");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationInitEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationContainerInitEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.Application");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationContainerFinishedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationFinishEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.application.ApplicationInitedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.AllocationBasedResourceUtilizationTracker");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.ContainerSchedulerEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.UpdateContainerSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.ResourceUtilizationTracker");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.ContainerScheduler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.ContainerSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.scheduler.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.GpuDevice");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.GpuDeviceSpecificationException");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.GpuDiscoverer");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.AssignedGpuDevice");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.NvidiaBinaryHelper");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.GpuNodeResourceUpdateHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.NvidiaDockerV2CommandPlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.NvidiaDockerV1CommandPlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.GpuResourcePlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.gpu.GpuDockerCommandPluginFactory");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.ResourcePlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.fpga.FpgaDiscoverer");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.fpga.FpgaResourcePlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.fpga.IntelFpgaOpenclPlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.fpga.FpgaNodeResourceUpdateHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.fpga.AbstractFpgaVendorPlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.NodeResourceUpdaterPlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.DockerCommandPlugin");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.resourceplugin.ResourcePluginManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.LocalCacheDirectoryManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.sharedcache.SharedCacheUploadService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.sharedcache.SharedCacheUploader");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.sharedcache.SharedCacheUploadEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.sharedcache.SharedCacheUploadEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.security.LocalizerTokenSelector");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.security.LocalizerSecurityInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.security.LocalizerTokenIdentifier");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.security.LocalizerTokenSecretManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.LocalCacheCleaner");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceLocalizationService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.LocalizerContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ContainerLocalizer");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.LocalResourceRequest");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.LocalResourcesTrackerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceState");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.LocalResourcesTracker");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.LocalizerResourceRequestEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.LocalizationEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ResourceEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ResourceRequestEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ResourceRecoveredEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ContainerLocalizationCleanupEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ResourceReleaseEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ContainerLocalizationEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ResourceLocalizedEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ResourceEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.LocalizationEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ResourceFailedLocalizationEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ContainerLocalizationRequestEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.LocalizerEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.ApplicationLocalizationEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.event.LocalizerEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.LocalizedResource");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.localizer.ResourceSet");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.JavaSandboxLinuxContainerRuntime");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerLoadCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerClient");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerPullCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerRunCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerRmCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerCommandExecutor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerStopCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerKillCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerInspectCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerVolumeCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.docker.DockerStartCommand");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.DelegatingLinuxContainerRuntime");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.LinuxContainerRuntimeConstants");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.DefaultLinuxContainerRuntime");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.LinuxContainerRuntime");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.runtime.DockerLinuxContainerRuntime");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.privileged.PrivilegedOperation");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.privileged.PrivilegedOperationExecutor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.privileged.PrivilegedOperationException");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.ResourceHandlerModule");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.DefaultOOMHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.ResourcesExceptionUtil");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.gpu.GpuResourceAllocator");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.gpu.GpuResourceHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.NetworkTagMappingManagerFactory");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CpuResourceHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.numa.NumaNodeResource");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.numa.NumaResourceAllocator");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.numa.NumaResourceHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.numa.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.numa.NumaResourceAllocation");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.OutboundBandwidthResourceHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.fpga.FpgaResourceAllocator");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.fpga.FpgaResourceHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupsMountConfig");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupsMemoryResourceHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupsCpuResourceHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.NetworkTagMappingManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.TrafficControlBandwidthHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.MemoryResourceHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.ResourceHandlerException");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.TrafficController");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.ResourceHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CombinedResourceCalculator");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupsHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupsResourceCalculator");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupsBlkioResourceHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupsHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.CGroupElasticMemoryController");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.NetworkPacketTaggingHandlerImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.ResourceHandlerChain");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.DiskResourceHandler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.linux.resources.NetworkTagMappingJsonManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.AllContainerLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.FailedContainerLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.AMOnlyLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.AppLogAggregatorImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.SampleContainerLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.NoneContainerLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.FailedOrKilledContainerLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.AMOrFailedContainerLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.LogAggregationService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.AppLogAggregator");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.AbstractContainerLogAggregationPolicy");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.deletion.recovery.DeletionTaskRecoveryInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.deletion.recovery.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.deletion.task.DeletionTask");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.deletion.task.DockerContainerDeletionTask");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.deletion.task.DeletionTaskType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.deletion.task.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.containermanager.deletion.task.FileDeletionTask");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeManagerEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeManagerEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.recovery.NMNullStateStoreService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.recovery.NMStateStoreService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.recovery.RecoveryIterator");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.recovery.NMLeveldbStateStoreService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeManagerMXBean");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.security.NMTokenSecretManagerInNM");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.security.NMContainerTokenSecretManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.security.authorize.NMPolicyProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.DefaultContainerExecutor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.CMgrSignalContainersEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeStatusUpdater");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.CMgrUpdateContainersEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.timelineservice.NMTimelineEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.timelineservice.NMTimelineEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.timelineservice.NMTimelinePublisher");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.timelineservice.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.metrics.NodeManagerMetrics");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.ContainerExecutor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.CMgrCompletedContainersEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.ContainerManagerEventType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NMAuditLogger");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.WindowsSecureContainerExecutor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.scheduler.DistributedScheduler");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.DeletionAsUserContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.ContainerSignalContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.ContainerPrepareContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.ContainerStartContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.ContainerReapContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.ContainerLivenessContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.LocalizerStartContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.executor.ContainerReacquisitionContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.ScriptBasedNodeAttributesProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.NodeDescriptorsProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.NodeDescriptorsScriptRunner");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.NodeLabelsProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.ConfigurationNodeAttributesProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.ScriptBasedNodeLabelsProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.ConfigurationNodeLabelsProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.NodeAttributesProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.nodelabels.AbstractNodeDescriptorsProvider");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.NMWebServices");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.WebServer");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.ContainerLogsUtils");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.NMErrorsAndWarningsPage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.gpu.GpuDeviceInformation");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.gpu.GpuDeviceInformationParser");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.gpu.NMGpuResourceInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.gpu.PerGpuTemperature");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.gpu.PerGpuMemoryUsage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.gpu.PerGpuDeviceInformation");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.gpu.PerGpuUtilizations");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.NodeInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.AppsInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.ContainersInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.ContainerInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.NMContainerLogsInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.AppInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.dao.NMResourceInfo");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.ContainerLogsPage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.AllApplicationsPage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.NMView");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.AggregatedLogsBlock");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.ContainerPage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.AllContainersPage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.AggregatedLogsPage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.ApplicationPage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.NMController");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.NMWebAppFilter");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.NodePage");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.JAXBContextResolver");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.webapp.NavBlock");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.ContainerStateTransitionListener");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.LinuxContainerExecutor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.ContainerManagerEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.CMgrCompletedAppsEvent");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.DirectoryCollection");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeStatusUpdaterImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeHealthCheckerService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeResourceMonitorImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.AbstractRequestInterceptor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.AMRMProxyService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.DefaultRequestInterceptor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.AMRMProxyTokenSecretManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.AMRMProxyApplicationContextImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.AMRMProxyApplicationContext");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.RequestInterceptor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.amrmproxy.FederationInterceptor");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.Context");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.LocalizerHeartbeatResponse");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.LocalizerAction");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.impl.pb.LocalizerStatusPBImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.impl.pb.LocalResourceStatusPBImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.impl.pb.LocalizerHeartbeatResponsePBImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.LocalizerStatus");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.ResourceStatusType");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.protocolrecords.LocalResourceStatus");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.ResourceLocalizationSpec");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.LocalizationProtocol");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.impl.pb.service.LocalizationProtocolPBServiceImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.impl.pb.NMProtoUtils");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.impl.pb.ResourceLocalizationSpecPBImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.impl.pb.client.LocalizationProtocolPBClientImpl");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.impl.pb.package-info");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.api.LocalizationProtocolPB");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.logaggregation.tracker.NMLogAggregationStatusTracker");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.ResourceView");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeManager");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.DeletionService");
	classList.add("org.apache.hadoop.yarn.server.nodemanager.NodeResourceMonitor");
    }

    private static void loadServerClasses4ResourceManager() {
	List<String> classList = new ArrayList<String>();
	componentClassListMap.put("ResourceManager", classList);
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ResourceTrackerService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ResourceManagerMXBean");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMAuditLogger");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.resource.ResourceProfilesManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.resource.DynamicResourceConfiguration");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.resource.ResourceProfilesManagerImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMAppManagerEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMServerUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMCriticalThreadUncaughtExceptionHandler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreRemoveAppAttemptEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateUpdateAppAttemptEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.StoreLimitException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.StoreFencedException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreRMDTEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.MemoryRMStateStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.FileSystemRMStateStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.NullRMStateStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateUpdateAppEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreRemoveAppEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateVersionIncompatibleException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.Recoverable");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreStoreReservationEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreAppEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreAppAttemptEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreAMRMTokenEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.ZKRMStateStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreRMDTMasterKeyEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.ApplicationStateData");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.ApplicationAttemptStateData");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.RMDelegationTokenIdentifierData");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.Epoch");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.AMRMTokenSecretManagerState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.impl.pb.ApplicationAttemptStateDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.impl.pb.ApplicationStateDataPBImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.impl.pb.AMRMTokenSecretManagerStatePBImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.records.impl.pb.EpochPBImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.LeveldbRMStateStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.recovery.RMStateStoreFactory");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppLogAggregation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppKillByClientEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMApp");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.AMLivelinessMonitor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttempt");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.event.RMAppAttemptRegistrationEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.event.RMAppAttemptStatusupdateEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.event.RMAppAttemptUnregistrationEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.event.RMAppAttemptContainerFinishedEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppStartAttemptEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.AggregateAppResourceUsage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.attempt.RMAppAttemptMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.monitor.RMAppLifetimeMonitor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.monitor.RMAppToMonitor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.monitor.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppNodeUpdateEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppRunningOnNodeEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppFailedAttemptEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppRecoverEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmapp.RMAppImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.RMDelegationTokenSecretManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.ClientToAMTokenSecretManagerInRM");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.DelegationTokenRenewer");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.AppPriorityACLsManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.AMRMTokenSecretManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.QueueACLsManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.authorize.RMPolicyProvider");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.RMContainerTokenSecretManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.ReservationsACLsManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.security.NMTokenSecretManagerInRM");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMFatalEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMNMInfoBeans");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingContainerFinishEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingApplicationFinishEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingHistoryEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingContainerStartEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.RMApplicationHistoryWriter");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingApplicationHistoryEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingApplicationStartEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingApplicationAttemptStartEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ahs.WritingApplicationAttemptFinishEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.AdminService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.NMLivelinessMonitor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.DefaultAMSProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.invariants.MetricsInvariantChecker");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.invariants.ReservationInvariantsChecker");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.invariants.InvariantsChecker");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.invariants.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.invariants.InvariantViolationException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.SchedulingMonitorManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.FifoCandidatesSelector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.IntraQueueCandidatesSelector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.TempAppPerPartition");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.PreemptableResourceCalculator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.ReservedContainerCandidatesSelector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.TempQueuePerPartition");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.TempSchedulerNode");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.AbstractPreemptionEntity");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.FifoIntraQueuePreemptionPlugin");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.CapacitySchedulerPreemptionContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.PreemptionCandidatesSelector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.CapacitySchedulerPreemptionUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.IntraQueuePreemptionComputePlugin");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.TempUserPerPartition");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.QueuePriorityContainerCandidateSelector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.AbstractPreemptableResourceCalculator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.ProportionalCapacityPreemptionPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.SchedulingMonitor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.monitor.SchedulingEditPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.timelineservice.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.timelineservice.RMTimelineCollectorManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.federation.FederationStateStoreService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.federation.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.federation.FederationStateStoreHeartbeat");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.metrics.TimelineServiceV2Publisher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.metrics.SystemMetricsPublisher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.metrics.AbstractSystemMetricsPublisher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.metrics.CombinedSystemMetricsPublisher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.metrics.TimelineServiceV1Publisher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.metrics.NoOpSystemMetricPublisher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.metrics.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.PlanView");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.FairReservationSystem");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.CapacityOverTimePolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.CapacityReservationSystem");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.PlanContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.PeriodicRLESparseResourceAllocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.exceptions.PlanningQuotaException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.exceptions.ResourceOverCommitException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.exceptions.PlanningException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.exceptions.ContractValidationException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.AlignedPlannerWithGreedy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.PlanningAlgorithm");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.StageAllocatorGreedyRLE");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.StageExecutionInterval");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.Planner");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.IterativePlanner");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.SimpleCapacityReplanner");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.StageAllocatorGreedy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.StageExecutionIntervalUnconstrained");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.StageAllocator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.ReservationAgent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.StageExecutionIntervalByDemand");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.TryManyReservationAgents");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.StageAllocatorLowCostAligned");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.planning.GreedyReservationAgent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.PlanFollower");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.ReservationSystemUtil");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.CapacitySchedulerPlanFollower");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.SharingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.ReservationSystem");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.NoOverCommitPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.ReservationSchedulerConfiguration");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.RLESparseResourceAllocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.AbstractSchedulerPlanFollower");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.InMemoryReservationAllocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.FairSchedulerPlanFollower");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.InMemoryPlan");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.ReservationInputValidator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.AbstractReservationSystem");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.ReservationConstants");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.ReservationInterval");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.Plan");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.PlanEdit");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.reservation.ReservationAllocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ClusterMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ApplicationMasterService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ClientRMService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMContextImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.FifoOrderingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.RecoveryComparator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.FairOrderingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.PriorityComparator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.OrderingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.AbstractComparatorOrderingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.FifoComparator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.FifoOrderingPolicyForPendingApps");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.CompoundComparator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.policy.SchedulableEntity");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ContainerUpdates");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.VisitedResourceRequestTracker");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSPreemptionThread");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSParentQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.MaxRunningAppsEnforcer");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSSchedulerNode");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.SchedulingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSLeafQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSOpDurations");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSStarvedApps");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.ConfigurableResource");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.allocation.QueueProperties");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.allocation.AllocationFileQueueParser");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.allocation.AllocationFileParser");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.AllocationConfigurationException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSAppAttempt");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.AllocationFileLoaderService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSQueueType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.AllocationConfiguration");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FifoAppComparator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.QueuePlacementRule");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.ReservationQueueConfiguration");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FSQueueMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairSchedulerConfiguration");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.Schedulable");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairSchedulerUtilities");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.QueuePlacementPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.policies.DominantResourceFairnessPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.policies.FairSharePolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.policies.FifoPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.policies.ComputeFairShares");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.InvalidQueueNameException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.QueueManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerAppUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.TimeBucketMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ApplicationPlacementAllocatorFactory");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.QueueResourceQuotas");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerNodeReport");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.NodeResponse");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.MutableConfigurationProvider");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.AbstractResourceUsage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.PlacementConstraintManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.AllocationTagsManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.TargetApplications");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.MemoryPlacementConstraintManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.algorithm.LocalAllocationTagsManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.algorithm.CircularIterator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.algorithm.iterators.SerialIterator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.algorithm.iterators.PopularTagsIterator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.algorithm.iterators.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.algorithm.DefaultPlacementAlgorithm");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.algorithm.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.PlacementConstraintsUtil");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.AllocationTags");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.AbstractPlacementProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.PlacementConstraintProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.SchedulerPlacementProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.NodeCandidateSelector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.BatchedRequests");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.DisabledPlacementProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.processor.PlacementDispatcher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.InvalidAllocationTagsQueryException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.Evaluable");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.PlacementConstraintManagerService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.ConstraintPlacementAlgorithm");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.ConstraintPlacementAlgorithmInput");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.PlacedSchedulingRequest");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.SchedulingRequestWithPlacementAttempt");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.ConstraintPlacementAlgorithmOutput");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.SchedulingResponse");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.api.ConstraintPlacementAlgorithmOutputCollector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.constraint.TargetApplicationsNamespace");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.AppSchedulingInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.QueueStateManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ContainerUpdateContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.AbstractYarnScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.QueueEntitlement");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.SchedulerContainer");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.ContainerRequest");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.ApplicationSchedulingConfig");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.ResourceAllocationCommitter");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.ContainerAllocationProposal");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.PendingAsk");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.AssignmentInformation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.fica.FiCaSchedulerNode");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.fica.FiCaSchedulerApp");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.common.ResourceCommitRequest");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.AllocationState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.ActivityState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.ActivityNode");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.ActivitiesManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.ActivitiesLogger");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.NodeAllocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.AllocationActivity");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.AppAllocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.activities.ActivityDiagnosticConstant");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerQueueManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fifo.FifoAppAttempt");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.fifo.FifoScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.Queue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ActiveUsersManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.NodeType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.SchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.AppAddedSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.NodeResourceUpdateSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.NodeAttributesUpdateSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.AppRemovedSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.ContainerPreemptEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.ReleaseContainerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.ContainerExpiredSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.AppAttemptAddedSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.NodeUpdateSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.NodeAddedSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.QueueManagementChangeEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.NodeLabelsUpdateSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.NodeRemovedSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.AppAttemptRemovedSchedulerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.event.SchedulerEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerDynamicEditException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.QueueInvalidException");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.QueueMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ResourceUsage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedContainerChangeRequest");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.MutableConfScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerNode");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.distributed.NodeQueueLoadMonitor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.distributed.QueueLimitCalculator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CSQueueUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.policy.QueueOrderingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.policy.PriorityUtilizationQueueOrderingPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AutoCreatedLeafQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.queuemanagement.GuaranteedOrZeroCapacityOverTimePolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AutoCreatedQueueManagementPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CSAssignment");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.UsersManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.PlanQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.SchedulingMode");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.LeafQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacitySchedulerMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacitySchedulerQueueManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CSQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityHeadroomProvider");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.ParentQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.QueueManagementChange");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AbstractAutoCreatedLeafQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacitySchedulerConfiguration");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AutoCreatedLeafQueueConfig");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.QueueCapacities");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.QueueManagementDynamicEditPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.ReservationQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacitySchedulerContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AppPriorityACLConfigurationParser");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.preemption.PreemptableQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.preemption.KillableContainer");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.preemption.PreemptionManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.AllocationState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.ContainerAllocator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.RegularContainerAllocator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.AbstractContainerAllocator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.allocator.ContainerAllocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.ManagedParentQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.UserInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AbstractManagedParentQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.YarnConfigurationStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.CSConfigurationProvider");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.FSSchedulerConfigurationStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.FileBasedCSConfigurationProvider");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.MutableCSConfigurationProvider");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.YarnConfigurationStoreFactory");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.ZKConfigurationStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.QueueAdminConfigurationMutationACLPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.InMemoryConfigurationStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.conf.LeveldbConfigurationStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AbstractCSQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CSQueueMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CSAMContainerLaunchDiagnosticsConstants");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.AppPriorityACLGroup");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.NodeFilter");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ResourceScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.Allocation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ConfigurationMutationACLPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerApplicationAttempt");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerAppReport");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.DefaultConfigurationMutationACLPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.AbstractUsersManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.ResourceUsageMultiNodeLookupPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.SimpleCandidateNodeSet");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.MultiNodeSorter");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.CandidateNodeSetUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.MultiNodeLookupPolicy");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.MultiNodeSortingManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.CandidateNodeSet");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.AppPlacementAllocator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.LocalityAppPlacementAllocator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.SingleConstraintAppPlacementAllocator");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.MultiNodePolicySpec");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.placement.PendingAskUpdateResult");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ClusterNodeTracker");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.PreemptableResourceScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.NodeReport");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ConfigurationMutationACLPolicyFactory");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.ResourceLimits");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.YarnScheduler");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerApplication");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.scheduler.SchedulerHealth");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMAppManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ClusterMonitor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMFatalEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.RMNodeLabelsManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.NodeAttributesStoreEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.FileSystemNodeAttributeStore");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.RMDelegatedNodeLabelsUpdater");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.NodeLabelsUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.RMNodeLabelsMappingProvider");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.NodeAttributesStoreEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.nodelabels.NodeAttributesManagerImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMNMInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.AMSProcessingChain");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNode");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeStartedEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeStatusEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeCleanAppEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeUpdateContainerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeCleanContainerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeDecommissioningEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeReconnectEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeFinishedContainersPulledByAMEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeResourceUpdateEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.UpdatedContainerInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmnode.RMNodeSignalContainerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.ApplicationsRequestBuilder");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.AppsBlockWithMetrics");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMAppAttemptBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.NodesPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.AboutPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.NodeLabelsPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.MetricsOverviewTable");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.DeSelectFields");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.AppLogAggregationStatusPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.AppAttemptPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.AppPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMWebServiceProtocol");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ApplicationStatisticsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppQueue");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.CapacitySchedulerInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.CapacitySchedulerQueueInfoList");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ResourcesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.PartitionResourcesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationRequestsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeToLabelsEntryList");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppAllocationInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.FifoSchedulerInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ApplicationSubmissionContextInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.LogAggregationContextInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.RMQueueAclInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ActivitiesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.FairSchedulerQueueInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.SchedulerTypeInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppTimeoutInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.UsersInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ConfInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.CredentialsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ResourceRequestInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.CapacitySchedulerQueueInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.UserMetricsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ClusterUserInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.QueueCapacitiesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.CapacitySchedulerHealthInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeToLabelsEntry");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ResourceInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.SchedulerInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.LabelsToNodesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeLabelsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.DelegationToken");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeAllocationInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeToLabelsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.FairSchedulerLeafQueueInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.FairSchedulerQueueInfoList");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.PartitionQueueCapacitiesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeAttributeInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppActivitiesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationDeleteRequestInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.FairSchedulerInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeLabelInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ClusterMetricsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationDefinitionInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationSubmissionRequestInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AllocationTagInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppAttemptInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppPriority");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ResourceUtilizationInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationRequestInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NewReservation");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppAttemptsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationUpdateResponseInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AllocationTagsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationDeleteResponseInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppTimeoutsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.CapacitySchedulerLeafQueueInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ContainerLaunchContextInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.StatisticsItemInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ActivityNodeInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ExecutionTypeRequestInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationListInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ResourceAllocationInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.AppInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NewApplication");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.LocalResourceInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ClusterInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ReservationUpdateRequestInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.NodeAttributesInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.dao.ResourceInformationsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.AboutBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RedirectionErrorPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.DefaultSchedulerPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMErrorsAndWarningsPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMAppsBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMWebApp");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.SchedulerPageUtil");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.FairSchedulerPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMContainerBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.ContainerPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMWebAppUtil");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMWebAppFilter");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RmController");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMAppLogAggregationStatusBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.ErrorBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.FairSchedulerAppsBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.CapacitySchedulerPage");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RmView");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMWebServices");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.JAXBContextResolver");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMAppBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.NavBlock");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.NodeIDsInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.webapp.RMWSConsts");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMActiveServiceContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ResourceManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.preprocessor.SubmissionContextPreProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.preprocessor.NodeLabelProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.preprocessor.QueueProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.preprocessor.TagAddProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.preprocessor.package-info");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.preprocessor.ContextProcessor");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncherEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.amlauncher.ApplicationMasterLauncher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.amlauncher.AMLauncherEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.DecommissioningNodesWatcher");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.NodesListManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMSecretManagerService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMAppManagerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.RMServiceContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.EmbeddedElector");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.ActiveStandbyElectorBasedElectorService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.OpportunisticContainerAllocatorAMService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.blacklist.DisabledBlacklistManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.blacklist.BlacklistManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.blacklist.SimpleBlacklistManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.IsResourceManagerActiveServlet");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.CuratorBasedElectorService");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.NodesListManagerEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.NodesListManagerEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.ApplicationPlacementContext");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.PlacementRule");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.AppNameMappingPlacementRule");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.QueuePath");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.PlacementManager");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.UserGroupMappingPlacementRule");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.QueuePlacementRuleUtils");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.QueueMappingEntity");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.placement.PlacementFactory");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerUpdatesAcquiredEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerImpl");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerEventType");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerReservedEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerNMDoneChangeResourceEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainer");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerFinishedEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerRecoverEvent");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.ContainerAllocationExpirer");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerState");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.AllocationExpirationInfo");
	classList.add("org.apache.hadoop.yarn.server.resourcemanager.rmcontainer.RMContainerEvent");
    }

    private static void loadServerClasses4NameNode() {
	List<String> classList = new ArrayList<String>();
	componentClassListMap.put("NameNode", classList);
	classList.add("org.apache.hadoop.hdfs.server.namenode.FSNamesystemLock");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeAttributes");
        classList.add("org.apache.hadoop.hdfs.server.namenode.Checkpointer");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditLogFileInputStream");
        classList.add("org.apache.hadoop.hdfs.server.namenode.CachedBlock");
        classList.add("org.apache.hadoop.hdfs.server.namenode.BackupImage");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeResourcePolicy");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageFormatProtobuf");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirConcatOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditLogBackupInputStream");
        classList.add("org.apache.hadoop.hdfs.server.namenode.BackupNode");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeReference");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeLayoutVersion");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeResourceChecker");
        classList.add("org.apache.hadoop.hdfs.server.namenode.AclEntryStatusFormat");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditLogOutputStream");
        classList.add("org.apache.hadoop.hdfs.server.namenode.CheckableNameNodeResource");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSPermissionChecker");
        classList.add("org.apache.hadoop.hdfs.server.namenode.BackupJournalManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSEditLogLoader");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeAttributeProvider");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer");
        classList.add("org.apache.hadoop.hdfs.server.namenode.LeaseManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeHttpServer");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageFormatPBINode");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EncryptionZoneManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.SaveNamespaceCancelledException");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNode");
        classList.add("org.apache.hadoop.hdfs.server.namenode.XAttrFormat");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSEditLogOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageTransactionalStorageInspector");
        classList.add("org.apache.hadoop.hdfs.server.namenode.TransferFsImage");
        classList.add("org.apache.hadoop.hdfs.server.namenode.JournalManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.Snapshot");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.AbstractINodeDiff");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.SnapshotFSImageFormat");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.DirectorySnapshottableFeature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.DiffList");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.SnapshotDiffListingInfo");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.AbstractINodeDiffList");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.SnapshotDiffInfo");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.FSImageFormatPBSnapshot");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.DiffListBySkipList");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.FileDiffList");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.DiffListByArrayList");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.FileWithSnapshotFeature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.DirectoryWithSnapshotFeature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.SnapshotStatsMXBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.SnapshotManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.FileDiff");
        classList.add("org.apache.hadoop.hdfs.server.namenode.snapshot.DirectoryDiffListFactory");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirAclOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodesInPath");
        classList.add("org.apache.hadoop.hdfs.server.namenode.UnsupportedActionException");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.EditLogTailer");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.RemoteNameNodeInfo");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.StandbyCheckpointer");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.ActiveState");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.NameNodeHAProxyFactory");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.StandbyState");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.HAState");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.BootstrapStandby");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ha.HAContext");
        classList.add("org.apache.hadoop.hdfs.server.namenode.DefaultINodeAttributesProvider");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeUtils");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSEditLogOpCodes");
        classList.add("org.apache.hadoop.hdfs.server.namenode.Content");
        classList.add("org.apache.hadoop.hdfs.server.namenode.SerialNumberManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.QuotaByStorageTypeEntry");
        classList.add("org.apache.hadoop.hdfs.server.namenode.SafeMode");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImage");
        classList.add("org.apache.hadoop.hdfs.server.namenode.CheckpointFaultInjector");
        classList.add("org.apache.hadoop.hdfs.server.namenode.JournalSet");
        classList.add("org.apache.hadoop.hdfs.server.namenode.metrics.NameNodeMetrics");
        classList.add("org.apache.hadoop.hdfs.server.namenode.metrics.ReplicatedBlocksMBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.metrics.FSNamesystemMBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.metrics.ECBlockGroupsMBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageStorageInspector");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirDeleteOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImagePreTransactionalStorageInspector");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ReencryptionHandler");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageUtil");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirMkdirOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirSymlinkOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.VersionInfoMXBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.AclTransformation");
        classList.add("org.apache.hadoop.hdfs.server.namenode.LogsPurgeable");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeDirectory");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditLogInputStream");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditsDoubleBuffer");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirSatisfyStoragePolicyOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.SerialNumberMap");
        classList.add("org.apache.hadoop.hdfs.server.namenode.StartupProgressServlet");
        classList.add("org.apache.hadoop.hdfs.server.namenode.RedundantEditLogInputStream");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirSnapshotOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeFile");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirTruncateOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.IllegalReservedPathException");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeFileAttributes");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageFormat");
        classList.add("org.apache.hadoop.hdfs.server.namenode.web.resources.NamenodeWebHdfsMethods");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ContentCounts");
        classList.add("org.apache.hadoop.hdfs.server.namenode.IsNameNodeActiveServlet");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameCache");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeWithAdditionalFields");
        classList.add("org.apache.hadoop.hdfs.server.namenode.DfsServlet");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirAppendOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NamenodeFsck");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ImageServlet");
        classList.add("org.apache.hadoop.hdfs.server.namenode.CacheManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeStatusMXBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ContentSummaryComputationContext");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.StartupProgressView");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.PhaseTracking");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.Status");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.AbstractTracking");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.StartupProgressMetrics");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.StepType");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.Step");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.package-info");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.StartupProgress");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.Phase");
        classList.add("org.apache.hadoop.hdfs.server.namenode.startupprogress.StepTracking");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FileJournalManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.BackupState");
        classList.add("org.apache.hadoop.hdfs.server.namenode.GlobalStateIdContext");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirErasureCodingOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EncryptionFaultInjector");
        classList.add("org.apache.hadoop.hdfs.server.namenode.Quota");
        classList.add("org.apache.hadoop.hdfs.server.namenode.SaveNamespaceContext");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSTreeTraverser");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeDirectoryAttributes");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeMap");
        classList.add("org.apache.hadoop.hdfs.server.namenode.SecondaryNameNode");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirAttrOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.Namesystem");
        classList.add("org.apache.hadoop.hdfs.server.namenode.QuotaCounts");
        classList.add("org.apache.hadoop.hdfs.server.namenode.StreamLimiter");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSEditLogAsync");
        classList.add("org.apache.hadoop.hdfs.server.namenode.MetaRecoveryContext");
        classList.add("org.apache.hadoop.hdfs.server.namenode.top.TopAuditLogger");
        classList.add("org.apache.hadoop.hdfs.server.namenode.top.metrics.TopMetrics");
        classList.add("org.apache.hadoop.hdfs.server.namenode.top.window.RollingWindowManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.top.window.RollingWindow");
        classList.add("org.apache.hadoop.hdfs.server.namenode.top.TopConf");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NNStorage");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeId");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INode");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NNUpgradeUtil");
        classList.add("org.apache.hadoop.hdfs.server.namenode.LeaseExpiredException");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.BlockStorageMovementAttemptedItems");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.StoragePolicySatisfier");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.StoragePolicySatisfyManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.ItemInfo");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.BlockMoveTaskHandler");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.SPSService");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.FileCollector");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.DatanodeCacheManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.package-info");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.BlockStorageMovementNeeded");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.Context");
        classList.add("org.apache.hadoop.hdfs.server.namenode.sps.BlockMovementListener");
        classList.add("org.apache.hadoop.hdfs.server.namenode.INodeSymlink");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeMXBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NameNodeFormatException");
        classList.add("org.apache.hadoop.hdfs.server.namenode.AclStorage");
        classList.add("org.apache.hadoop.hdfs.server.namenode.XAttrStorage");
        classList.add("org.apache.hadoop.hdfs.server.namenode.XAttrFeature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FsckServlet");
        classList.add("org.apache.hadoop.hdfs.server.namenode.XAttrPermissionFilter");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageCompression");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirectory");
        classList.add("org.apache.hadoop.hdfs.server.namenode.DirectoryWithQuotaFeature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.SecondaryNameNodeInfoMXBean");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSNamesystem");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirStatAndListingOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditLogBackupOutputStream");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirEncryptionZoneOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSEditLog");
        classList.add("org.apache.hadoop.hdfs.server.namenode.CheckpointConf");
        classList.add("org.apache.hadoop.hdfs.server.namenode.HdfsAuditLogger");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirRenameOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirWriteFileOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditLogInputException");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FileUnderConstructionFeature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.StoragePolicySummary");
        classList.add("org.apache.hadoop.hdfs.server.namenode.AuditLogger");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ReencryptionUpdater");
        classList.add("org.apache.hadoop.hdfs.server.namenode.CachePool");
        classList.add("org.apache.hadoop.hdfs.server.namenode.ErasureCodingPolicyManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSImageSerialization");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSDirXAttrOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.AclFeature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.NNStorageRetentionManager");
        classList.add("org.apache.hadoop.hdfs.server.namenode.CheckpointSignature");
        classList.add("org.apache.hadoop.hdfs.server.namenode.EditLogFileOutputStream");
        classList.add("org.apache.hadoop.hdfs.server.namenode.FSNDNCacheOp");
        classList.add("org.apache.hadoop.hdfs.server.namenode.InotifyFSEditLogOpTranslator");
    }
    
    private static void loadServerClasses4DataNode() {
	List<String> classList = new ArrayList<String>();
	componentClassListMap.put("DataNode", classList);
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedBlockReader");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.ErasureCodingWorker");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedBlockReconstructor");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedBlockWriter");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedReconstructionInfo");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedBlockChecksumReconstructor");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedBlockChecksumMd5CrcReconstructor");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedReconstructor");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedReader");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedWriter");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.StripedBlockChecksumCompositeCrcReconstructor");
        classList.add("org.apache.hadoop.hdfs.server.datanode.erasurecode.package-info");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BlockReceiver");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DNConf");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ProvidedReplica");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BlockSender");
        classList.add("org.apache.hadoop.hdfs.server.datanode.SecureDataNodeStarter");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BlockPoolSliceStorage");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DataNodeLayoutVersion");
        classList.add("org.apache.hadoop.hdfs.server.datanode.FinalizedProvidedReplica");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BPOfferService");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ProfilingFileIoEvents");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaWaitingToBeRecovered");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DataXceiverServer");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaHandler");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DiskBalancer");
        classList.add("org.apache.hadoop.hdfs.server.datanode.metrics.DataNodeMetricHelper");
        classList.add("org.apache.hadoop.hdfs.server.datanode.metrics.FSDatasetMBean");
        classList.add("org.apache.hadoop.hdfs.server.datanode.metrics.DataNodePeerMetrics");
        classList.add("org.apache.hadoop.hdfs.server.datanode.metrics.OutlierDetector");
        classList.add("org.apache.hadoop.hdfs.server.datanode.metrics.DataNodeDiskMetrics");
        classList.add("org.apache.hadoop.hdfs.server.datanode.metrics.DataNodeMetrics");
        classList.add("org.apache.hadoop.hdfs.server.datanode.FileIoProvider");
        classList.add("org.apache.hadoop.hdfs.server.datanode.FaultInjectorFileIoEvents");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DirectoryScanner");
        classList.add("org.apache.hadoop.hdfs.server.datanode.IncrementalBlockReportManager");
        classList.add("org.apache.hadoop.hdfs.server.datanode.UnexpectedReplicaStateException");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DataNodeMXBean");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReportBadBlockAction");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.webhdfs.DataNodeUGIProvider");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.webhdfs.ExceptionHandler");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.webhdfs.HdfsWriter");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.webhdfs.ParameterParser");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.webhdfs.WebHdfsHandler");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.DatanodeHttpServer");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.URLDispatcher");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.RestCsrfPreventionFilterHandler");
        classList.add("org.apache.hadoop.hdfs.server.datanode.web.SimpleHttpProxyHandler");
        classList.add("org.apache.hadoop.hdfs.server.datanode.VolumeScanner");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaBeingWritten");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.ThrottledAsyncChecker");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.AbstractFuture");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.TimeoutFuture");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.VolumeCheckResult");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.Checkable");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.StorageLocationChecker");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.DatasetVolumeChecker");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.package-info");
        classList.add("org.apache.hadoop.hdfs.server.datanode.checker.AsyncChecker");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BlockChecksumHelper");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.RoundRobinVolumeChoosingPolicy");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.LengthInputStream");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.ReplicaInputStreams");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.DataNodeVolumeMetrics");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.FsVolumeSpi");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.AddBlockPoolException");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.BlockPoolSlice");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.ProvidedVolumeImpl");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetImpl");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.MappableBlock");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.RamDiskReplicaLruTracker");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.VolumeFailureInfo");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetAsyncDiskService");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.ReservedSpaceCalculator");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.ReplicaMap");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetCache");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsVolumeImplBuilder");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetUtil");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsDatasetFactory");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsVolumeList");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.RamDiskAsyncLazyPersistService");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.FsVolumeImpl");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.impl.RamDiskReplicaTracker");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.AvailableSpaceVolumeChoosingPolicy");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.VolumeChoosingPolicy");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.ReplicaOutputStreams");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.FsVolumeReference");
        classList.add("org.apache.hadoop.hdfs.server.datanode.fsdataset.FsDatasetSpi");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BlockPoolManager");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BPServiceActorActionException");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaUnderRecovery");
        classList.add("org.apache.hadoop.hdfs.server.datanode.FinalizedReplica");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BPServiceActorAction");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaInfo");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaInPipeline");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaBuilder");
        classList.add("org.apache.hadoop.hdfs.server.datanode.Replica");
        classList.add("org.apache.hadoop.hdfs.server.datanode.LocalReplica");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DatanodeUtil");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BPServiceActor");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DataNodeFaultInjector");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DataNode");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BlockScanner");
        classList.add("org.apache.hadoop.hdfs.server.datanode.LocalReplicaInPipeline");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ShortCircuitRegistry");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ReplicaAlreadyExistsException");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ErrorReportAction");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DataXceiver");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DiskFileCorruptException");
        classList.add("org.apache.hadoop.hdfs.server.datanode.StorageLocation");
        classList.add("org.apache.hadoop.hdfs.server.datanode.ChunkChecksum");
        classList.add("org.apache.hadoop.hdfs.server.datanode.DataStorage");
        classList.add("org.apache.hadoop.hdfs.server.datanode.BlockRecoveryWorker");
}

    private static void loadServerClasses4JournalNode() {
	List<String> classList = new ArrayList<String>();
	componentClassListMap.put("JournalNode", classList);
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournalNodeSyncer");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournalNodeMXBean");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.GetJournalEditServlet");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournalNodeHttpServer");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournalNodeRpcServer");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.Journal");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournaledEditsCache");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournalMetrics");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournalFaultInjector");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JNStorage");
        classList.add("org.apache.hadoop.hdfs.qjournal.server.JournalNode");
    } 

    private static void loadServerClasses() {
	if (componentClassListMap.size() > 0)
	    return;
 	loadServerClasses4NameNode();	
 	loadServerClasses4DataNode();	
	loadServerClasses4JournalNode();
	loadServerClasses4ApplicationHistoryServer();
	loadServerClasses4NodeManager();
	loadServerClasses4ResourceManager();
    }
  
    /**
     * msx
     * <code>getComponentClassListMap</code>
     * @return Map
     */
    public static Map<String, List<String>> getComponentClassListMap() {
        return componentClassListMap;
    }
     
    /**
     * msx
     * <code>getStartStackMap</code>
     * @return Map
     */
    public static Map<Long, String> getTidComponentMap() {
        return tidComponentMap;
    }
    
    /**
     * msx
     * <code>getStartStackMap</code>
     * @return Map
     */
    public static Map<String, List<Long>> getComponentTidListMap() {
        return componentTidListMap;
    }
    
    /**
     * msx
     * <code>getStartStackMap</code>
     * @return Map
     */
    public static Map getStartStackMap() {
        return startStackMap;
    }
    
    /**
     * msx
     * <code>getInitStackMap</code>
     * @return Map
     */
    public static Map getInitStackMap() {
        return initStackMap;
    }

    private void findComponentByTid(Long tid, Long parentTid, StackTraceElement[] parentStack) {
	loadServerClasses();
        StackTraceElement[] stack = parentStack;
        String component = null;

        // if parent is a component thread, find the component and return
        if ((component = tidComponentMap.get(parentTid)) != null) {
            tidComponentMap.put(tid, component);
            componentTidListMap.get(component).add(tid);
            return;
        }

        // trace back who invokes this start()
        if (stack != null) {
            for (int i = (stack.length-1); i >= 2; i--) {
                StackTraceElement s = stack[i];
                for (String keyComponent : componentClassListMap.keySet()) {
		    List<String> classList = componentClassListMap.get(keyComponent);
		    if (classList != null && classList.contains(s.getClassName())) {
			// start() comes from this component class
                        component = keyComponent;
                        tidComponentMap.put(tid, component);
                        List<Long> tidList = componentTidListMap.get(component);
                        if (tidList == null)
                            tidList = new ArrayList<Long>();
                        tidList.add(tid);
                        componentTidListMap.put(component, tidList);
                        return;
		    }
		}
            }
        }
        return;
  }
   
    /**
     * Causes this thread to begin execution; the Java Virtual Machine
     * calls the <code>run</code> method of this thread.
     * <p>
     * The result is that two threads are running concurrently: the
     * current thread (which returns from the call to the
     * <code>start</code> method) and the other thread (which executes its
     * <code>run</code> method).
     * <p>
     * It is never legal to start a thread more than once.
     * In particular, a thread may not be restarted once it has completed
     * execution.
     *
     * @exception  IllegalThreadStateException  if the thread was already
     *               started.
     * @see        #run()
     * @see        #stop()
     */
    public synchronized void start() {
	// msx
        if (startStackMap.get(this.tid) == null) {
	    startStackMap.put(this.tid, Thread.currentThread().getStackTrace());
	}

        Long childTid = this.tid;
        Long parentTid = Thread.currentThread().getId();
        StackTraceElement[] parentStack =  Thread.currentThread().getStackTrace();
        findComponentByTid(childTid, parentTid, parentStack);

        /**
         * This method is not invoked for the main method thread or "system"
         * group threads created/set up by the VM. Any new functionality added
         * to this method in the future may have to also be added to the VM.
         *
         * A zero status value corresponds to state "NEW".
         */
        if (threadStatus != 0)
            throw new IllegalThreadStateException();

        /* Notify the group that this thread is about to be started
         * so that it can be added to the group's list of threads
         * and the group's unstarted count can be decremented. */
        group.add(this);

        boolean started = false;
        try {
            start0();
            started = true;
        } finally {
            try {
                if (!started) {
                    group.threadStartFailed(this);
                }
            } catch (Throwable ignore) {
                /* do nothing. If start0 threw a Throwable then
                  it will be passed up the call stack */
            }
        }
    }

    private native void start0();

    /**
     * If this thread was constructed using a separate
     * <code>Runnable</code> run object, then that
     * <code>Runnable</code> object's <code>run</code> method is called;
     * otherwise, this method does nothing and returns.
     * <p>
     * Subclasses of <code>Thread</code> should override this method.
     *
     * @see     #start()
     * @see     #stop()
     * @see     #Thread(ThreadGroup, Runnable, String)
     */
    @Override
    public void run() {
        if (target != null) {
            target.run();
        }
    }

    /**
     * This method is called by the system to give a Thread
     * a chance to clean up before it actually exits.
     */
    private void exit() {
        if (group != null) {
            group.threadTerminated(this);
            group = null;
        }
        /* Aggressively null out all reference fields: see bug 4006245 */
        target = null;
        /* Speed the release of some of these resources */
        threadLocals = null;
        inheritableThreadLocals = null;
        inheritedAccessControlContext = null;
        blocker = null;
        uncaughtExceptionHandler = null;
    }

    /**
     * Forces the thread to stop executing.
     * <p>
     * If there is a security manager installed, its <code>checkAccess</code>
     * method is called with <code>this</code>
     * as its argument. This may result in a
     * <code>SecurityException</code> being raised (in the current thread).
     * <p>
     * If this thread is different from the current thread (that is, the current
     * thread is trying to stop a thread other than itself), the
     * security manager's <code>checkPermission</code> method (with a
     * <code>RuntimePermission("stopThread")</code> argument) is called in
     * addition.
     * Again, this may result in throwing a
     * <code>SecurityException</code> (in the current thread).
     * <p>
     * The thread represented by this thread is forced to stop whatever
     * it is doing abnormally and to throw a newly created
     * <code>ThreadDeath</code> object as an exception.
     * <p>
     * It is permitted to stop a thread that has not yet been started.
     * If the thread is eventually started, it immediately terminates.
     * <p>
     * An application should not normally try to catch
     * <code>ThreadDeath</code> unless it must do some extraordinary
     * cleanup operation (note that the throwing of
     * <code>ThreadDeath</code> causes <code>finally</code> clauses of
     * <code>try</code> statements to be executed before the thread
     * officially dies).  If a <code>catch</code> clause catches a
     * <code>ThreadDeath</code> object, it is important to rethrow the
     * object so that the thread actually dies.
     * <p>
     * The top-level error handler that reacts to otherwise uncaught
     * exceptions does not print out a message or otherwise notify the
     * application if the uncaught exception is an instance of
     * <code>ThreadDeath</code>.
     *
     * @exception  SecurityException  if the current thread cannot
     *               modify this thread.
     * @see        #interrupt()
     * @see        #checkAccess()
     * @see        #run()
     * @see        #start()
     * @see        ThreadDeath
     * @see        ThreadGroup#uncaughtException(Thread,Throwable)
     * @see        SecurityManager#checkAccess(Thread)
     * @see        SecurityManager#checkPermission
     * @deprecated This method is inherently unsafe.  Stopping a thread with
     *       Thread.stop causes it to unlock all of the monitors that it
     *       has locked (as a natural consequence of the unchecked
     *       <code>ThreadDeath</code> exception propagating up the stack).  If
     *       any of the objects previously protected by these monitors were in
     *       an inconsistent state, the damaged objects become visible to
     *       other threads, potentially resulting in arbitrary behavior.  Many
     *       uses of <code>stop</code> should be replaced by code that simply
     *       modifies some variable to indicate that the target thread should
     *       stop running.  The target thread should check this variable
     *       regularly, and return from its run method in an orderly fashion
     *       if the variable indicates that it is to stop running.  If the
     *       target thread waits for long periods (on a condition variable,
     *       for example), the <code>interrupt</code> method should be used to
     *       interrupt the wait.
     *       For more information, see
     *       <a href="{@docRoot}/../technotes/guides/concurrency/threadPrimitiveDeprecation.html">Why
     *       are Thread.stop, Thread.suspend and Thread.resume Deprecated?</a>.
     */
    @Deprecated
    public final void stop() {
        SecurityManager security = System.getSecurityManager();
        if (security != null) {
            checkAccess();
            if (this != Thread.currentThread()) {
                security.checkPermission(SecurityConstants.STOP_THREAD_PERMISSION);
            }
        }
        // A zero status value corresponds to "NEW", it can't change to
        // not-NEW because we hold the lock.
        if (threadStatus != 0) {
            resume(); // Wake up thread if it was suspended; no-op otherwise
        }

        // The VM can handle all thread states
        stop0(new ThreadDeath());
    }

    /**
     * Throws {@code UnsupportedOperationException}.
     *
     * @param obj ignored
     *
     * @deprecated This method was originally designed to force a thread to stop
     *        and throw a given {@code Throwable} as an exception. It was
     *        inherently unsafe (see {@link #stop()} for details), and furthermore
     *        could be used to generate exceptions that the target thread was
     *        not prepared to handle.
     *        For more information, see
     *        <a href="{@docRoot}/../technotes/guides/concurrency/threadPrimitiveDeprecation.html">Why
     *        are Thread.stop, Thread.suspend and Thread.resume Deprecated?</a>.
     */
    @Deprecated
    public final synchronized void stop(Throwable obj) {
        throw new UnsupportedOperationException();
    }

    /**
     * Interrupts this thread.
     *
     * <p> Unless the current thread is interrupting itself, which is
     * always permitted, the {@link #checkAccess() checkAccess} method
     * of this thread is invoked, which may cause a {@link
     * SecurityException} to be thrown.
     *
     * <p> If this thread is blocked in an invocation of the {@link
     * Object#wait() wait()}, {@link Object#wait(long) wait(long)}, or {@link
     * Object#wait(long, int) wait(long, int)} methods of the {@link Object}
     * class, or of the {@link #join()}, {@link #join(long)}, {@link
     * #join(long, int)}, {@link #sleep(long)}, or {@link #sleep(long, int)},
     * methods of this class, then its interrupt status will be cleared and it
     * will receive an {@link InterruptedException}.
     *
     * <p> If this thread is blocked in an I/O operation upon an {@link
     * java.nio.channels.InterruptibleChannel InterruptibleChannel}
     * then the channel will be closed, the thread's interrupt
     * status will be set, and the thread will receive a {@link
     * java.nio.channels.ClosedByInterruptException}.
     *
     * <p> If this thread is blocked in a {@link java.nio.channels.Selector}
     * then the thread's interrupt status will be set and it will return
     * immediately from the selection operation, possibly with a non-zero
     * value, just as if the selector's {@link
     * java.nio.channels.Selector#wakeup wakeup} method were invoked.
     *
     * <p> If none of the previous conditions hold then this thread's interrupt
     * status will be set. </p>
     *
     * <p> Interrupting a thread that is not alive need not have any effect.
     *
     * @throws  SecurityException
     *          if the current thread cannot modify this thread
     *
     * @revised 6.0
     * @spec JSR-51
     */
    public void interrupt() {
        if (this != Thread.currentThread())
            checkAccess();

        synchronized (blockerLock) {
            Interruptible b = blocker;
            if (b != null) {
                interrupt0();           // Just to set the interrupt flag
                b.interrupt(this);
                return;
            }
        }
        interrupt0();
    }

    /**
     * Tests whether the current thread has been interrupted.  The
     * <i>interrupted status</i> of the thread is cleared by this method.  In
     * other words, if this method were to be called twice in succession, the
     * second call would return false (unless the current thread were
     * interrupted again, after the first call had cleared its interrupted
     * status and before the second call had examined it).
     *
     * <p>A thread interruption ignored because a thread was not alive
     * at the time of the interrupt will be reflected by this method
     * returning false.
     *
     * @return  <code>true</code> if the current thread has been interrupted;
     *          <code>false</code> otherwise.
     * @see #isInterrupted()
     * @revised 6.0
     */
    public static boolean interrupted() {
        return currentThread().isInterrupted(true);
    }

    /**
     * Tests whether this thread has been interrupted.  The <i>interrupted
     * status</i> of the thread is unaffected by this method.
     *
     * <p>A thread interruption ignored because a thread was not alive
     * at the time of the interrupt will be reflected by this method
     * returning false.
     *
     * @return  <code>true</code> if this thread has been interrupted;
     *          <code>false</code> otherwise.
     * @see     #interrupted()
     * @revised 6.0
     */
    public boolean isInterrupted() {
        return isInterrupted(false);
    }

    /**
     * Tests if some Thread has been interrupted.  The interrupted state
     * is reset or not based on the value of ClearInterrupted that is
     * passed.
     */
    private native boolean isInterrupted(boolean ClearInterrupted);

    /**
     * Throws {@link NoSuchMethodError}.
     *
     * @deprecated This method was originally designed to destroy this
     *     thread without any cleanup. Any monitors it held would have
     *     remained locked. However, the method was never implemented.
     *     If if were to be implemented, it would be deadlock-prone in
     *     much the manner of {@link #suspend}. If the target thread held
     *     a lock protecting a critical system resource when it was
     *     destroyed, no thread could ever access this resource again.
     *     If another thread ever attempted to lock this resource, deadlock
     *     would result. Such deadlocks typically manifest themselves as
     *     "frozen" processes. For more information, see
     *     <a href="{@docRoot}/../technotes/guides/concurrency/threadPrimitiveDeprecation.html">
     *     Why are Thread.stop, Thread.suspend and Thread.resume Deprecated?</a>.
     * @throws NoSuchMethodError always
     */
    @Deprecated
    public void destroy() {
        throw new NoSuchMethodError();
    }

    /**
     * Tests if this thread is alive. A thread is alive if it has
     * been started and has not yet died.
     *
     * @return  <code>true</code> if this thread is alive;
     *          <code>false</code> otherwise.
     */
    public final native boolean isAlive();

    /**
     * Suspends this thread.
     * <p>
     * First, the <code>checkAccess</code> method of this thread is called
     * with no arguments. This may result in throwing a
     * <code>SecurityException </code>(in the current thread).
     * <p>
     * If the thread is alive, it is suspended and makes no further
     * progress unless and until it is resumed.
     *
     * @exception  SecurityException  if the current thread cannot modify
     *               this thread.
     * @see #checkAccess
     * @deprecated   This method has been deprecated, as it is
     *   inherently deadlock-prone.  If the target thread holds a lock on the
     *   monitor protecting a critical system resource when it is suspended, no
     *   thread can access this resource until the target thread is resumed. If
     *   the thread that would resume the target thread attempts to lock this
     *   monitor prior to calling <code>resume</code>, deadlock results.  Such
     *   deadlocks typically manifest themselves as "frozen" processes.
     *   For more information, see
     *   <a href="{@docRoot}/../technotes/guides/concurrency/threadPrimitiveDeprecation.html">Why
     *   are Thread.stop, Thread.suspend and Thread.resume Deprecated?</a>.
     */
    @Deprecated
    public final void suspend() {
        checkAccess();
        suspend0();
    }

    /**
     * Resumes a suspended thread.
     * <p>
     * First, the <code>checkAccess</code> method of this thread is called
     * with no arguments. This may result in throwing a
     * <code>SecurityException</code> (in the current thread).
     * <p>
     * If the thread is alive but suspended, it is resumed and is
     * permitted to make progress in its execution.
     *
     * @exception  SecurityException  if the current thread cannot modify this
     *               thread.
     * @see        #checkAccess
     * @see        #suspend()
     * @deprecated This method exists solely for use with {@link #suspend},
     *     which has been deprecated because it is deadlock-prone.
     *     For more information, see
     *     <a href="{@docRoot}/../technotes/guides/concurrency/threadPrimitiveDeprecation.html">Why
     *     are Thread.stop, Thread.suspend and Thread.resume Deprecated?</a>.
     */
    @Deprecated
    public final void resume() {
        checkAccess();
        resume0();
    }

    /**
     * Changes the priority of this thread.
     * <p>
     * First the <code>checkAccess</code> method of this thread is called
     * with no arguments. This may result in throwing a
     * <code>SecurityException</code>.
     * <p>
     * Otherwise, the priority of this thread is set to the smaller of
     * the specified <code>newPriority</code> and the maximum permitted
     * priority of the thread's thread group.
     *
     * @param newPriority priority to set this thread to
     * @exception  IllegalArgumentException  If the priority is not in the
     *               range <code>MIN_PRIORITY</code> to
     *               <code>MAX_PRIORITY</code>.
     * @exception  SecurityException  if the current thread cannot modify
     *               this thread.
     * @see        #getPriority
     * @see        #checkAccess()
     * @see        #getThreadGroup()
     * @see        #MAX_PRIORITY
     * @see        #MIN_PRIORITY
     * @see        ThreadGroup#getMaxPriority()
     */
    public final void setPriority(int newPriority) {
        ThreadGroup g;
        checkAccess();
        if (newPriority > MAX_PRIORITY || newPriority < MIN_PRIORITY) {
            throw new IllegalArgumentException();
        }
        if((g = getThreadGroup()) != null) {
            if (newPriority > g.getMaxPriority()) {
                newPriority = g.getMaxPriority();
            }
            setPriority0(priority = newPriority);
        }
    }

    /**
     * Returns this thread's priority.
     *
     * @return  this thread's priority.
     * @see     #setPriority
     */
    public final int getPriority() {
        return priority;
    }

    /**
     * Changes the name of this thread to be equal to the argument
     * <code>name</code>.
     * <p>
     * First the <code>checkAccess</code> method of this thread is called
     * with no arguments. This may result in throwing a
     * <code>SecurityException</code>.
     *
     * @param      name   the new name for this thread.
     * @exception  SecurityException  if the current thread cannot modify this
     *               thread.
     * @see        #getName
     * @see        #checkAccess()
     */
    public final synchronized void setName(String name) {
        checkAccess();
        if (name == null) {
            throw new NullPointerException("name cannot be null");
        }

        this.name = name;
        if (threadStatus != 0) {
            setNativeName(name);
        }
    }

    /**
     * Returns this thread's name.
     *
     * @return  this thread's name.
     * @see     #setName(String)
     */
    public final String getName() {
        return name;
    }

    /**
     * Returns the thread group to which this thread belongs.
     * This method returns null if this thread has died
     * (been stopped).
     *
     * @return  this thread's thread group.
     */
    public final ThreadGroup getThreadGroup() {
        return group;
    }

    /**
     * Returns an estimate of the number of active threads in the current
     * thread's {@linkplain java.lang.ThreadGroup thread group} and its
     * subgroups. Recursively iterates over all subgroups in the current
     * thread's thread group.
     *
     * <p> The value returned is only an estimate because the number of
     * threads may change dynamically while this method traverses internal
     * data structures, and might be affected by the presence of certain
     * system threads. This method is intended primarily for debugging
     * and monitoring purposes.
     *
     * @return  an estimate of the number of active threads in the current
     *          thread's thread group and in any other thread group that
     *          has the current thread's thread group as an ancestor
     */
    public static int activeCount() {
        return currentThread().getThreadGroup().activeCount();
    }

    /**
     * Copies into the specified array every active thread in the current
     * thread's thread group and its subgroups. This method simply
     * invokes the {@link java.lang.ThreadGroup#enumerate(Thread[])}
     * method of the current thread's thread group.
     *
     * <p> An application might use the {@linkplain #activeCount activeCount}
     * method to get an estimate of how big the array should be, however
     * <i>if the array is too short to hold all the threads, the extra threads
     * are silently ignored.</i>  If it is critical to obtain every active
     * thread in the current thread's thread group and its subgroups, the
     * invoker should verify that the returned int value is strictly less
     * than the length of {@code tarray}.
     *
     * <p> Due to the inherent race condition in this method, it is recommended
     * that the method only be used for debugging and monitoring purposes.
     *
     * @param  tarray
     *         an array into which to put the list of threads
     *
     * @return  the number of threads put into the array
     *
     * @throws  SecurityException
     *          if {@link java.lang.ThreadGroup#checkAccess} determines that
     *          the current thread cannot access its thread group
     */
    public static int enumerate(Thread tarray[]) {
        return currentThread().getThreadGroup().enumerate(tarray);
    }

    /**
     * Counts the number of stack frames in this thread. The thread must
     * be suspended.
     *
     * @return     the number of stack frames in this thread.
     * @exception  IllegalThreadStateException  if this thread is not
     *             suspended.
     * @deprecated The definition of this call depends on {@link #suspend},
     *             which is deprecated.  Further, the results of this call
     *             were never well-defined.
     */
    @Deprecated
    public native int countStackFrames();

    /**
     * Waits at most {@code millis} milliseconds for this thread to
     * die. A timeout of {@code 0} means to wait forever.
     *
     * <p> This implementation uses a loop of {@code this.wait} calls
     * conditioned on {@code this.isAlive}. As a thread terminates the
     * {@code this.notifyAll} method is invoked. It is recommended that
     * applications not use {@code wait}, {@code notify}, or
     * {@code notifyAll} on {@code Thread} instances.
     *
     * @param  millis
     *         the time to wait in milliseconds
     *
     * @throws  IllegalArgumentException
     *          if the value of {@code millis} is negative
     *
     * @throws  InterruptedException
     *          if any thread has interrupted the current thread. The
     *          <i>interrupted status</i> of the current thread is
     *          cleared when this exception is thrown.
     */
    public final synchronized void join(long millis)
    throws InterruptedException {
        long base = System.currentTimeMillis();
        long now = 0;

        if (millis < 0) {
            throw new IllegalArgumentException("timeout value is negative");
        }

        if (millis == 0) {
            while (isAlive()) {
                wait(0);
            }
        } else {
            while (isAlive()) {
                long delay = millis - now;
                if (delay <= 0) {
                    break;
                }
                wait(delay);
                now = System.currentTimeMillis() - base;
            }
        }
    }

    /**
     * Waits at most {@code millis} milliseconds plus
     * {@code nanos} nanoseconds for this thread to die.
     *
     * <p> This implementation uses a loop of {@code this.wait} calls
     * conditioned on {@code this.isAlive}. As a thread terminates the
     * {@code this.notifyAll} method is invoked. It is recommended that
     * applications not use {@code wait}, {@code notify}, or
     * {@code notifyAll} on {@code Thread} instances.
     *
     * @param  millis
     *         the time to wait in milliseconds
     *
     * @param  nanos
     *         {@code 0-999999} additional nanoseconds to wait
     *
     * @throws  IllegalArgumentException
     *          if the value of {@code millis} is negative, or the value
     *          of {@code nanos} is not in the range {@code 0-999999}
     *
     * @throws  InterruptedException
     *          if any thread has interrupted the current thread. The
     *          <i>interrupted status</i> of the current thread is
     *          cleared when this exception is thrown.
     */
    public final synchronized void join(long millis, int nanos)
    throws InterruptedException {

        if (millis < 0) {
            throw new IllegalArgumentException("timeout value is negative");
        }

        if (nanos < 0 || nanos > 999999) {
            throw new IllegalArgumentException(
                                "nanosecond timeout value out of range");
        }

        if (nanos >= 500000 || (nanos != 0 && millis == 0)) {
            millis++;
        }

        join(millis);
    }

    /**
     * Waits for this thread to die.
     *
     * <p> An invocation of this method behaves in exactly the same
     * way as the invocation
     *
     * <blockquote>
     * {@linkplain #join(long) join}{@code (0)}
     * </blockquote>
     *
     * @throws  InterruptedException
     *          if any thread has interrupted the current thread. The
     *          <i>interrupted status</i> of the current thread is
     *          cleared when this exception is thrown.
     */
    public final void join() throws InterruptedException {
        join(0);
    }

    /**
     * Prints a stack trace of the current thread to the standard error stream.
     * This method is used only for debugging.
     *
     * @see     Throwable#printStackTrace()
     */
    public static void dumpStack() {
        new Exception("Stack trace").printStackTrace();
    }

    /**
     * Marks this thread as either a {@linkplain #isDaemon daemon} thread
     * or a user thread. The Java Virtual Machine exits when the only
     * threads running are all daemon threads.
     *
     * <p> This method must be invoked before the thread is started.
     *
     * @param  on
     *         if {@code true}, marks this thread as a daemon thread
     *
     * @throws  IllegalThreadStateException
     *          if this thread is {@linkplain #isAlive alive}
     *
     * @throws  SecurityException
     *          if {@link #checkAccess} determines that the current
     *          thread cannot modify this thread
     */
    public final void setDaemon(boolean on) {
        checkAccess();
        if (isAlive()) {
            throw new IllegalThreadStateException();
        }
        daemon = on;
    }

    /**
     * Tests if this thread is a daemon thread.
     *
     * @return  <code>true</code> if this thread is a daemon thread;
     *          <code>false</code> otherwise.
     * @see     #setDaemon(boolean)
     */
    public final boolean isDaemon() {
        return daemon;
    }

    /**
     * Determines if the currently running thread has permission to
     * modify this thread.
     * <p>
     * If there is a security manager, its <code>checkAccess</code> method
     * is called with this thread as its argument. This may result in
     * throwing a <code>SecurityException</code>.
     *
     * @exception  SecurityException  if the current thread is not allowed to
     *               access this thread.
     * @see        SecurityManager#checkAccess(Thread)
     */
    public final void checkAccess() {
        SecurityManager security = System.getSecurityManager();
        if (security != null) {
            security.checkAccess(this);
        }
    }

    /**
     * Returns a string representation of this thread, including the
     * thread's name, priority, and thread group.
     *
     * @return  a string representation of this thread.
     */
    public String toString() {
        ThreadGroup group = getThreadGroup();
        if (group != null) {
            return "Thread[" + getName() + "," + getPriority() + "," +
                           group.getName() + "]";
        } else {
            return "Thread[" + getName() + "," + getPriority() + "," +
                            "" + "]";
        }
    }

    /**
     * Returns the context ClassLoader for this Thread. The context
     * ClassLoader is provided by the creator of the thread for use
     * by code running in this thread when loading classes and resources.
     * If not {@linkplain #setContextClassLoader set}, the default is the
     * ClassLoader context of the parent Thread. The context ClassLoader of the
     * primordial thread is typically set to the class loader used to load the
     * application.
     *
     * <p>If a security manager is present, and the invoker's class loader is not
     * {@code null} and is not the same as or an ancestor of the context class
     * loader, then this method invokes the security manager's {@link
     * SecurityManager#checkPermission(java.security.Permission) checkPermission}
     * method with a {@link RuntimePermission RuntimePermission}{@code
     * ("getClassLoader")} permission to verify that retrieval of the context
     * class loader is permitted.
     *
     * @return  the context ClassLoader for this Thread, or {@code null}
     *          indicating the system class loader (or, failing that, the
     *          bootstrap class loader)
     *
     * @throws  SecurityException
     *          if the current thread cannot get the context ClassLoader
     *
     * @since 1.2
     */
    @CallerSensitive
    public ClassLoader getContextClassLoader() {
        if (contextClassLoader == null)
            return null;
        SecurityManager sm = System.getSecurityManager();
        if (sm != null) {
            ClassLoader.checkClassLoaderPermission(contextClassLoader,
                                                   Reflection.getCallerClass());
        }
        return contextClassLoader;
    }

    /**
     * Sets the context ClassLoader for this Thread. The context
     * ClassLoader can be set when a thread is created, and allows
     * the creator of the thread to provide the appropriate class loader,
     * through {@code getContextClassLoader}, to code running in the thread
     * when loading classes and resources.
     *
     * <p>If a security manager is present, its {@link
     * SecurityManager#checkPermission(java.security.Permission) checkPermission}
     * method is invoked with a {@link RuntimePermission RuntimePermission}{@code
     * ("setContextClassLoader")} permission to see if setting the context
     * ClassLoader is permitted.
     *
     * @param  cl
     *         the context ClassLoader for this Thread, or null  indicating the
     *         system class loader (or, failing that, the bootstrap class loader)
     *
     * @throws  SecurityException
     *          if the current thread cannot set the context ClassLoader
     *
     * @since 1.2
     */
    public void setContextClassLoader(ClassLoader cl) {
        SecurityManager sm = System.getSecurityManager();
        if (sm != null) {
            sm.checkPermission(new RuntimePermission("setContextClassLoader"));
        }
        contextClassLoader = cl;
    }

    /**
     * Returns <tt>true</tt> if and only if the current thread holds the
     * monitor lock on the specified object.
     *
     * <p>This method is designed to allow a program to assert that
     * the current thread already holds a specified lock:
     * <pre>
     *     assert Thread.holdsLock(obj);
     * </pre>
     *
     * @param  obj the object on which to test lock ownership
     * @throws NullPointerException if obj is <tt>null</tt>
     * @return <tt>true</tt> if the current thread holds the monitor lock on
     *         the specified object.
     * @since 1.4
     */
    public static native boolean holdsLock(Object obj);

    private static final StackTraceElement[] EMPTY_STACK_TRACE
        = new StackTraceElement[0];

    /**
     * Returns an array of stack trace elements representing the stack dump
     * of this thread.  This method will return a zero-length array if
     * this thread has not started, has started but has not yet been
     * scheduled to run by the system, or has terminated.
     * If the returned array is of non-zero length then the first element of
     * the array represents the top of the stack, which is the most recent
     * method invocation in the sequence.  The last element of the array
     * represents the bottom of the stack, which is the least recent method
     * invocation in the sequence.
     *
     * <p>If there is a security manager, and this thread is not
     * the current thread, then the security manager's
     * <tt>checkPermission</tt> method is called with a
     * <tt>RuntimePermission("getStackTrace")</tt> permission
     * to see if it's ok to get the stack trace.
     *
     * <p>Some virtual machines may, under some circumstances, omit one
     * or more stack frames from the stack trace.  In the extreme case,
     * a virtual machine that has no stack trace information concerning
     * this thread is permitted to return a zero-length array from this
     * method.
     *
     * @return an array of <tt>StackTraceElement</tt>,
     * each represents one stack frame.
     *
     * @throws SecurityException
     *        if a security manager exists and its
     *        <tt>checkPermission</tt> method doesn't allow
     *        getting the stack trace of thread.
     * @see SecurityManager#checkPermission
     * @see RuntimePermission
     * @see Throwable#getStackTrace
     *
     * @since 1.5
     */
    public StackTraceElement[] getStackTrace() {
        if (this != Thread.currentThread()) {
            // check for getStackTrace permission
            SecurityManager security = System.getSecurityManager();
            if (security != null) {
                security.checkPermission(
                    SecurityConstants.GET_STACK_TRACE_PERMISSION);
            }
            // optimization so we do not call into the vm for threads that
            // have not yet started or have terminated
            if (!isAlive()) {
                return EMPTY_STACK_TRACE;
            }
            StackTraceElement[][] stackTraceArray = dumpThreads(new Thread[] {this});
            StackTraceElement[] stackTrace = stackTraceArray[0];
            // a thread that was alive during the previous isAlive call may have
            // since terminated, therefore not having a stacktrace.
            if (stackTrace == null) {
                stackTrace = EMPTY_STACK_TRACE;
            }
            return stackTrace;
        } else {
            // Don't need JVM help for current thread
            return (new Exception()).getStackTrace();
        }
    }

    /**
     * Returns a map of stack traces for all live threads.
     * The map keys are threads and each map value is an array of
     * <tt>StackTraceElement</tt> that represents the stack dump
     * of the corresponding <tt>Thread</tt>.
     * The returned stack traces are in the format specified for
     * the {@link #getStackTrace getStackTrace} method.
     *
     * <p>The threads may be executing while this method is called.
     * The stack trace of each thread only represents a snapshot and
     * each stack trace may be obtained at different time.  A zero-length
     * array will be returned in the map value if the virtual machine has
     * no stack trace information about a thread.
     *
     * <p>If there is a security manager, then the security manager's
     * <tt>checkPermission</tt> method is called with a
     * <tt>RuntimePermission("getStackTrace")</tt> permission as well as
     * <tt>RuntimePermission("modifyThreadGroup")</tt> permission
     * to see if it is ok to get the stack trace of all threads.
     *
     * @return a <tt>Map</tt> from <tt>Thread</tt> to an array of
     * <tt>StackTraceElement</tt> that represents the stack trace of
     * the corresponding thread.
     *
     * @throws SecurityException
     *        if a security manager exists and its
     *        <tt>checkPermission</tt> method doesn't allow
     *        getting the stack trace of thread.
     * @see #getStackTrace
     * @see SecurityManager#checkPermission
     * @see RuntimePermission
     * @see Throwable#getStackTrace
     *
     * @since 1.5
     */
    public static Map<Thread, StackTraceElement[]> getAllStackTraces() {
        // check for getStackTrace permission
        SecurityManager security = System.getSecurityManager();
        if (security != null) {
            security.checkPermission(
                SecurityConstants.GET_STACK_TRACE_PERMISSION);
            security.checkPermission(
                SecurityConstants.MODIFY_THREADGROUP_PERMISSION);
        }

        // Get a snapshot of the list of all threads
        Thread[] threads = getThreads();
        StackTraceElement[][] traces = dumpThreads(threads);
        Map<Thread, StackTraceElement[]> m = new HashMap<>(threads.length);
        for (int i = 0; i < threads.length; i++) {
            StackTraceElement[] stackTrace = traces[i];
            if (stackTrace != null) {
                m.put(threads[i], stackTrace);
            }
            // else terminated so we don't put it in the map
        }
        return m;
    }


    private static final RuntimePermission SUBCLASS_IMPLEMENTATION_PERMISSION =
                    new RuntimePermission("enableContextClassLoaderOverride");

    /** cache of subclass security audit results */
    /* Replace with ConcurrentReferenceHashMap when/if it appears in a future
     * release */
    private static class Caches {
        /** cache of subclass security audit results */
        static final ConcurrentMap<WeakClassKey,Boolean> subclassAudits =
            new ConcurrentHashMap<>();

        /** queue for WeakReferences to audited subclasses */
        static final ReferenceQueue<Class<?>> subclassAuditsQueue =
            new ReferenceQueue<>();
    }

    /**
     * Verifies that this (possibly subclass) instance can be constructed
     * without violating security constraints: the subclass must not override
     * security-sensitive non-final methods, or else the
     * "enableContextClassLoaderOverride" RuntimePermission is checked.
     */
    private static boolean isCCLOverridden(Class<?> cl) {
        if (cl == Thread.class)
            return false;

        processQueue(Caches.subclassAuditsQueue, Caches.subclassAudits);
        WeakClassKey key = new WeakClassKey(cl, Caches.subclassAuditsQueue);
        Boolean result = Caches.subclassAudits.get(key);
        if (result == null) {
            result = Boolean.valueOf(auditSubclass(cl));
            Caches.subclassAudits.putIfAbsent(key, result);
        }

        return result.booleanValue();
    }

    /**
     * Performs reflective checks on given subclass to verify that it doesn't
     * override security-sensitive non-final methods.  Returns true if the
     * subclass overrides any of the methods, false otherwise.
     */
    private static boolean auditSubclass(final Class<?> subcl) {
        Boolean result = AccessController.doPrivileged(
            new PrivilegedAction<Boolean>() {
                public Boolean run() {
                    for (Class<?> cl = subcl;
                         cl != Thread.class;
                         cl = cl.getSuperclass())
                    {
                        try {
                            cl.getDeclaredMethod("getContextClassLoader", new Class<?>[0]);
                            return Boolean.TRUE;
                        } catch (NoSuchMethodException ex) {
                        }
                        try {
                            Class<?>[] params = {ClassLoader.class};
                            cl.getDeclaredMethod("setContextClassLoader", params);
                            return Boolean.TRUE;
                        } catch (NoSuchMethodException ex) {
                        }
                    }
                    return Boolean.FALSE;
                }
            }
        );
        return result.booleanValue();
    }

    private native static StackTraceElement[][] dumpThreads(Thread[] threads);
    private native static Thread[] getThreads();

    /**
     * Returns the identifier of this Thread.  The thread ID is a positive
     * <tt>long</tt> number generated when this thread was created.
     * The thread ID is unique and remains unchanged during its lifetime.
     * When a thread is terminated, this thread ID may be reused.
     *
     * @return this thread's ID.
     * @since 1.5
     */
    public long getId() {
        return tid;
    }

    /**
     * A thread state.  A thread can be in one of the following states:
     * <ul>
     * <li>{@link #NEW}<br>
     *     A thread that has not yet started is in this state.
     *     </li>
     * <li>{@link #RUNNABLE}<br>
     *     A thread executing in the Java virtual machine is in this state.
     *     </li>
     * <li>{@link #BLOCKED}<br>
     *     A thread that is blocked waiting for a monitor lock
     *     is in this state.
     *     </li>
     * <li>{@link #WAITING}<br>
     *     A thread that is waiting indefinitely for another thread to
     *     perform a particular action is in this state.
     *     </li>
     * <li>{@link #TIMED_WAITING}<br>
     *     A thread that is waiting for another thread to perform an action
     *     for up to a specified waiting time is in this state.
     *     </li>
     * <li>{@link #TERMINATED}<br>
     *     A thread that has exited is in this state.
     *     </li>
     * </ul>
     *
     * <p>
     * A thread can be in only one state at a given point in time.
     * These states are virtual machine states which do not reflect
     * any operating system thread states.
     *
     * @since   1.5
     * @see #getState
     */
    public enum State {
        /**
         * Thread state for a thread which has not yet started.
         */
        NEW,

        /**
         * Thread state for a runnable thread.  A thread in the runnable
         * state is executing in the Java virtual machine but it may
         * be waiting for other resources from the operating system
         * such as processor.
         */
        RUNNABLE,

        /**
         * Thread state for a thread blocked waiting for a monitor lock.
         * A thread in the blocked state is waiting for a monitor lock
         * to enter a synchronized block/method or
         * reenter a synchronized block/method after calling
         * {@link Object#wait() Object.wait}.
         */
        BLOCKED,

        /**
         * Thread state for a waiting thread.
         * A thread is in the waiting state due to calling one of the
         * following methods:
         * <ul>
         *   <li>{@link Object#wait() Object.wait} with no timeout</li>
         *   <li>{@link #join() Thread.join} with no timeout</li>
         *   <li>{@link LockSupport#park() LockSupport.park}</li>
         * </ul>
         *
         * <p>A thread in the waiting state is waiting for another thread to
         * perform a particular action.
         *
         * For example, a thread that has called <tt>Object.wait()</tt>
         * on an object is waiting for another thread to call
         * <tt>Object.notify()</tt> or <tt>Object.notifyAll()</tt> on
         * that object. A thread that has called <tt>Thread.join()</tt>
         * is waiting for a specified thread to terminate.
         */
        WAITING,

        /**
         * Thread state for a waiting thread with a specified waiting time.
         * A thread is in the timed waiting state due to calling one of
         * the following methods with a specified positive waiting time:
         * <ul>
         *   <li>{@link #sleep Thread.sleep}</li>
         *   <li>{@link Object#wait(long) Object.wait} with timeout</li>
         *   <li>{@link #join(long) Thread.join} with timeout</li>
         *   <li>{@link LockSupport#parkNanos LockSupport.parkNanos}</li>
         *   <li>{@link LockSupport#parkUntil LockSupport.parkUntil}</li>
         * </ul>
         */
        TIMED_WAITING,

        /**
         * Thread state for a terminated thread.
         * The thread has completed execution.
         */
        TERMINATED;
    }

    /**
     * Returns the state of this thread.
     * This method is designed for use in monitoring of the system state,
     * not for synchronization control.
     *
     * @return this thread's state.
     * @since 1.5
     */
    public State getState() {
        // get current thread state
        return sun.misc.VM.toThreadState(threadStatus);
    }

    // Added in JSR-166

    /**
     * Interface for handlers invoked when a <tt>Thread</tt> abruptly
     * terminates due to an uncaught exception.
     * <p>When a thread is about to terminate due to an uncaught exception
     * the Java Virtual Machine will query the thread for its
     * <tt>UncaughtExceptionHandler</tt> using
     * {@link #getUncaughtExceptionHandler} and will invoke the handler's
     * <tt>uncaughtException</tt> method, passing the thread and the
     * exception as arguments.
     * If a thread has not had its <tt>UncaughtExceptionHandler</tt>
     * explicitly set, then its <tt>ThreadGroup</tt> object acts as its
     * <tt>UncaughtExceptionHandler</tt>. If the <tt>ThreadGroup</tt> object
     * has no
     * special requirements for dealing with the exception, it can forward
     * the invocation to the {@linkplain #getDefaultUncaughtExceptionHandler
     * default uncaught exception handler}.
     *
     * @see #setDefaultUncaughtExceptionHandler
     * @see #setUncaughtExceptionHandler
     * @see ThreadGroup#uncaughtException
     * @since 1.5
     */
    @FunctionalInterface
    public interface UncaughtExceptionHandler {
        /**
         * Method invoked when the given thread terminates due to the
         * given uncaught exception.
         * <p>Any exception thrown by this method will be ignored by the
         * Java Virtual Machine.
         * @param t the thread
         * @param e the exception
         */
        void uncaughtException(Thread t, Throwable e);
    }

    // null unless explicitly set
    private volatile UncaughtExceptionHandler uncaughtExceptionHandler;

    // null unless explicitly set
    private static volatile UncaughtExceptionHandler defaultUncaughtExceptionHandler;

    /**
     * Set the default handler invoked when a thread abruptly terminates
     * due to an uncaught exception, and no other handler has been defined
     * for that thread.
     *
     * <p>Uncaught exception handling is controlled first by the thread, then
     * by the thread's {@link ThreadGroup} object and finally by the default
     * uncaught exception handler. If the thread does not have an explicit
     * uncaught exception handler set, and the thread's thread group
     * (including parent thread groups)  does not specialize its
     * <tt>uncaughtException</tt> method, then the default handler's
     * <tt>uncaughtException</tt> method will be invoked.
     * <p>By setting the default uncaught exception handler, an application
     * can change the way in which uncaught exceptions are handled (such as
     * logging to a specific device, or file) for those threads that would
     * already accept whatever &quot;default&quot; behavior the system
     * provided.
     *
     * <p>Note that the default uncaught exception handler should not usually
     * defer to the thread's <tt>ThreadGroup</tt> object, as that could cause
     * infinite recursion.
     *
     * @param eh the object to use as the default uncaught exception handler.
     * If <tt>null</tt> then there is no default handler.
     *
     * @throws SecurityException if a security manager is present and it
     *         denies <tt>{@link RuntimePermission}
     *         (&quot;setDefaultUncaughtExceptionHandler&quot;)</tt>
     *
     * @see #setUncaughtExceptionHandler
     * @see #getUncaughtExceptionHandler
     * @see ThreadGroup#uncaughtException
     * @since 1.5
     */
    public static void setDefaultUncaughtExceptionHandler(UncaughtExceptionHandler eh) {
        SecurityManager sm = System.getSecurityManager();
        if (sm != null) {
            sm.checkPermission(
                new RuntimePermission("setDefaultUncaughtExceptionHandler")
                    );
        }

         defaultUncaughtExceptionHandler = eh;
     }

    /**
     * Returns the default handler invoked when a thread abruptly terminates
     * due to an uncaught exception. If the returned value is <tt>null</tt>,
     * there is no default.
     * @since 1.5
     * @see #setDefaultUncaughtExceptionHandler
     * @return the default uncaught exception handler for all threads
     */
    public static UncaughtExceptionHandler getDefaultUncaughtExceptionHandler(){
        return defaultUncaughtExceptionHandler;
    }

    /**
     * Returns the handler invoked when this thread abruptly terminates
     * due to an uncaught exception. If this thread has not had an
     * uncaught exception handler explicitly set then this thread's
     * <tt>ThreadGroup</tt> object is returned, unless this thread
     * has terminated, in which case <tt>null</tt> is returned.
     * @since 1.5
     * @return the uncaught exception handler for this thread
     */
    public UncaughtExceptionHandler getUncaughtExceptionHandler() {
        return uncaughtExceptionHandler != null ?
            uncaughtExceptionHandler : group;
    }

    /**
     * Set the handler invoked when this thread abruptly terminates
     * due to an uncaught exception.
     * <p>A thread can take full control of how it responds to uncaught
     * exceptions by having its uncaught exception handler explicitly set.
     * If no such handler is set then the thread's <tt>ThreadGroup</tt>
     * object acts as its handler.
     * @param eh the object to use as this thread's uncaught exception
     * handler. If <tt>null</tt> then this thread has no explicit handler.
     * @throws  SecurityException  if the current thread is not allowed to
     *          modify this thread.
     * @see #setDefaultUncaughtExceptionHandler
     * @see ThreadGroup#uncaughtException
     * @since 1.5
     */
    public void setUncaughtExceptionHandler(UncaughtExceptionHandler eh) {
        checkAccess();
        uncaughtExceptionHandler = eh;
    }

    /**
     * Dispatch an uncaught exception to the handler. This method is
     * intended to be called only by the JVM.
     */
    private void dispatchUncaughtException(Throwable e) {
        getUncaughtExceptionHandler().uncaughtException(this, e);
    }

    /**
     * Removes from the specified map any keys that have been enqueued
     * on the specified reference queue.
     */
    static void processQueue(ReferenceQueue<Class<?>> queue,
                             ConcurrentMap<? extends
                             WeakReference<Class<?>>, ?> map)
    {
        Reference<? extends Class<?>> ref;
        while((ref = queue.poll()) != null) {
            map.remove(ref);
        }
    }

    /**
     *  Weak key for Class objects.
     **/
    static class WeakClassKey extends WeakReference<Class<?>> {
        /**
         * saved value of the referent's identity hash code, to maintain
         * a consistent hash code after the referent has been cleared
         */
        private final int hash;

        /**
         * Create a new WeakClassKey to the given object, registered
         * with a queue.
         */
        WeakClassKey(Class<?> cl, ReferenceQueue<Class<?>> refQueue) {
            super(cl, refQueue);
            hash = System.identityHashCode(cl);
        }

        /**
         * Returns the identity hash code of the original referent.
         */
        @Override
        public int hashCode() {
            return hash;
        }

        /**
         * Returns true if the given object is this identical
         * WeakClassKey instance, or, if this object's referent has not
         * been cleared, if the given object is another WeakClassKey
         * instance with the identical non-null referent as this one.
         */
        @Override
        public boolean equals(Object obj) {
            if (obj == this)
                return true;

            if (obj instanceof WeakClassKey) {
                Object referent = get();
                return (referent != null) &&
                       (referent == ((WeakClassKey) obj).get());
            } else {
                return false;
            }
        }
    }


    // The following three initially uninitialized fields are exclusively
    // managed by class java.util.concurrent.ThreadLocalRandom. These
    // fields are used to build the high-performance PRNGs in the
    // concurrent code, and we can not risk accidental false sharing.
    // Hence, the fields are isolated with @Contended.

    /** The current seed for a ThreadLocalRandom */
    @sun.misc.Contended("tlr")
    long threadLocalRandomSeed;

    /** Probe hash value; nonzero if threadLocalRandomSeed initialized */
    @sun.misc.Contended("tlr")
    int threadLocalRandomProbe;

    /** Secondary seed isolated from public ThreadLocalRandom sequence */
    @sun.misc.Contended("tlr")
    int threadLocalRandomSecondarySeed;

    /* Some private helper methods */
    private native void setPriority0(int newPriority);
    private native void stop0(Object o);
    private native void suspend0();
    private native void resume0();
    private native void interrupt0();
    private native void setNativeName(String name);
}
