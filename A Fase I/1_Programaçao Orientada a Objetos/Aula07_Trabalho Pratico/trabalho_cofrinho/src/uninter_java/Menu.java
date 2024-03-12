package uninter_java;

import java.util.Scanner;

public class Menu {
	
	private Scanner scan;
	private Cofrinho cofrinho;
	
	public Menu() {
		scan = new Scanner(System.in);
		cofrinho = new Cofrinho();
	}

	public void showMenu() {             					//Exibe o Menu principal quando chamado na classe Main.
		System.out.println("COFRINHO:");
		System.out.println("1 - Adicionar Moeda");
		System.out.println("2 - Remover Moeda");
		System.out.println("3 - Listar Moedas");
		System.out.println("4 - Calcular Total em Real");
		System.out.println("0 - Encerrar");
		
		String option = scan.next(); 							//Lê a opção escolhida pelo usuário
		
		switch(option) {
		case "1":
			System.out.println("Escolha uma moeda:");
			System.out.println("1 - Real");
			System.out.println("2 - Dólar");
			System.out.println("3 - Euro");
			
			int moedaEscolhida = scan.nextInt(); 				//Lê a opção escolhida pelo usuário
			
			System.out.println("Digite um valor: ");
			String stringMoeda = scan.next();
			stringMoeda = stringMoeda.replace(",", "."); 		//Substitui o primeiro argumento pelo segundo
			
			double valorMoeda = Double.valueOf(stringMoeda); 	//"valueOf" Converte o valor da moeda para um double
			System.out.println("valor: " + valorMoeda);
			
			Moeda moeda = null; 										//Criação da variável moeda 
			
			if(moedaEscolhida == 1) {
				moeda = new Real(valorMoeda);	//Instancia a moeda de acordo com a nacionalidade escolhida
			}else if(moedaEscolhida == 2){
				moeda = new Dolar(valorMoeda);
			}else if(moedaEscolhida == 3){
				moeda = new Euro(valorMoeda);	
			}else {
				System.out.println("Moeda Inválida!!!!");
				System.out.println("------------------------------------------------------");
				showMenu();
			}
			
			cofrinho.adicionar(moeda); 			// Chama o método "adicionar()" do cofrinho
			System.out.println("Moeda adicionada com sucesso!");
			System.out.println("------------------------------------------------------");
			showMenu();
			break;
			
		case "2":											//Análogo ao "case 1"
			System.out.println("Escolha uma moeda:");
			System.out.println("1 - Real");
			System.out.println("2 - Dólar");
			System.out.println("3 - Euro");
			
			int moedaEscolhida1 = scan.nextInt(); 				
			
			System.out.println("Digite um valor: ");
			String stringMoeda1 = scan.next();
			stringMoeda1 = stringMoeda1.replace(",", "."); 		
			
			double valorMoeda1 = Double.valueOf(stringMoeda1); 
			System.out.println("valor: " + valorMoeda1);
			
			Moeda moeda1 = null; 									
			
			if(moedaEscolhida1 == 1) {
				moeda1 = new Real(valorMoeda1);
			}else if(moedaEscolhida1 == 2){
				moeda1 = new Dolar(valorMoeda1);
			}else if(moedaEscolhida1 == 3){
				moeda1 = new Euro(valorMoeda1);	
			}else {
				System.out.println("------------------------------------------------------");
				showMenu();
			}
			
			boolean removido = cofrinho.remover(moeda1); //Chama o método "remover()" do cofrinho
			
			if(removido) {
				System.out.println("Moeda removida com sucesso!-");
				System.out.println("------------------------------------------------------");
				
			}else {
				System.out.println("Não existe essa moeda no cofrinho!");
				System.out.println("------------------------------------------------------");
			}
			showMenu();
			break;
			
		case "3":
			System.out.println("Lista de Moedas:");
			cofrinho.listagemMoedas();
			System.out.println("------------------------------------------------------");
			showMenu();
			break;
		
		case "4":
			double valorConvertido = cofrinho.totalConvertido();
			System.out.println("O valor total convertido para para real é: " + valorConvertido);
			System.out.println("------------------------------------------------------");
			showMenu();
			break;
			
		case "0":
			System.out.println("Programa Encerrado com Sucesso.");
			break;
		default:
			System.out.println("Opção Inválida. Tente Novamente!");
			showMenu();
			break;
		}
	}

	
}
