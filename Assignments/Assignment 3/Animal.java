/* Animal - Abstract base class for animals with a name and random position
 * 
 * Joseph Haggerty
 * 05/22/2016
 *
 * Java SE 7
 *
 * Notes - none
 *
 */


import java.awt.Point;
import java.util.Random;

public abstract class Animal
{
	protected Point _pos;
	private String _name;
	protected Random _rng;
	
	public String getName() { return _name; }
	public Point getLocation() { return _pos; }
	public void setStartLocation()
	{
		// assuming island is 5x5 and surrounded by water/bridges
		int max = 5;
		int min = 1;
		int x = _rng.nextInt(max - min + 1) + min;
		int y = _rng.nextInt(max - min + 1) + min;
		_pos = new Point(x, y);
	}
	
	public abstract void move() ;
	
	public Animal( String name, Random rng) { _name = name; _rng = rng; }
}
