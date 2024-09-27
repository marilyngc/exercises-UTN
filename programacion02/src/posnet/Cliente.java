/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package posnet;

/**
 *
 * @author Marilyn
 */
public class Cliente {
    private final String DNI ;
    private String nombre;
    private String apellido;
    private int telefono;
    private String email;

    public Cliente(String DNI, String nombre, String apellido, int telefono, String email) {
        this.DNI = DNI;
        this.nombre = nombre;
        this.apellido = apellido;
        this.telefono = telefono;
        this.email = email;
    }

    public String nombreCompleto(){
        return nombre + " " + apellido;
    }
}
