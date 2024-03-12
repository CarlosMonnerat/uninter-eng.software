package uninter_java;

public class Real extends Moeda { 			// Classe Filha da classe Moeda

	public Real(double valor) {
		this.valor = valor;
	}
	
	@Override
	public void info() {
		System.out.println("Real: " +valor);
		
	}

	@Override
	public double converter() {
		return this.valor;
		
	}

	@Override
	public boolean equals(Object obj) {	//Comparação da moeda adicionada com a  moeda solicitada pelo usuário para ser removida
		if(this.getClass() != obj.getClass()) {
			return false;
		}
		
		Real objReal = (Real) obj; 		// conversão da classe object 
		
		if(this.valor != objReal.valor) {
			return false;
		}
		
		return true;	
	}

	
}
