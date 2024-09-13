/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package auto;

import java.util.ArrayList;

/**
 *
 * @author Marilyn
 */
public class Estacionamiento {

    private ArrayList<Auto> autos;

    public Estacionamiento() {
        autos = new ArrayList<>();

    }

    public void agresarAuto(Auto auto) {
        if (auto == null) {
            throw new NullPointerException();
        }

        autos.add(auto);

    }

    public void listarAuto() {
        for (int i= 0;i < cantidadAutos();i++){
            System.out.println(autos.get(i));
        }
    }

    public int cantidadAutos() {
        return autos.size();

    }

}
