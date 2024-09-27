/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package calculadora;

/**
 *
 * @author Marilyn
 */
public class Calculadora {
    public static int sumar(int a, int b){
        return a + b;
    }
    public static int restar(int a, int b){
        return a - b;
    }
    public static int multiplicar(int a, int b){
        return a * b;
    }
    public static double dividir(int a, int b){
        if(b != 0){
            return (double) a / b;
        }
        throw new RuntimeException("No se puede dividir con 0");
    }
    
    
}
