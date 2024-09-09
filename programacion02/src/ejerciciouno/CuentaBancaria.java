/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejerciciouno;

/**
 *
 * @author Marilyn
 */
public class CuentaBancaria {
    private double saldo;
    private String titular;
    private int numeroCuenta;

    public CuentaBancaria(double saldo, String titular, int numeroCuenta) {
        this.saldo = saldo;
        this.titular = titular;
        this.numeroCuenta = numeroCuenta;
    }
    
    public void depositarDinero(double dineroIngresado){
        saldo += dineroIngresado;
    }
    
    public void retirarDinero(double dineroARetirar){
        if(saldo > 0){
            saldo -= dineroARetirar;
        }
        else{
            System.out.println("Su retiro es mayor a lo que tiene en la cuenta");
        }
    }
    
    public void verSaldo(){
        System.out.printf("Su saldo actual es: %.2f ",saldo);
    }
}
