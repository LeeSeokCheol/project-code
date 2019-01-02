package chap02;

public class VariableExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int engScore;
		
		engScore = 10;
		System.out.println("Midterm English score : 10");
		System.out.println("Midterm English score : " + 10);
		System.out.println("Midterm English score : " + engScore);
		System.out.println("Midterm English score : " + 10+10 + "Points");
		System.out.println("Midterm English score : " + (10+10) + "Points");
		System.out.println("Midterm English score : " + engScore + "Points");
		// a = 10+10;
		engScore = engScore + 10;
		System.out.println("Midterm English score : " + engScore + "Points");
		engScore += 10; // a = a + 10;
		System.out.println("Midterm English score : " + engScore + "Points");
		double mathScore = 50.5;
		System.out.println("Midterm Math score : " + mathScore + "Points");
		// Initializing Variables
		char grade = 'B';
		System.out.println("Midterm grade is " + grade);
	}

}
