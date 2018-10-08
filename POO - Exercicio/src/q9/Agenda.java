package q9;

import java.util.*;

public class Agenda {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean fim = true;
		while (fim) {
			
			System.out.println("\nBem vindo - Escolha uma opção\n\n1-Agendar Compromisso\n2-Remover Compromisso\n3-Alterar Compromisso\n4-Exibir Compromissos\n5-Sair\n\nOpção: ");
			Scanner sc = new Scanner (System.in);
			Dados dados = new Dados();
			int opcao = sc.nextInt();
			
			switch (opcao) {
			case 1:
				System.out.println(" - Agendar - \nInforme os dados para realizar o agendamento:");
				System.out.println("Dia:");
				dados.setDia(sc.nextInt());
				System.out.println("Mês:");
				dados.setMes(sc.nextInt());
				System.out.println("Hora:");
				dados.setHora(sc.nextLine());
				System.out.println("Local:");
				dados.setLocal(sc.nextLine());
				System.out.println("Descrição:");
				dados.setDescricao(sc.nextLine());
				
				break;
			case 2:
				System.out.println(" - Remover - ");
				break;
			case 3:
				System.out.println(" - Alterar Compromisso - ");
				break;
			case 4:
				System.out.println(" - Exibir Compromissos - ");
				break;
			case 5:
				fim = false;
				break;
			default:
				System.out.println("Opção invalida");	
			}
			
		}
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
