/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia;

/**
 *
 * @author Marilyn
 */
public class Moto extends Vehiculo {

    boolean eslingaPuesta;

    public Moto( String patente, String marca, String modelo) {
        super(patente, marca, modelo);
        
    }

    @Override
    public String toString() {
        return "Moto{" + "eslingaPuesta=" + eslingaPuesta + '}';
    }

   
    public void bloquear(){
         if(!eslingaPuesta){
             eslingaPuesta = true;
         }
    }
    
}
