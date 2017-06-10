// prob3.java - reads in a year and determines if it is a leap year
//
// Joseph Haggerty
// 5/13/2016

public class prob3
{
	public static void main( String[] args )
	{
		if ( args.length != 1 )
			System.out.println("Error: specify exactly one arg");
		else
		{
			int year = Integer.parseInt(args[0]);
			if ( year % 4 != 0 )
				System.out.println("not a leap year!");
			else if ( year % 100 != 0 )
				System.out.println("leap year!");
			else if ( year % 400 != 0 )
				System.out.println("not a leap year!");
			else
				System.out.println("leap year!");
		}
	}
}
