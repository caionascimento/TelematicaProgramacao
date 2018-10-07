package q1and2;

public class Livro {
	private String titulo;
	private String autor;
	private int codigo;
	private float preco;
	
	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String t) {
		this.titulo = t;
	}
	public String getAutor() {
		return autor;
	}
	public void setAutor(String a) {
		this.autor = a;
	}
	public int getCodigo() {
		return codigo;
	}
	public void setCodigo(int c) {
		this.codigo = c;
	}
	public float getPreco() {
		return preco;
	}
	public void setPreco(float p) {
		this.preco = p;
	}
	public String toString(){
		return String.format("Titulo: %s, Autor: %s, Codigo: %d, Preço: %.2f R$", titulo, autor, codigo, preco);
	}
	
	public boolean equals(Object arrayLivros[], int totalLivros){
		Livro livro = new Livro();
		boolean teste = false;
		int i = 0;
		while (teste == false){
			if (arrayLivros[i].equals(livro.toString())){
				teste = true;
			}
			else {
				teste = false;
			}
			i++;
		}
		return teste;
	}
}


/*
 * 
 * 
 * for (int i = 0; i < totalLivros; i ++) {
			if (arrayLivros[i].equals(livro.toString())){
				teste = true;
				break;
			}
			else {
				teste = false;
			}
			i++;
			
 
 *
 *
 */




























