import java.util.*;

class CatsDogs
{
	public static void main(String[] qw)
	{
		Scanner sc = new Scanner(System.in);
		int c = sc.nextInt();
		int d = sc.nextInt();
		int legs = sc.nextInt();
		if(legs % 4 != 0)
		{
			System.out.println("NO");
		}
		else
		{
			if(d > legs/4)
			{
				System.out.println("NO");
			}
			else
			{
				int temp_legs = 0;
				if(d*2 >= c)
				{
					temp_legs = d*4;
				}
				else
				{
					temp_legs = (d*4) + (c - (d*2))*4;
				}
				if(temp_legs <= legs)
				{
					System.out.println("YES");
				}
				else
				{
					System.out.println("NO");
				}
			}
		}
	}
}
