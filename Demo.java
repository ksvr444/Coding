import java.util.*;
import java.lang.*;
class Demo
{

  public static void main(String[]qw)
  {
    String s = "klsadnfnvikndf^&%^(*HJGJKHGJ<HG&%&*^%^$KJ>H(&^%#%$#JHGJH))";
    String sr = s.replaceAll("\\p{Punct}", " ");
    String arr[] = sr.split(" ");
    for(int i = 0; i < arr.length; i++)
    {
      System.out.println(arr[i]);
    }
  }
}
