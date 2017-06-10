// prob2.java - reads a number from command line and determines if even/odd
//
// Joseph Haggerty
// 5/13/2016

public class prob2
{
	public static void main( String[] args )
	{
		if ( args.length != 1 )
			System.out.println("Error: specify exactly one arg");
		else
		{
			int i = Integer.parseInt(args[0]);
			if ( i % 2 == 0)
				System.out.println("even");
			else
				System.out.println("odd");
		}
	}
}
