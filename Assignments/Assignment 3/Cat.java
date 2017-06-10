/* Cat - A type of animal, which extends move functionality and is a predator
 * 
 * Joseph Haggerty
 * 05/22/2016
 *
 * Java SE 7
 *
 * Notes - A cat will always stay on the island
 *
 */

import java.awt.Point;
import java.util.Random;

public class Cat extends Animal
{
	public Cat( String name, Random rng ) { super(name, rng); }
	
	@Override
	public void move()
	{
		int x = (int) this._pos.getX();
		int y = (int) this._pos.getY();

		do
		{
			int direction = this._rng.nextInt(4);
		
			switch(direction)
			{
				case 0: //north
					y++;
					break;
				case 1: //east
					x++;
					break;
				case 2: //south
					y--;
					break;
				case 3: //west
					x--;
					break;
			}
		}
		while ( x == 0 || x == 6 || y == 0 || y == 6); // avoid water and bridges
		
		this._pos.setLocation(x, y);
	}
}
