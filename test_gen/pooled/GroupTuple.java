import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class GroupTuple {

    public static class Tuple {
        public String proj = "";
        public String test = "";
        public String para = "";
        public String component = "";
        public String point = "";
        public String v1 = "";
        public String v2 = "";

        public Tuple(String str[]) {
            proj=str[0];
            test=str[1];
            para=str[2];
            component=str[3];
            point=str[4];
            v1=str[5];
            v2=str[6];
        }

        @Override
        public String toString() {
            return para + "@@@" +
                component + "@@@" +
                point + "@@@" +
                v1 + "@@@" +
                v2;
        }
    }
    public static void main(String[] args) {
	try {
	    String logName = args[0];
	    int groupSize = Integer.valueOf(args[1]);
            Map<String, List<Tuple>> paraMap = new HashMap<String, List<Tuple>>();
            
            // convert log lines into map of <parameter, tuples>
	    BufferedReader reader = new BufferedReader(new FileReader(logName));
	    String line = "";
	    while ((line = reader.readLine()) != null) {
	  	String[] elements = line.split(" ");
                Tuple tuple = new Tuple(elements);
                //System.out.println("tuple: " + tuple);
                String key = tuple.para;
                List<Tuple> tupleList = null;
                if ((tupleList = paraMap.get(key)) == null) {
                    tupleList = new ArrayList<Tuple>();
                    paraMap.put(key, tupleList);
                } 
                tupleList.add(tuple);
	    }

            //System.out.println("paraMap size = " + paraMap.size());
            // override groupSize if larger than # of para
            if (groupSize > paraMap.size()) {
                groupSize = paraMap.size();
            }
            //for (Map.Entry<String, List<Tuple>> kv : paraMap.entrySet()) {
            //    System.out.println(kv.getKey() + ": " + kv.getValue());
            //}

            List<List<Tuple>> groupList = new ArrayList<List<Tuple>>();
            boolean mapIsEmpty = false;
            while (! mapIsEmpty) {
                // record parameters contained so far
                List<String> paraWeHava = new ArrayList<String>();
                List<Tuple> currentGroup = new ArrayList<Tuple>();

                // iterate map
                for (Iterator<Map.Entry<String, List<Tuple>>> it = paraMap.entrySet().iterator(); it.hasNext(); ) {
                    Map.Entry<String, List<Tuple>> p_t = it.next();
                    String k_para = p_t.getKey();
                    List<Tuple> v_tupleList = p_t.getValue();

                    if (!paraWeHava.contains(k_para)) {
                        if (v_tupleList == null || v_tupleList.size() == 0) {
                            System.out.println("ERROR!");
                            System.exit(-1);
                        }

                        // consume the first tuple
                        // if tupleForThisPara is empty, remove it from map
                        currentGroup.add(v_tupleList.remove(0));
                        if (v_tupleList.size() == 0) {
                            it.remove();
                            if (paraMap.keySet().size() == 0) {
                                mapIsEmpty = true;
                                break;
                            }
                        }
                        
                        paraWeHava.add(p_t.getKey());
                        if (currentGroup.size() >= groupSize) {
                            break;
                        }
                    }
                }

                groupList.add(currentGroup);
                /*if (currentGroup.size() == groupSize) {
                    System.out.println("Okay: group size is " + currentGroup.size());
                } else {
                    System.out.println("Sorry: we cannot find enough tuple with distinct parameters, now size is " + currentGroup.size());
                }
                for (Tuple t : currentGroup) {
                    System.out.println(t.para);
                }
                System.out.println("\n");*/
            }
            for (List<Tuple> group : groupList) {
                for (int i=0; i<group.size(); i++) {
                    Tuple t = group.get(i);
                    if (i == 0)
                        System.out.print(t.proj + " " + t.test + " ");
                    if (i == (group.size()-1))
                        System.out.print(t);
                    else
                        System.out.print(t + "%%%");
                }
                System.out.print("\n");
            }
	    
	} catch (Exception e) {
	    e.printStackTrace();
	}
    }
}
