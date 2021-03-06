package org.apache.hadoop.conf;

import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Enumeration;
import org.apache.hadoop.conf.Configuration;
import java.util.concurrent.locks.ReentrantLock;

public class ConfAgent {
    private static boolean msxConfEnable = false;
    private static final String reconf_systemRootDir = "/root/ZebraConf/runner/shared/";
    private static String reconf_vvmode = "";
    private static List<HTask> h_list = new ArrayList<HTask>();

    // load just once
    static {
	loadSharedVariables();
    }
    
    public static class HTask {
        public String reconf_parameter = "";
        public String reconf_component = "";
        public String reconf_point = "";
        public int reconf_point_int = 0;
        public String reconf_v1 = "";
        public String reconf_v2 = "";

        public HTask(String para, String comp, String po, String v1, String v2) {
            this.reconf_parameter = para;
            this.reconf_component = comp;
            this.reconf_point = po;
            this.reconf_point_int = Integer.valueOf(this.reconf_point);
            this.reconf_v1 = v1.equals("null") ? null : v1;
            this.reconf_v2 = v2.equals("null") ? null : v2;
        }

        @Override
        public String toString() {
            return reconf_parameter + "," + reconf_component + "," + reconf_point +
                "," + reconf_v1 + "," + reconf_v2;
        }
    }

    private static void loadSharedVariables() {
        try {
            BufferedReader reader;
            reader = new BufferedReader(new FileReader(new File(reconf_systemRootDir + "reconf_vvmode")));
            ConfAgent.reconf_vvmode = reader.readLine();
            reader.close();
            if (!reconf_vvmode.equals("v1v1") && !reconf_vvmode.equals("v2v2") && !reconf_vvmode.equals("v1v2") && 
                !reconf_vvmode.equals("none")) {
                myErrorPrint("ERROR : wrong value of reconf_vvmode " + reconf_vvmode);
                System.exit(1);
            }
                
            reader = new BufferedReader(new FileReader("/root/reconf_test_gen/lib/enable"));
            String buffer = reader.readLine();
            reader.close();
            if (buffer.equals("true")) { 
                msxConfEnable = true;
            } else {
                msxConfEnable = false;
            }

            if (!ConfAgent.reconf_vvmode.equals("none")) {
                reader = new BufferedReader(new FileReader(new File(reconf_systemRootDir + "reconf_h_list")));
                String h_list_str = reader.readLine();
                reader.close();
        	String[] htasks = h_list_str.split("%%%");
        	//System.out.println("htasks size = " + htasks.length);
        	for (String task : htasks) {
            	    String[] fields = task.split("@@@");
            	    if (fields.length != 5) {
                        myErrorPrint("ERROR: wrong fields length");
                    }
                    HTask tt = new HTask(fields[0], fields[1], fields[2], fields[3], fields[4]);
                    h_list.add(tt);
                }
            }
	    myInfoPrint("v17.0 reconf_vvmode=" + reconf_vvmode + ", reconf_h_list=" + h_list); 
        } catch (Exception e) {
            myErrorPrint("ERROR : loadSharedVariables");
            e.printStackTrace();
        }
    }

    public static class ComponentConf {
	public Object componentObj = null;
	public String group = "";
        public Configuration rootConf = null;
        public Map<String, Long> rootConfTimestampMap = new HashMap<String, Long>();
	public Set<Configuration> confSet = new HashSet<Configuration>();
        public int index = 0;
        public Configuration originalConf = null;

	public ComponentConf(Object o, String g, Configuration c_root, int i, Configuration o_conf) {
	    this.componentObj = o;
	    this.group = g;
            this.rootConf = c_root;
	    this.confSet.add(c_root);
            this.index = i;
            this.originalConf = o_conf;
	}

        public String componentWithIndex() {
           return this.group + "." + this.index;
        }
    }

    private static Set<Configuration> unidentifiedConfSet = new HashSet<Configuration>();
    private static Set<Configuration> externalConfSet = new HashSet<Configuration>();
    private static Map<Configuration, Map<String, Long>> ocsTimestampMap = new HashMap<Configuration, Map<String, Long>>();
    private static List<ComponentConf> table = new ArrayList<ComponentConf>();
    private static Map<String, Integer> componentIndexMap = new HashMap<String, Integer>();
    
    public static Map<Thread, Object> initContext = new HashMap<Thread, Object>();

    /* helper function */
    private static synchronized ComponentConf findEntryByComponentObj(Object o) {
        List<ComponentConf> entryList = new ArrayList<ComponentConf>();
        for (ComponentConf entry : table) {
	    if (o.equals(entry.componentObj)) {
                entryList.add(entry);
	    }
	}
        if (entryList.size() == 0)
	    return null;
        if (entryList.size() > 1) {



            myErrorPrint("ERROR: sanity check failed, obj is registered by mutiple component entries");
        }

        return entryList.get(0);
    }
    
    /* helper function */
    public static synchronized ComponentConf findEntryByConf(Configuration c) {
        List<ComponentConf> entryList = new ArrayList<ComponentConf>();
        for (ComponentConf entry : table) {
	    if (entry.confSet.contains(c)) {
                entryList.add(entry);
	    }
	}
        if (entryList.size() == 0)
            return null;

        if (entryList.size() > 1) {
            String buffer = "";
            for (ComponentConf e : entryList) {
                buffer = buffer + e.componentWithIndex() + ",";
            }
            myErrorPrint("ERROR: sanity check failed, conf is shared among component entries" + buffer);
        }
	    
        return entryList.get(0);
    }

    /* helper function */
    private static synchronized ComponentConf findEntryByRootConf(Configuration r_c) {
        List<ComponentConf> entryList = new ArrayList<ComponentConf>();
        for (ComponentConf entry : table) {
	    if (entry.rootConf.equals(r_c)) {
	        entryList.add(entry);
	    }
	}
        if (entryList.size() == 0)
            return null;
        if (entryList.size() > 1) {
            String buffer = "";
            for (ComponentConf e : entryList) {
                buffer = buffer + e.componentWithIndex() + ",";
            }
            myErrorPrint("ERROR: sanity check failed, root conf is registered by mutiple component entries" + buffer);
        }
	return entryList.get(0);
    }

    private static boolean isFirstPrint1 = true;
    /* helper function */
    private static synchronized List<ComponentConf> findEntryByOriginalConf(Configuration o_c) {
        List<ComponentConf> entryList = new ArrayList<ComponentConf>();
        for (ComponentConf entry : table) {
	    if (entry.originalConf.equals(o_c)) {
                entryList.add(entry);
	    }
	}
        if (entryList.size() > 1 && isFirstPrint1) {
            String buffer = "";
            for (ComponentConf e : entryList) {
                buffer = buffer + e.componentWithIndex() + ",";
            }
            myInfoPrint("INFO: record sharing, original external conf is shared by multiple components" + buffer);
            isFirstPrint1 = false;
        }
	return entryList;
    }

    public static synchronized void updateTimestamp(Configuration c, String para, String v) {
        Long currentTime = System.currentTimeMillis();

        // c is cloned internal root conf
        ComponentConf rootConfEntry = findEntryByRootConf(c);
        if (rootConfEntry != null) {
            Map<String, Long> internal_rc_map = rootConfEntry.rootConfTimestampMap;
            internal_rc_map.put(para, currentTime);
            //myPrint("update timestamp for internal root conf with para " + para + " v " + v);
            return;
        }

        // c is external original conf
        Map<String, Long> external_oc_map = ocsTimestampMap.get(c);
        if (external_oc_map != null) {
            external_oc_map.put(para, currentTime);
            //myPrint("update timestamp for external original conf with para " + para + " v " + v);
        }
    }
    
    public static boolean enableExtend = true;

    private static List<Configuration[]> extendTable = new ArrayList<Configuration[]>();

    public static synchronized void extendMyConf(Configuration originalConf, Configuration extendedConf) {
        // ignore external-internal clone
        if (enableExtend == true) {
            ComponentConf in_entry = findEntryByConf(originalConf);
            if (in_entry != null) {
                myPrint("extendMyConf: add extended conf " + extendedConf.hashCode() + " that extends conf " +
                    originalConf.hashCode() + " into componenet " + in_entry.componentWithIndex() + "'s conf set");
                in_entry.confSet.add(extendedConf);
            } else {
                if (externalConfSet.contains(originalConf)) { // original conf is external
                    externalConfSet.add(extendedConf);
                    refreshExternalConf();
                    myPrint("extendMyConf: add extended conf " + extendedConf.hashCode() + " into external conf set");
                } else {
                    myPrint("extendMyConf: extended conf " + extendedConf.hashCode() + " from conf " + originalConf.hashCode() +
                        " cannot be identified");
                }
            }
            Configuration[] relation = new Configuration[2];
            relation[0] = originalConf;
            relation[1] = extendedConf;
            //myPrint("msx-debug extendTable add relation " + relation[0].hashCode() + 
            //    " " + relation[1].hashCode());
            extendTable.add(relation);
        }
    }

    public static synchronized void registerOrphanConf(Configuration conf) {
        // early external creation
        if (table.size() == 0) {
            externalConfSet.add(conf);
            refreshExternalConf();
            myPrint("registerOrphanConf: add early conf " + conf.hashCode() + " into externalConfSet");
            return;
        }

        // init context internal
        Object component = null;
        if ((component = initContext.get(Thread.currentThread())) != null) {
            ComponentConf in_entry = findEntryByComponentObj(component);
            if (in_entry == null) {
                myErrorPrint("ERROR: init context indicates <thread, component_obj>, but we cannot find the entry");
                return;
            } else {
                in_entry.confSet.add(conf);
                myPrint("registerOrphanConf: add init context conf " + conf.hashCode() + " into " +
                    in_entry.componentWithIndex() + "'s conf set");
                return;
            }
        }

        myPrint("registerOrphanConf: cannot identify conf " + conf.hashCode());
        return;
    } 

    // refresh when we have new original/external conf
    private static void refreshExternalConf() {
        while (true) {
            Set<Configuration> newAddedExternalConfs = new HashSet<Configuration>();

            // iterate through extend relation table
            for (Configuration[] relation : extendTable) {
                Configuration left = relation[0];
                Configuration right = relation[1];
                if ((ocsTimestampMap.keySet().contains(right) || externalConfSet.contains(right))
                    && (!ocsTimestampMap.keySet().contains(left) && !externalConfSet.contains(left))) {
                    newAddedExternalConfs.add(left);
                    myPrint("refreshExternalConf: add left external conf " + left.hashCode() + " into externalConfSet");
                }

                if ((ocsTimestampMap.keySet().contains(left) || externalConfSet.contains(left))
                    && (!ocsTimestampMap.keySet().contains(right) && !externalConfSet.contains(right))) {
                    newAddedExternalConfs.add(right);
                    myPrint("refreshExternalConf: add right external conf " + right.hashCode() + " into externalConfSet");
                }
            }
            for (Configuration c : newAddedExternalConfs) {
                externalConfSet.add(c);
            }
            if (newAddedExternalConfs.size() == 0) {
                break;
            }
        }

        List<Configuration> resolvedExternalConf = new ArrayList<Configuration>();
        for (Configuration uncertain : unidentifiedConfSet) {
            if (externalConfSet.contains(uncertain) || ocsTimestampMap.keySet().contains(uncertain)) {
                myPrint(uncertain.hashCode() + " later identified as external");
                resolvedExternalConf.add(uncertain);
            }
        }
        for (Configuration resolved : resolvedExternalConf) {
            unidentifiedConfSet.remove(resolved);
        }
    }

    public static synchronized Configuration registerMyComponent(Object componentObj, String componentGroup, 
        Configuration originConf) {

        initContext.put(Thread.currentThread(), componentObj);

        try {
            if (originConf == null) {
                myPrint("INFO: originConf is null");
                return originConf;
            }

            if (componentObj == null) {
                myPrint("INFO: componentObj is null, we don't handle static function this time");
                return originConf;
            }

            for (ComponentConf e : table) {
                if (e.confSet.contains(originConf)) {
                    myPrint("WARN: this " + componentGroup + " is subcomponent of " + e.componentWithIndex() + 
                        ", because its originConf " + originConf.hashCode() + " belongs to component " + e.componentWithIndex());
                    // stop registeration
                    initContext.remove(Thread.currentThread());
                    return originConf;
                }
            }
             
            // check if component object is registered before
            ComponentConf entryRegistered = findEntryByComponentObj(componentObj);
            if (entryRegistered != null) {
                // check group
                if (!entryRegistered.group.equals(componentGroup)) {
                    myPrint("WARN: registered component " + entryRegistered.componentWithIndex() +
                        " is being registered with a different group " + componentGroup);
                    //return originConf;
                } 

                // if originConf already exists in confset, do nothing.
                if (entryRegistered.confSet.contains(originConf)) {
                    myPrint("INFO: registered component " + entryRegistered.componentWithIndex() +
          	        " is being registered with already-exisiting conf " + originConf.hashCode());
                    return originConf;
                } else { // if originConf NOT exists in confset, check if shared with other componnets objs.
                    Configuration uniqueConf = null; 
                    
                    myPrint("WARN: try to add registered component " + entryRegistered.componentWithIndex() +
          	        "'s conf set with conf " + originConf.hashCode());
                    
                    if (true) {
                        enableExtend = false;
                        uniqueConf = new Configuration(originConf);
                        enableExtend = true;
                        myPrint("ERROR: no matter conf " + originConf.hashCode() + " is shared with component or not" +
                            ", let clone and return new conf " + uniqueConf.hashCode());
                    }
                    entryRegistered.confSet.add(uniqueConf);
                    return uniqueConf; 
                }
            } 
            
            // for unregistered new component obj
            Configuration uniqueConf = null; 
            int myIndex = 0;
            ComponentConf newComponentConf = null;
            
            if (true) {
                enableExtend = false;
                uniqueConf = new Configuration(originConf);
                enableExtend = true;
                myPrint("INFO: no matter conf " + originConf.hashCode() + " is shared with component or not" +
                    ", let clone and return new conf " + uniqueConf.hashCode());
            }

            // increment component index map
            Integer fetchedIndex = componentIndexMap.get(componentGroup);
            if (fetchedIndex == null) {
                myIndex = 1;
            } else {
                myIndex = fetchedIndex + 1;
            }
            componentIndexMap.put(componentGroup, myIndex);
            
            // add newComponentConf entry into table
            newComponentConf = new ComponentConf(componentObj, componentGroup, uniqueConf, myIndex, originConf);
            myInfoPrint("registerMyComponent for comoponent " + newComponentConf.componentWithIndex() + 
                " uniqueConf " + uniqueConf.hashCode() + " originConf " + originConf.hashCode());
            table.add(newComponentConf);

            // keep track of cloned original conf
            ocsTimestampMap.put(originConf, new HashMap<String, Long>());
            refreshExternalConf();

            return uniqueConf;
        } catch(Exception e) {
            myErrorPrint("ERROR: bug");
            e.printStackTrace();
            System.exit(1);
        }

        // should not reach here
        myErrorPrint("ERROR: should not reach here in registerMyComponent");
        return null;
    }

    public static void updateExternalConfWhenCopy(Configuration o_c) {
        List<ComponentConf> entryList = findEntryByOriginalConf(o_c);
        if (entryList.size() > 0) {
            for (Enumeration<Object> e = o_c.getProps().keys(); e.hasMoreElements();) {
                String p = (String) e.nextElement();
                // call get() to update
                String new_v = o_c.get(p);
                o_c.set(p, new_v);
            }
        }
    }

    private static boolean isFirstPrint2 = true;
    
    public static synchronized String whichV(Configuration conf, String para, String v) {
        // sanity check
        //if (msxConfEnable) {
        for (ComponentConf e : table) {
            for (Configuration i_c : e.confSet) {
                if (externalConfSet.contains(i_c)) {
                    myErrorPrint("ERROR: sanity check failed, external contains internal " + i_c.hashCode() +
                        " " + e.componentWithIndex());
                }
                if (ocsTimestampMap.keySet().contains(i_c)) {
                    myErrorPrint("ERROR: sanity check failed, original contains internal " + i_c.hashCode() +
                        " " + e.componentWithIndex());
                }
            }
        }
        //}

        // c is external original conf
        boolean isOriginal = false;
        Map<String, Long> external_oc_map = ocsTimestampMap.get(conf);
        if (external_oc_map != null) {
            if (isFirstPrint2) {
                myPrint("INFO: record sharing, original external conf is read after being used for component init");
                isFirstPrint2 = false;
            }
            isOriginal = true;
            Long externalTS = external_oc_map.get(para);
            if (externalTS == null) {
                externalTS = 0L;
            }
        
            // there could be multiple cloned internal confs
            List<ComponentConf> entrysByOriginal = findEntryByOriginalConf(conf);
            
            Long internalMaxTS = 0L;
            ComponentConf entryWithMaxTs = null;
            if (entrysByOriginal.size() == 0) {
                myErrorPrint("ERROR: cannot find entry by original conf");
            } else {
                boolean isFirst = true;
                for (ComponentConf entry : entrysByOriginal) {
                    Map<String, Long> internal_rc_map = entry.rootConfTimestampMap;
                    Long ts = internal_rc_map.get(para);
                    if (ts == null) {
                        ts = 0L;
                    }
                    if (isFirst || ts > internalMaxTS) {
                        internalMaxTS = ts;
                        entryWithMaxTs = entry;
                        isFirst = false;
                    }
                }
            }
            if (internalMaxTS > externalTS) {
                String latestV = entryWithMaxTs.rootConf.get(para);
                v = latestV;
                //myPrint("because internalTS " + internalTS + " > externalTS " + externalTS +
                //    ", substitue para " + para + " with interval value " + latestV);
            }
        }
            
        ComponentConf entry = null;
        String identified = null;
        if (externalConfSet.contains(conf)) { // 0.a external because no one has registered
            identified = "external";
        } else if (isOriginal) { // 0.b external because no one has registered
            identified = "external";
        } else {
            entry = findEntryByConf(conf);
            if (entry != null) { // 1 internal found in table
                identified = "internal";
            } 
        }
        
        if (identified != null) {
            if (identified.equals("external")) {
                myPrint(para + " can be identified as reading from " + identified + " conf " + conf.hashCode());
            } else if (identified.equals("internal")) {
                myPrint(para + " can be identified as reading from " + identified + " conf " + conf.hashCode() + 
                    " from " + entry.componentWithIndex());
            }
        } else {
            myPrint(para + " cannot be identified when reading from conf " + conf.hashCode());
            unidentifiedConfSet.add(conf);
        }

        /*if (reconf_vvmode.equals("none")) {
            if (msxConfEnable == true) {
                ComponentConf entry_found = findEntryByConf(conf);
                if (v != null) {
                    if (entry_found != null) {
                        System.out.println("msx-get " + para + " " + entry_found.componentWithIndex() + " "
                            + v + " getter");
                    } else {
                        System.out.println("msx-get " + para + " " + "unit_test" + " "
                            + v + " getter");
                    }
                }
            }
            return v;
        }*/

        // check if this para matches any tasks in h_list
        boolean para_concerned = false;
        for (HTask task : h_list) {
            if (task.reconf_parameter.equals(para)) {
                para_concerned = true;
            }
        }
        if (para_concerned == false) {
            return v;
        }

        // h_list is used after this point
        for (HTask task : h_list) {
            // parameter does not match, return v
            /*if (!para.equals(reconf_parameter)) { 
                return v;
            }*/

            // if I'm not the concerned para, continue to the next task
            if (!para.equals(task.reconf_parameter)) {
                continue;
            }

            // decide value for reconf_parameter with mode v1v1/v2v2/v1v2
            if (ConfAgent.reconf_vvmode.equals("v1v1")) {
                myPrint("get-return para " + para + " " +
                    task.reconf_v1 + " for v1v1");
                return task.reconf_v1;
            }
            
            if (ConfAgent.reconf_vvmode.equals("v2v2")) {
                myPrint("get-return para " + para + " " +
                    task.reconf_v2 + " for v2v2");
                return task.reconf_v2;
            }

            // 1. uncertain, 2. external, 3. component internal
            if (ConfAgent.reconf_vvmode.equals("v1v2")) {
                if (identified == null) { // uncertain
                    myErrorPrint("ERROR: get-return we have trouble identifying conf " + conf.hashCode() + " para " + para);
                    return task.reconf_v1;
                } else {
                    if (identified.equals("external")) {
                        myPrint("get-return para " + para + " " +
                            task.reconf_v1 + " for external");
                        return task.reconf_v1;
                    } else { 
                        // nextly,it must be internal
                        
                        // check if component group match; if not, set with v1
                        if (!entry.group.equals(task.reconf_component)) {
                            myPrint("get-return para " + para + " " +
                                task.reconf_v1 + " for other components " + entry.componentWithIndex());
                            return task.reconf_v1;
                        } else { // group match
                            // decide v1 or v2 for our interested component object based on index
                            if (task.reconf_point_int == -1) { // set odd components with v2
                                if ((entry.index % 2) == 1) {
                                    myPrint("get-return para " + para + " " +
                                        task.reconf_v2 + " for " + entry.componentWithIndex());
                                    return task.reconf_v2;
                                } else {
                                    myPrint("get-return para " + para + " " +
                                        task.reconf_v1 + " for " + entry.componentWithIndex());
                                    return task.reconf_v1;
                                }
                            } else if (task.reconf_point_int == -2) { // set even components with v2
                                if ((entry.index % 2) == 0) {
                                    myPrint("get-return para " + para + " " +
                                        task.reconf_v2 + " for " + entry.componentWithIndex());
                                    return task.reconf_v2;
                                } else {
                                    myPrint("get-return para " + para + " " +
                                        task.reconf_v1 + " for " + entry.componentWithIndex());
                                    return task.reconf_v1;
                                }
                            } else if (task.reconf_point_int == -3) { // set v2 for all components in this group
                                myPrint("get-return para " + para + " " +
                                    task.reconf_v2 + " for " + entry.componentWithIndex());
                                return task.reconf_v2;
                            } else { // set v2 to component whose index is reconf_point_int
                                if (entry.index == task.reconf_point_int) {
                                    myPrint("get-return para " + para + " " +
                                        task.reconf_v2 + " for " + entry.componentWithIndex());
                                    return task.reconf_v2;
                                } else {
                                    myPrint("get-return para " + para + " " +
                                        task.reconf_v1 + " for " + entry.componentWithIndex());
                                    return task.reconf_v1;
                                }
                            }
                        }
                    }
                } 

            }
        }
        
        // should not reach here
        myErrorPrint("ERROR: should not reach here in whichV");
        return v;
    }

    public static void myPrint(String str) { 
        if (msxConfEnable) {
            System.out.println("msx-confcontroller " + str);
        } 
    }
    
    public static void myErrorPrint(String str) { if (msxConfEnable) { System.out.println("msx-confcontroller " + str);}}
    
    public static void myInfoPrint(String str) { if (msxConfEnable) {System.out.println("msx-confcontroller " + str);}}
}
