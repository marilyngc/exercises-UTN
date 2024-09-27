/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencia;

import java.util.ArrayList;

/**
 *
 * @author Marilyn
 */
public class Concesionario {

    private String nombre;
    private ArrayList<Vehiculo> vehiculos;

    public Concesionario(String nombre) {
        this.nombre = nombre;
        vehiculos = new ArrayList<>();

    }

    public void agregarVehiculo(Vehiculo vehiculo) {
        if (vehiculo != null) {
            vehiculos.add(vehiculo);
        }

    }

    public void listarVehiculo() {
        if (vehiculos.isEmpty()) {
            System.out.println("no hay motos");
        } else {
            for (Vehiculo vehiculos : vehiculos) {
                System.out.println(vehiculos);
            }
        }
    }

    public void listarAutos() {
        if (vehiculos.isEmpty()) {
            System.out.println("no hay motos");
        } else {
            for (Vehiculo vehiculos : vehiculos) {
                if (vehiculos instanceof Auto) {
                    System.out.println(vehiculos);
                }
            }

        }
    }
    
      public void listarMotos() {
        if (vehiculos.isEmpty()) {
            System.out.println("no hay motos");
        } else {
            for (Vehiculo vehiculos : vehiculos) {
                if (vehiculos instanceof Moto) { // operador binario - pregunta si la instancia es de clase Moto
                    System.out.println(vehiculos);
                }
            }

        }
    }

}
