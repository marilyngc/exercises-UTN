/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package herencia;

/**
 *
 * @author Marilyn
 */
public class TestHerencia {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Concesionario concesionario = new Concesionario("Sprint automores");
       
       Auto auto1 = new Auto("fiat","palio","abc");
       Auto auto2 = new Auto("renault","palio","abc");
       Auto auto3 = new Auto("fiat","palio","abc");
       
       Moto moto1 = new Moto("Honda","palio","ABBD4");
       Moto moto2 = new Moto("Honda","palio","ABBD4");
       Moto moto3 = new Moto("Honda","palio","ABBD4");
       
       concesionario.agregarVehiculo(auto1);
       concesionario.agregarVehiculo(auto2);
       concesionario.agregarVehiculo(auto3);
       
       concesionario.agregarVehiculo(moto2);
       concesionario.agregarVehiculo(moto2);
       concesionario.agregarVehiculo(moto2);
        

       
        concesionario.listarVehiculo();
        concesionario.listarAutos();
        concesionario.listarAutos();
        
    }
    
}
