/* gIntTest - A test class for gInt, a java representation of a Gaussian Integer
 *
 * Joseph Haggerty
 * 05/30/2016
 *
 * Java SE 7
 *
 * Notes - 
 *
 */

import junit.framework.*;

public class gIntTest extends TestCase {
	public gIntTest(String name) {
		super(name);
	}

	private gInt gIntR5I0;
	private gInt gIntR2I4;
	private gInt gIntR3I4;

	protected void setUp() {
		gIntR5I0 = new gInt(5);
		gIntR2I4 = new gInt(2,4);
		gIntR3I4 = new gInt(3,4);
	}

	public static Test suite() {
		return new TestSuite(gIntTest.class);
	}

	public void testEquals() {
		gInt expected = new gInt(2,4);
		Assert.assertEquals(expected,gIntR2I4);
		Assert.assertEquals(gIntR2I4,gIntR2I4);
		Assert.assertNotSame(expected,gIntR2I4);
		Assert.assertFalse(gIntR5I0.equals(gIntR2I4));
		Assert.assertFalse(expected.equals(gIntR5I0));
	}

	public void testAdd() {
		gInt expected = new gInt(7,4);
		gInt result = gIntR5I0.add(gIntR2I4);
		Assert.assertEquals(expected,result);
	}

	public void testMultiply() {
		gInt expected = new gInt(10,20);
		gInt result = gIntR5I0.multiply(gIntR2I4);
		Assert.assertEquals(expected,result);
	}

	public void testNorm() {
		float expected = 5;
		float result = gIntR5I0.norm();
		Assert.assertEquals(expected,result); 
		result = gIntR3I4.norm();
		Assert.assertEquals(expected,result);
	}

	public static void main(String args[]) {
		junit.textui.TestRunner.run(suite());
	}
}
