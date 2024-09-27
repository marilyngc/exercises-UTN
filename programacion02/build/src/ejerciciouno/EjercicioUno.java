/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejerciciouno;

/**
 *
 * @author Marilyn
 */
public class EjercicioUno {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // RECTANGULO
        Rectangulo figuraUno = new Rectangulo(50,10);
        figuraUno.verificarRectangulo();
        
        Rectangulo figuraDos = new Rectangulo(50,10);
        // sumar dos rectangulo
       // Rectangulo figuraTres = figuraUno.sumarRectangulo(figuraDos);
       
       Rectangulo rect3 = Rectangulo.sumarRectangulos(figuraUno, figuraDos);
       rect3.mostrarDimensiones();
       
        
        
        
        System.out.println("**************************************");
        // CIRCULO
        Circulo figuraCirculo = new Circulo(20);
        figuraCirculo.mostrarDatos();
        figuraCirculo.escalarCirculo(50);
        figuraCirculo.mostrarDatos();
        
         System.out.println("**************************************");
        // PERSONA
        Persona personaUno = new Persona("juan",20, 1.55);
        personaUno.esMayorDeEdad();
        personaUno.calcularIMC(55);
        
         System.out.println("**************************************");
        // COCHE
        Coche cocheUno = new Coche("honda","civic typeR",234.3,20.4);
        cocheUno.calcularKilometraje(1);
        cocheUno.recargarCombustible(5);
        
         System.out.println("**************************************");
        //CUENTA BANCARIA
        CuentaBancaria cuentaUno = new CuentaBancaria(100000.05,"marta",32456);
        cuentaUno.depositarDinero(10000);
        cuentaUno.retirarDinero(5000);
        cuentaUno.verSaldo();
        
         System.out.println("**************************************");
        //LIBRO
        Libro libroUno = new Libro("El principito","principe",156,20);
        libroUno.retrocederPagina();
        libroUno.avanzarPagina();
        libroUno.estadoLibro();
        
        System.out.println("**************************************");
        // TERMOMETRO
        Termometro termometro = new Termometro(20);
        termometro.celsiusAFahrenheit();
        termometro.fahrenheitACelsius(50);
        termometro.aumentarTemperatura(10);
    }
    
}
