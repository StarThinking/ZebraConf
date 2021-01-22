public class Greet{
   int knowncount;
   public Greet()
   {
      System.out.println("Hello");
      knowncount++;
   }   
   public Greet(String language)
   {
     if(language.equals("ENGLISH"))  {System.out.println("Hello"); knowncount++; }
     else  if(language.equals("SPANISH")) {System.out.println("Hola"); knowncount++;}
     else  System.out.println("Language not recognized");
   }

   public void showCount() 
   {
     System.out.println("count : "+knowncount);
   }

   public String getBoolean() {
	return "Hello Boolean";
   }
   
   public String get() {
	return "Hello get";
   }

}
