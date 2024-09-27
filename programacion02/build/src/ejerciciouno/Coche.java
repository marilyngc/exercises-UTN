/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejerciciouno;

/**
 *
 * @author Marilyn
 */
public class Coche {

    private String marca;
    private String modelo;
    private double kilometraje;
    private double combustibleRestante;

    public Coche(String marca, String modelo, double kilometraje, double combustibleRestante) {
        this.marca = marca;
        this.modelo = modelo;
        this.kilometraje = kilometraje;
        this.combustibleRestante = combustibleRestante;
    }

    public double calcularKilometraje(double consumoPorKm) {
        if (consumoPorKm <= 0) {
            System.out.println("Ingrese un numero mayor a 0");
        }
        return combustibleRestante / consumoPorKm;
    
    
    }
    
    public void recargarCombustible(double litros) {
        if (litros <= 0) {
            System.out.println("Ingrese un numero mayor a 0");
        }
        combustibleRestante += litros;

    }
}
