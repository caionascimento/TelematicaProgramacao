package q8;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner (System.in);
		
		System.out.println("Opções:");
		System.out.println("1 - cadastrar pessoa");
		System.out.println("2 - remover pessoa");
		System.out.println("3 - modificar pessoa");
		System.out.println("4 - exibir pessoa");
		System.out.println("99 - sair");
		
		int opcao = sc.nextInt();
		switch(opcao) {
		case 1:
			//codigo para cadastrar a pessoa
			break;
		case 2:
			//codigo para remover a pessoa
			break;
		case 3:
			//codigo para modificar a pessoa
			break;
		case 4:
			//codigo para exibir a pessoa
			break;
		case 99:
			//codigo para sair
			break;
		default:
			//mensagem de erro quando for informado uma opção invalida
		}
		
		
	}

}
