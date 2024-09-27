/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package auto;

/**
 *
 * @author Marilyn
 */
public class Auto {
    private String patente;
    private String marca;
    private double precio;
    private Color color;
    private Motor motor;
    

    public Auto(String patente, String marca, double precio, Color color, String nrMotor, double cilindrada, String tipo) {
        this.patente = patente;
        this.marca = marca;
        this.precio = precio;
        this.color = color;
        this.motor = new Motor(nrMotor, cilindrada,tipo);
        
    }

    @Override
    public String toString() {
        return "Auto{" + "patente=" + patente + ", marca=" + marca + ", precio=" + precio + ", color=" + color + ", motor=" + motor + '}';
    }

    public void acelerar(){
        motor.subirRpm();
    }
    
   
}
