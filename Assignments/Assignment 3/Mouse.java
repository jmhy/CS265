/* Mouse - A type of animal, which extends move functionality and is prey
 * 
 * Joseph Haggerty
 * 05/22/2016
 *
 * Java SE 7
 *
 * Notes - A mouse can escape the island, or die trying
 *
 */

import java.awt.Point;
import java.util.Random;

public class Mouse extends Animal
{
	public Mouse( String name, Random rng ) { super(name, rng); }
	
	@Override
	public void move()
	{
		int x = (int) this._pos.getX();
		int y = (int) this._pos.getY();

		int direction = this._rng.nextInt(4);
	
		switch(direction) //mouse can end up in water or escape via bridge
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
		
		this._pos.setLocation(x, y);
	}
}
