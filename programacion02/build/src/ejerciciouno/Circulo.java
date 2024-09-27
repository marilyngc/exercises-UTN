/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejerciciouno;

/**
 *
 * @author Marilyn
 */
public class Circulo {

    private double radio;

    public Circulo(double radio) {
        this.radio = radio;
    }

    public void escalarCirculo(double porcentaje) {
        if (porcentaje > -100) {
            radio += radio * (porcentaje / 100);
        } else {
            System.out.println("Tiene que ser mayor a -100");
        }

    }

    private double calcularArea() {
        double area = Math.PI * radio * radio;
        return area;

    }

    private double calcularCircunferencia() {
        double circuferencia = 2 * Math.PI * radio;
        return circuferencia;

    }

    public void mostrarDatos() {
        double area = calcularArea();
        double circunferencia = calcularCircunferencia();
        System.out.printf("El area es %.2f y cirfuferencia es: %.2f%n", area, circunferencia);

    }

}
