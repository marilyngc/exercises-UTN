/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package posnet;

/**
 *
 * @author Marilyn
 */
public class Tarjeta {
    private  EntidadFinanciera entidadFinanciera;

    private String numero;
    private double saldo;
    private Cliente titular;

    public Tarjeta(EntidadFinanciera entidadFinanciera, String numero, double saldo, Cliente titular) {
        this.entidadFinanciera = entidadFinanciera;

        this.numero = numero;
        this.saldo = saldo;
        this.titular = titular;
    }
     public boolean puedoPagar(double monto){
       return saldo >= monto;
   }
     
     public void debitar(double monto){
         if(puedoPagar(monto)){
             saldo -= monto;
         }
     }
    
     public String nombreTitular(){
         return titular.nombreCompleto();
     }
}
