/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package posnet;

/**
 *
 * @author Marilyn
 */
public class TestPosnet {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Cliente c = new Cliente("345345","juan","perez",29876234,"juan@gmail.com");
       Tarjeta tc = new Tarjeta(EntidadFinanciera.Mastercard,"superville",23453453,c);
       Posnet posnet = new Posnet();
       
       Ticket ticket = posnet.efectuarPago(tc,2000000,5);
    }
    
}
