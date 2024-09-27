/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia;

/**
 *
 * @author Marilyn
 */
public abstract class Vehiculo extends Object{

    String patente;
    String marca;
    String modelo;

    public Vehiculo(String patente, String marca, String modelo) {
  
        this.patente = patente;
        this.marca = marca;
        this.modelo = modelo;
    }

    @Override
    public String toString() {
        return "Vehiculo{" + "patente=" + patente + ", marca=" + marca + ", modelo=" + modelo + '}';
    }

    private boolean checkMotor() {
        System.out.println("todo ok");
        return true;
    }

    public void encender() {
        if (checkMotor()) {
            System.out.println("Encendiendo Vehiculo");
        }

    }

    public void frenar() {
        System.out.println("Frenando Vehiculo");
    }

    public void acelerar() {
        System.out.println("Aceleranod vehiculo");
    }

}

