import java.util.*;
class Permutations
{
  // boolean visited[] = new boolean[26];
  void permutations(String cand, String rem)
  {
    boolean visited[] = new boolean[26];
    if(rem.length() == 0)
    {
      System.out.println(cand);
      return;
    }
    else
    {
      for(int i = 0; i < rem.length(); i++)
      {
        char newCand = rem.charAt(i);
        String newRem = rem.substring(0,i) + rem.substring(i+1);
        if(visited[newCand - 'a'] == false)
        {
          visited[newCand - 'a'] = true;
          permutations(cand + newCand, newRem);
        }

      }
    }
  }

  public static void main(String[]qw)
  {
    Scanner sc = new Scanner(System.in);
    Permutations p = new Permutations();
    p.permutations("", sc.next());
  }
}
