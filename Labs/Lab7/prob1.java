// prob1.java - reads a name from command lines and prints it 100 times
//
// Joseph Haggerty
// 5/13/2016

public class prob1
{
	public static void main( String[] args )
	{
		if ( args.length != 1 )
			System.out.println("Error: specify exactly one arg");
		else
		{
			for ( int i = 0; i < 100; i++)
				System.out.print(args[0] + " ");
			System.out.println();
		}
	}
}
