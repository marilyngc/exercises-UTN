/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejerciciouno;

/**
 *
 * @author Marilyn
 */
public class Persona {
    private String nombre;
    private int edad;
    private double altura;

    public Persona(String nombre, int edad, double altura) {
        this.nombre = nombre;
        this.edad = edad;
        this.altura = altura;
    }

    
    public boolean esMayorDeEdad(){
        if(edad > 17){
            System.out.println("Es mayor");
            return true;
        }
        else{
            System.out.println("Es menor");
            return false;
        }
        
        
    }
   
    public void calcularIMC(double peso){
        double imc = peso / (altura * altura);
        System.out.printf("su IMC ES: %.2f ", imc);
    }
}
