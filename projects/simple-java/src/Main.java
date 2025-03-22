import java.util.*;
public class Main{
public static void main(String[] args){
	Date currDate=new Date();
	System.out.println("Hello, Docker! current date: "+currDate);
	Scanner in=new Scanner(System.in);
	System.out.print("Enter your name: ");
	String name=in.next();
	System.out.println("Greetings!! "+name);
}
}
