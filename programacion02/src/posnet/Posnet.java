/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package posnet;

/**
 *
 * @author Marilyn
 */
public class Posnet {

    private static final int MAX_CUOTA = 6;
    private static final int MIN_CUOTA = 1;
    private static final double PORC_CUOTA = 0.003;

    public Ticket efectuarPago(Tarjeta tarjeta, double monto, int cuotas) {
        
        try{
          validarDatos(tarjeta, monto, cuotas);  
          
          double porcRecargo =  calcularPorcentajeRecargo(cuotas);
          
          double montoTotal = monto + monto * porcRecargo;
          
          if (checkSaldo(tarjeta,monto)){
              tarjeta.debitar(monto);
              return new Ticket(tarjeta.nombreTitular(),montoTotal,cuotas);
          }
        }
        catch(Exception ex){
            System.out.println("No se puede procesar el pago");
        }
        return null;
    }

    private boolean validarDatos(Tarjeta tarjeta, double monto, int cuotas) {
        return validarTarjeta(tarjeta) && validarMonto(monto) && validarCuotas(cuotas);
    }

    private boolean validarTarjeta(Tarjeta tarjeta) {
        if (tarjeta == null) {
            throw new NullPointerException("Tarjeta nula");
        }

        return true;
    }

    private boolean validarCuotas(double cuotas) {
        if (cuotas < MAX_CUOTA || cuotas > MIN_CUOTA) {
            throw new IllegalArgumentException("Cuotas invalidas");
        }
        return true;
    }

    private boolean validarMonto(double monto) {
        if (monto <= 0) {
            throw new IllegalArgumentException("Monto invalido");

        }
        return true;
    }

    private double calcularPorcentajeRecargo(int cuotas) {
        double recargo = PORC_CUOTA * (cuotas - 1);
        return recargo;
    }

    private boolean checkSaldo(Tarjeta tarjeta, double monto) {
        return tarjeta.puedoPagar(monto);
    }
    
  
}
