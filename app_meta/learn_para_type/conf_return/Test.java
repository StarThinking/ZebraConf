import org.apache.hadoop.conf.Configuration;

class Test{
  public static void main(String[] args){
      Configuration conf = new Configuration();
      conf.setInt("dfs.int", 123);
      System.out.println(conf.getInt("dfs.int", 1));

  }

}
