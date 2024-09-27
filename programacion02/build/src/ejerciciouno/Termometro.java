/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejerciciouno;

/**
 *
 * @author Marilyn
 */
public class Termometro {
    private double temperatura;

    public Termometro(double temperatura) {
        this.temperatura = temperatura;
    }
    
    public void celsiusAFahrenheit(){
        double fahrenheit = (temperatura * 9/5) + 32;
        System.out.printf("grado en fahrenheit: %.2f\n", fahrenheit);
    }
    public void fahrenheitACelsius(double tempFahrenheit){
        double celsius = (tempFahrenheit - 32) * 5/9;
        System.out.printf("grado en celsius: %.2f\n", celsius);
    }
    
    public void aumentarTemperatura(double subirTemp){
        temperatura += subirTemp;
    }
}
