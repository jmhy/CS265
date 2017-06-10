/* gInt - A java representation of a Gaussian Integer
 *
 * Joseph Haggerty
 * 05/30/2016
 *
 * Java SE 7
 *
 * Notes - 
 *
 */

import java.lang.Math;

public class gInt {
	private int r;
	private int i;
	
	//initialize with only real #
	public gInt(int r) {
		this.r = r;
		this.i = 0;
	}

	//initialize with real and imaginary parts
	public gInt(int r, int i) {
		this.r = r;
		this.i = i;
	}

	//return real part
	public int real() {
		return this.r;
	}

	//return imaginary part
	public int imag() {
		return this.i;
	}

	//add two gInts, returning a new gInt
	public gInt add(gInt rhs) {
		int r = this.real() + rhs.real();
		int i = this.imag() + rhs.imag();
		return new gInt(r,i);
	}

	//multiply two gInts, returning a new gInt
	public gInt multiply(gInt rhs) {
		int r = (this.real() * rhs.real()) - (this.imag() * rhs.imag());
		int i = (this.real() * rhs.imag()) + (rhs.real() * this.imag());
		return new gInt(r,i);
	}

	//return L2 norm of this gInt
	public float norm() {
		return (float)Math.sqrt(this.real()*this.real() + this.imag()*this.imag());
	}

	//override equals for later testing
	@Override
	public boolean equals(Object obj) {
		if(!(obj instanceof gInt))
			return false;

		gInt rhs = (gInt)obj;
		return (this.real() == rhs.real() && this.imag() == rhs.imag());
	}
}
