package uninter_java;

public class Euro extends Moeda {    		// Classe Filha da classe Moeda
	
	public Euro(double valor) {
		this.valor = valor;
	}

	@Override
	public void info() {
		System.out.println("Euro: " +valor);
		
	}

	@Override
	public double converter() {
		return this.valor * 5.37; 	//5.37 é a cotação atual do Euro
	}

	@Override
	public boolean equals(Object obj) {	//Comparação da moeda adicionada com a  moeda solicitada pelo usuário para ser removida
		if(this.getClass() != obj.getClass()) {
			return false;
		}
		
		Euro objEuro = (Euro) obj; 		// conversão da classe object 
		
		if(this.valor != objEuro.valor) {
			return false;
		}
		
		return true;	
	}
}