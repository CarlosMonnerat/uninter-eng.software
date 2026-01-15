package uninter_java;

import java.util.ArrayList;

public class Cofrinho {
	
	private ArrayList<Moeda> listaMoedas; 		 //Independe da nacionalidade da moeda
	
	public Cofrinho() {
		this.listaMoedas = new ArrayList<>(); 	 //Instancia a lista das moedas vazia
	}
	
	public void adicionar(Moeda moeda) { 		 //Adiciona moedas
		this.listaMoedas.add(moeda);
	}
	
	public boolean remover(Moeda moeda) {			//Remove moedas
		return this.listaMoedas.remove(moeda);
	}
	
	public void listagemMoedas() {                //Lista as moedas
		
		if (this.listaMoedas.isEmpty()) {
			System.out.println("O cofrinho está vazio");
			return;
		}
		
		for (Moeda moeda: this.listaMoedas) {    //Para cada moeda na lista, chama o método info();
			moeda.info();
		}
	}
	
	public double totalConvertido() {
		if(this.listaMoedas.isEmpty()) {
			return 0;
		}
		
		double acumulador = 0;
		for (Moeda moeda: this.listaMoedas) {   //Loooping que soma os valores das moedas
			acumulador = acumulador + moeda.converter();
		}
		return acumulador;
		
	}
}
