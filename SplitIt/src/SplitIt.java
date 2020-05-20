import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class SplitIt {
//------------------------------------------------------------------------Initialise Maps to use---------------------------------------------------------------------------------//
	static Map<String,User> User_list_email = new HashMap<String,User>(); // use .put()
	static Map<User, String> User_list_name = new HashMap<User,String>(); // use .put()
	static Map<String,User> String_to_user = new HashMap<String,User>(); // use .put()
	static String [] transactions = new String[0];
//----------------------------------------------------------------------------Invalid Choice-------------------------------------------------------------------------------------//
	public static void Invalid_choice() {
		System.out.println();
		System.out.println("|Invalid choice, please choose again!!!|");
		System.out.println();
	}
//------------------------------------------------------------------------------Add New User-------------------------------------------------------------------------------------//
	public static void new_user() {
		System.out.println();
		System.out.println("New User Option -");
		Scanner scan = new Scanner(System.in);
		System.out.println("Please enter new user's name:");
		String name = scan.next();
		Scanner scan1 = new Scanner(System.in);
		System.out.println("Please enter new user's email:");
		String email = scan1.next();

		
		User user_name = User_list_email.get(email);
		
		if (user_name != null) 
		{
			System.out.println();
			System.out.println("-----User with email already exists, try registering again with a different email.-----");
			System.out.println();
		}
		if (user_name == null) 
		{
			new User(name, email);
		}
	}
//------------------------------------------------------------------------------Add Transactions----------------------------------------------------------------------------------//
	
	public static void new_trans() 
	{
		System.out.println();
		System.out.println("New Transaction Option -");
		Scanner scan = new Scanner(System.in);
		System.out.println("Who paid?");
		String lender = scan.next();
		
		if (String_to_user.get(lender) == null) 
		{
			Scanner scn = new Scanner(System.in);
			System.out.println("Lender does not exist, please enter email ID to create a new user: ");
			String new_email = scn.next();
			
			new User(lender, new_email);
		}
		
		User lender_name = String_to_user.get(lender);
		
		Scanner scan1 = new Scanner(System.in);
		System.out.println("For what?");
		String activity = scan1.next();
		
		Scanner scan2 = new Scanner(System.in);
		System.out.println("Transaction Date:");
		String date = scan2.next();
		date += " " + scan2.next();
		
		Scanner scan3 = new Scanner(System.in);
		System.out.println("No. of people involved:");
		int participants = scan3.nextInt();
		
		Scanner scan4 = new Scanner(System.in);
		System.out.println("Total transaction amount:");
		double amount = scan4.nextDouble();
		
		double individual_amt = amount/participants;
		String [] parts = new String[participants];
		Map<String,User> map_participants = new HashMap<String,User>();
		
		for (int p=0; p <participants; p++) 
		{
			Scanner scan5 = new Scanner(System.in);
			System.out.println("Person No." + Integer.toString(p+1) +"'s name: ");
			String name = scan5.next();
			parts[p] = name;
			
			if (String_to_user.get(name) == null) 
			{
				Scanner scan6 = new Scanner(System.in);
				System.out.println("User does not exist, please enter email ID to create a new user: ");
				String new_email = scan6.next();
				new User(name, new_email);
				User user_name1 = User_list_email.get(new_email);
				map_participants.put(name, user_name1);
			}
			if (String_to_user.get(name) != null) 
			{
				map_participants.put(name, String_to_user.get(name));
			}
		}
		for (User names : map_participants.values())  
		{
			if (names.name == lender_name.name) {}
			else 
			{
				new Transaction(names, lender_name, individual_amt, activity, date, participants);
			}
//			new Transaction(names, lender_name, individual_amt, activity, date, participants);
		}
		String parts_1 = "";
		for (int f = 0; f<parts.length; f++) 
		{
			if (parts.length -1 == f) 
			{
				parts_1 += " and " + parts[f]+"." ;
			}
			else if (parts.length -2 == f) 
			{
				parts_1 += parts[f] ;
			}
			else 
			{
				parts_1 += parts[f] + ", ";
			}
		}
		String ret = lender + " paid $" + amount+ " for " + activity + " on " + date + " split with " + participants + " people: " + parts_1;
		System.out.println();
		System.out.println("TRANSACTION RECORDED: " + ret);
		add_trans(lender_name, amount, activity, date, participants);
	}
	
	public static void add_trans(User lender, double amount, String detail, String date, int participants) 
	{
		String ret = (lender.name + " paid $" + amount + " for " + detail + " on " + date + " split with " + Integer.toString(participants) + " people.");
		String[] destArray = new String[transactions.length+1];
	    for(int i = 0; i < transactions.length; i++) 
	    {
	        destArray[i] = transactions[i];
	    }
	    destArray[destArray.length - 1] = ret;
	    transactions = destArray;
	}
	
//-------------------------------------------------------------------------Transaction Summary------------------------------------------------------------------------------------//
	
	public static void trans_summary() 
	{
		if (transactions.length != 0) 
		{
			for (int t=0; t<transactions.length; t++) 
			{
				String d1 = "Transaction " + Integer.toString(t+1) + " - ";
				System.out.println(d1+ transactions[t]);
			}
		}
		else 
		{
			System.out.println("No transactions to show!");
		}
	}
//-------------------------------------------------------------------------User Summary----------------------------------------------------------------------------------------//
	public static void user_summary() 
	{
		Scanner s = new Scanner(System.in);
		System.out.println("Please enter user's name for details: ");
		String user = s.next();
		User x = String_to_user.get(user);
		System.out.println();
		System.out.println(user + " is owed a total of: $" + x.total_lent);
		if (x.total_lent > 0) 
		{
			System.out.println(user + " has to take the following amount from the following people:");
			for (User name : x.lent.keySet())  
			{
				Double y = x.lent.get(name);
				System.out.println(name.name + ": $" + y);
			}
		}
		if (x.total_lent == 0) 
		{
			System.out.println(user + " gets nothing from anyone");
		}
		System.out.println("");
		System.out.println(user + " owes a total of: $" + x.total_borrowed);
		if (x.total_borrowed > 0) 
		{
			System.out.println(user + " has to give the following amount to the following people:");
			for (User name : x.borrowed.keySet())  
			{
				Double y = x.borrowed.get(name);
				System.out.println(name.name + ": $" + y);
			}
		}
		if (x.total_borrowed == 0) 
		{
			System.out.println(user + " owes nothing to anyone");
			System.out.println();
		}
	}
//----------------------------------------------------------------------------Quit Program-----------------------------------------------------------------------------------------//
	
	public static void quit_program() 
	{
		System.out.println();
		System.out.println("Thank you for using SplitIt.\nHave a great day!");
		System.out.println();
	}
//----------------------------------------------------------------------------User Class-------------------------------------------------------------------------------------------//
	
	
	static class User{
		String name;
		String email;
		int total_borrowed;
		int total_lent;
		Map<User,Double> borrowed = new HashMap<User,Double>(); // use .put()
		Map<User,Double> lent = new HashMap<User,Double>(); // use .put()
		User(String name, String email) {
			this.name = name;
			this.email = email;
			this.total_borrowed = 0;
			this.total_lent = 0;
			User_list_name.put(this, this.email);
			User_list_email.put(this.email, this);
			String_to_user.put(this.name,this);
		}
			
	}
//------------------------------------------------------------------------Transactions Class--------------------------------------------------------------------------------------//

	
	static class Transaction{
		User borrower;
		User lender;
		double amount;
		String detail;
		Transaction(User borrower, User lender, double amount, String detail, String date, int participants) {
			this.borrower = borrower;
			this.lender = lender;
			this.amount = amount;
			this.detail = detail;
			borrower.total_borrowed += amount;
			lender.total_lent += amount;
			borrower.borrowed.put(lender, amount);
			lender.lent.put(borrower,  amount);
		}
		
	}
			
//----------------------------------------------------------------------------Main Class-----------------------------------------------------------------------------------------//	

	public static void main(String[] args) {
		System.out.println("Hello and Welcome to SplitIt!");
		System.out.println();
		new User("Jayesh", "jayesh11@bu.edu");
		new User("Sakshi", "sakshi01ag@gmail.com");
		while (true) 
		{
			//menu options
			String[] menu = new String[] {"Enter New User","Enter new Transaction","Summary of transactions", 
					"Specific User Summary","Quit"}; //add "Total Summary"

			//prints the menu options
			System.out.println("Choose any of the options from the menu below:");
			System.out.println();
			for (int x = 0; x<menu.length; x++) 
			{
				System.out.println(Integer.toString(x) + " - " + menu[x]);
			}
			
			//takes user input
			System.out.println();
			Scanner sc= new Scanner(System.in);
			System.out.println("Enter your choice: ");  
			int choice= sc.nextInt();
			
			//if user opts to quite
			if (choice == menu.length-1){quit_program(); break;}
			//if choice out of bounds
			if (choice > menu.length-1){Invalid_choice();}
			//if choice = 0
			if (choice == 0){new_user();}
			//if choice = 1
			if (choice == 1){new_trans();}
			//if choice = 2
			if (choice == 2){trans_summary();}
			//if choice = 3
			if (choice == 3){user_summary();}
			System.out.println("-----------------------Back to main Menu------------------------------");
		}
	}
}
