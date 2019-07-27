import java.util.*;
class Berth
{
	public static void main(String[]qw)
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int i = 0; i < t; i++)
		{
			int x = sc.nextInt();
			int rem = x % 8;
			switch(rem)
			{
				case 0: System.out.printf("%dSL\n", x-1);break;
				case 1: System.out.printf("%dLB\n", x+3);break;
				case 2: System.out.printf("%dMB\n", x+3);break;
				case 3: System.out.printf("%dUB\n", x+3);break;
				case 4: System.out.printf("%dUB\n", x-3);break;
				case 5: System.out.printf("%dMB\n", x-3);break;
				case 6: System.out.printf("%dLB\n", x-3);break;
				case 7: System.out.printf("%dSU\n", x-1);break;
			}
		}
	}
}
