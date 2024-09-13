/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package auto;

/**
 *
 * @author Marilyn
 */
public class TestAuto {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
  
        Estacionamiento estacionamiento = new Estacionamiento();
        Auto a1 = new Auto("ABC123","fORD",10000,Color.AZUL,"ADF",1.8,"Nafta");
        Auto a2 = new Auto("EDC443","Ronault",11000,Color.ROJO,"ADF",1.8,"Nafta");
        
        estacionamiento.agresarAuto(a1);
        estacionamiento.agresarAuto(a2);
        
        estacionamiento.cantidadAutos();
         estacionamiento.listarAuto();
        
        System.out.println(a1);
    }
    
}
