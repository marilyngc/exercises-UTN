package posnet;

public class Posnet {
    private double montoAAbonar;
    private int cantidadCuota;
    private Tarjeta tarjeta;

    public Posnet(double montoAAbonar, int cantidadCuota, Tarjeta tarjeta) {
        this.montoAAbonar = montoAAbonar;
        this.cantidadCuota = cantidadCuota;
        this.tarjeta = tarjeta;
    }

    public void efectuarPago() {
        double montoTotal = tarjeta.validarMonto(montoAAbonar, cantidadCuota);
        if (montoTotal > 0) { 
            double pagoPorMes = this.montoCadaCuota(montoTotal);
            this.generarTicket(montoTotal, pagoPorMes);
        } else {
            System.out.println("Error: Monto total inválido o saldo insuficiente.");
        }
    }

    public double montoCadaCuota(double montoTotal) {
        double porCuota = montoTotal / this.cantidadCuota;
        return porCuota;

    }

    public void generarTicket(double montoTotal, double pagoPorMes) {
        String nombreCliente = tarjeta.getCliente().getNombre();
        String apellidoCliente = tarjeta.getCliente().getApellido();

        if (tarjeta != null && !nombreCliente.isEmpty()) {
         
            System.out.printf("Nombre y apellido del cliente: %s %s%n", nombreCliente, apellidoCliente);
            System.out.printf("Monto total a pagar:%.2f%n", montoTotal);
            System.out.printf("Monto de cada cuota:%.2f%n", pagoPorMes);
            System.out.println("******************************");
        } else {
            System.out.println("Error: Cliente o tarjeta no están disponibles.");
        }

    }
}
