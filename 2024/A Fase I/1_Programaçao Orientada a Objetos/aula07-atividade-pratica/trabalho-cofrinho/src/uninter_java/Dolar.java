package uninter_java;

public class Dolar extends Moeda {			// Classe Filha da classe Moeda
	
	public Dolar(double valor) {
		this.valor = valor;
	}

	@Override
	public void info() {
		System.out.println("Dólar: " +valor);
		
	}

	@Override
	public double converter() {
		return this.valor * 4.95; 	//4.95 é a cotação atual do dólar
	}

	@Override
	public boolean equals(Object obj) {	//Comparação da moeda adicionada com a  moeda solicitada pelo usuário para ser removida
		if(this.getClass() != obj.getClass()) {
			return false;
		}
		
		Dolar objDolar = (Dolar) obj; 		// conversão da classe object 
		
		if(this.valor != objDolar.valor) {
			return false;
		}
		
		return true;	
	}
}
