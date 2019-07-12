import java.util.*;
public class HackerearthContest
{
    ArrayList<Integer> temp;
    HackerearthContest()
    {
        temp = new ArrayList<Integer>();
    }

    ArrayList<ArrayList<Integer>> getBlocks(int n, int x, int arr[])
    {
        ArrayList<ArrayList<Integer>> val = new ArrayList<ArrayList<Integer>>();
        int start, end = 0, bl_ind = 1;
        while(end != n)
        {
            end = n > (bl_ind)*x ? bl_ind*x : n;
            val.add(new ArrayList<Integer>());
            for(start =(bl_ind-1)*x +1; start <= end; start++)
            {
                val.get(bl_ind-1).add(arr[start]);
            }
            bl_ind++;
        }
        return val;
    }

    void getArrayVals(ArrayList<ArrayList<Integer>> blocks, int blocks_len, int ind, int sum)
    {
        if(ind == blocks_len)
        {
            this.temp.add(sum);
            return;
        }
        for(int i = 0; i < blocks.get(ind).size(); i++)
        {
            getArrayVals(blocks, blocks_len, ind+1, sum*10+blocks.get(ind).get(i));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int k = sc.nextInt();
        String s = sc.next();
        char ch[] = s.toCharArray();
        int arr[] = new int[s.length()+1];
        for(int i = 1; i < arr.length; i++)
        {
            arr[i] = ch[i-1]-48;
        }
        HackerearthContest m = new HackerearthContest();
        ArrayList<ArrayList<Integer>> blocks =  m.getBlocks(n, x, arr);
        System.out.println(blocks);
        m.getArrayVals(blocks, blocks.size(), 0, 0);
        Collections.sort(m.temp);
        System.out.println(m.temp);
        System.out.println(m.temp.get(k-1));
    }
}
