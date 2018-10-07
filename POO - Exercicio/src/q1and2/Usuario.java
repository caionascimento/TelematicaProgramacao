package q1and2;

import java.util.Scanner;

public class Usuario {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Livro livro = new Livro();
		
		String[] arrayLivros = new String [10];
		int[] arrayCodigo = new int [10];
		
		int totalLivros = 3;
		
		for (int encher = 0; encher < 10; encher ++) {
			arrayLivros[encher] = "0";
		}
		
		for (int quantiaLivros = 0; quantiaLivros < totalLivros; quantiaLivros++) {
			System.out.println("Cadastro de Livros");
			Scanner sc = new Scanner(System.in);
			
			System.out.printf("Titulo: ");		
			livro.setTitulo(sc.nextLine());
			
			System.out.printf("Autor: ");
			livro.setAutor(sc.next());
			
			System.out.printf("Código: ");
			livro.setCodigo(sc.nextInt());
			
			System.out.printf("Preço: ");
			livro.setPreco(sc.nextFloat());
	
			if (livro.equals(arrayLivros, totalLivros)) {
				System.out.println("Livro Já Cadastrado");
			}
			else {
				arrayLivros[quantiaLivros] = livro.toString();
			}
			
			System.out.println("");
			
		}
		System.out.println("Livros Cadastros: ");
		for (int quantia = 0; quantia < totalLivros; quantia++) {
			System.out.println(arrayLivros[quantia]);
		}
	}
}
