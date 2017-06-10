// Csv.java - java implementation of C++ csv reader
//
// Joseph Haggerty
// 5/20/2016

import java.io.*;
import java.util.*;

public class Csv
{
	private BufferedReader fin;
	private String line;
	private ArrayList<String> field;
	private String fieldsep;
	
	// initializes an instance of the Csv class, reads a specified csv file
	public Csv(String fname, String sep)
	{
		try
		{
			fieldsep = sep;
			FileReader freader = new FileReader(fname);
			fin = new BufferedReader(freader);
		}
		catch (FileNotFoundException ex)
		{
			System.out.println(ex.getMessage());
		}
	}
	
	// read and parse one line from the file
	public String getline()
	{
		try
		{
			line = fin.readLine();
			if (line == null)
				return line;
			else
			{
				field = split();
				return line;
			}
		}
		catch (IOException ex)
		{
			System.out.println(ex.getMessage());
			return null;
		}
	}
	
	// split lines into fields and store them
	private ArrayList<String> split()
	{
		ArrayList<String> list = new ArrayList<String>();
		StringBuffer fld = new StringBuffer();;
		int i, j;

		if (line.length() == 0)
			return list;

		i = 0;

		do {
			if (i < line.length() && line.charAt(i) == '"') // field is quoted
			{
				fld.setLength(0); // clear buf before writing to it
				j = advquoted(line, fld, ++i);
				list.add(fld.toString());
			}
			else // field not quoted
			{
				fld.setLength(0); // clear buf before writing to it
				j = advplain(line, fld, i);
				list.add(fld.toString());
			}
			i = j + 1;
		}
		while (j < line.length());

		return list;
	}
	
	// for a quoted field, returns index of next separator and writes to fld
	private int advquoted(String s, StringBuffer fld, int i)
	{
		int j;

		for (j = i; j < s.length(); j++)
		{
			if (s.charAt(j) == '"' && (++j == s.length() || s.charAt(j) != '"'))
			{
				int k = s.indexOf(fieldsep, j);
				if (k == -1) // no separator
					k = s.length();
				for (k -= j; k-- > 0; )
					fld.append(s.substring(j++));
				break;
			}
			fld.append(s.charAt(j));
		}
		return j;
	}
	
	// for unquoted field, returns index of next separator and writes to fld
	private int advplain(String s, StringBuffer fld, int i)
	{
		int j;
		
		j = s.indexOf(fieldsep, i);
		if (j == -1) // no separator
			j = s.length();
		fld.append(s.substring(i, j));
		return j;
	}
	
	// refutn n-th field
	public String getfield(int n)
	{
		if (n < 0 || n >= field.size())
			return "";
		else
			return field.get(n);
	}

	public int getnfield()
	{
		return this.field.size();
	}
	
	// test Csv class
	public static void main(String[] args)
	{
		String line;
		Csv csv = new Csv("test.csv", ",");

		while ( (line = csv.getline()) != null )
		{
			System.out.println("line = `" + line + "'");
			for (int i = 0; i < csv.getnfield(); i++)
				System.out.println("field[" + i + "] = `" + csv.getfield(i) + "'");
		}
	}
}
