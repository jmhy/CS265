/* Chase - A game where a cat chases a mouse until the latter escapes, drowns or is eaten
 * 
 * Joseph Haggerty
 * 05/22/2016
 *
 * Java SE 7
 *
 * Notes - The island is assumed to be 5x5, surrounded by water and 8 evenly spaced bridges
 *
 */

import java.awt.Point;
import java.util.ArrayList;
import java.util.Random;

public class Chase
{
	public static int playGame(Cat cat, Mouse mouse)
	{
		ArrayList<Point> bridges = new ArrayList<Point>();
		bridges.add(new Point(0,2));
		bridges.add(new Point(0,4));
		bridges.add(new Point(2,6));
		bridges.add(new Point(4,6));
		bridges.add(new Point(6,4));
		bridges.add(new Point(6,2));
		bridges.add(new Point(4,0));
		bridges.add(new Point(2,0));
		
		do
		{
			cat.setStartLocation();
			mouse.setStartLocation();
		}
		while ( cat.getLocation().equals(mouse.getLocation()) );
		
		while ( true )
		{
			mouse.move();
			
			if ( bridges.contains(mouse.getLocation()) )
			{
				return 0; //mouse escapes
			}
			else if ( mouse.getLocation().getX() == 0 ||
				mouse.getLocation().getX() == 6 ||
				mouse.getLocation().getY() == 0 ||
				mouse.getLocation().getY() == 6 )
			{
				return 1; //mouse drowns
			}
			else if ( cat.getLocation().equals(mouse.getLocation()) )
			{
				//no op, mouse runs into cat, but doesn't necessarily get eaten as per lab directions
			}

			cat.move();
			
			if ( cat.getLocation().equals(mouse.getLocation()) )
			{
				return 2; //cat runs into mouse and eats it
			}
		}
	}
	
	public static void main( String[] args )
	{
		Random rng = new Random();
		Cat cat = new Cat("Tabby", rng);
		Mouse mouse = new Mouse("Ratatouille", rng);
		int i = 0, escaped = 0, drowned = 0, eaten = 0;
		
		while ( i < 30 )
		{
			int result = playGame(cat, mouse);
			
			switch ( result )
			{
				case -1:
					System.out.println("placeholder");
					break;
				case 0:
					System.out.println("mouse escaped");
					escaped++;
					break;
				case 1:
					System.out.println("mouse drowned");
					drowned++;
					break;
				case 2:
					System.out.println("cat had a snack");
					eaten++;
					break;
			}
			i++;
		}
		
		System.out.println();
		
		float pct;
		pct = (escaped/30.0f)*100;
		System.out.format("mouse escaped %f percent of the time\n", pct);
		pct = (drowned/30.0f)*100;
		System.out.format("mouse drowned %f percent of the time\n", pct);
		pct = (eaten/30.0f)*100;
		System.out.format("mouse was eaten %f percent of the time\n", pct);
	}
}
