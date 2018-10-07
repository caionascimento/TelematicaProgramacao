package q3and4;

import java.util.Scanner;

public class TestaCirculo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner (System.in);
		Circulo circulo = new Circulo();
		
		int quantCirculo = 3;
		
		for (int i = 0; i < quantCirculo; i++) {
		
			System.out.println("Informe os dados abaixo:");
			System.out.printf("Raio: ");
			circulo.setRaio(sc.nextFloat());
			System.out.printf("X: ");
			circulo.setX(sc.nextFloat());
			System.out.printf("Y: ");
			circulo.setY(sc.nextFloat());
			circulo.setPi(3.14);
		}
	}
}
