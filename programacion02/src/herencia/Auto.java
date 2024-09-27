/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia;

/**
 *
 * @author Marilyn
 */
public class Auto extends Vehiculo{
    boolean tieneGPS;

    public Auto( String patente, String marca, String modelo) {
        super(patente, marca, modelo);
        
    }
   
    public void agregarGPS(){
        tieneGPS = true;
    }

    @Override
    public String toString() {
        return "Auto{" + "tieneGPS=" + tieneGPS + '}';
    }
 
    public void ingresarRuta(){
        if(tieneGPS){
            System.out.println("ruta");
        }else{
            System.out.println("vas a usar el celular");
        }
         
    }
    
     
}
