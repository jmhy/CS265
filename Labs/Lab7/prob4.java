// prob4.java - prints date and time information based on command line argument
//
// Joseph Haggerty
// 5/13/2016

import java.util.Date;

public class prob4
{
	public static void main( String[] args )
	{
		Date d = new Date();
		long milli = d.getTime();
		long s = milli / 1000;
		long days = s / 86400;
		switch( args[0] )
		{
			case "0":
				System.out.printf("milliseconds since January 1, 1970: %d\n", milli);
				break;
			case "1":
				System.out.printf("seconds since January 1, 1970: %d\n", s);
				break;
			case "2":
				System.out.printf("days since January 1, 1970: %d\n", days);
				break;
			case "3":
				System.out.println("date/time: " + d.toString());
				break;
			default:
				break;
		}
	}
}
