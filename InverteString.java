package target.sistemas.desafio3;

import java.util.Scanner;


public class InverteString {
    public static void main(String[] args) {
    	// Criação de uma classe para receber a String digitada pelo Usuário 
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite uma string: ");
        String string = scanner.nextLine();
// Variavel que vai armazenar a String Invertida
        String stringInv = "";

// Criação de um Loop for para identificar todos os caracteres da String
        for (int i = string.length() - 1; i >= 0; i--) {
            stringInv += string.charAt(i);
        }
// Exibição da String 
        System.out.println("String original: " + string);
        System.out.println("String invertida: " + stringInv);

        scanner.close();
    }
}