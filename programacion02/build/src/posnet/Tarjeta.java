package posnet;

public class Tarjeta {
    private String entidadFinanciera;
    private int nroTarjeta;
    private double saldoDisponible;
    private Persona persona;

    public Tarjeta(String entidadFinanciera, int nroTarjeta, double saldoDisponible,
            String nombre, String apellido, int nroDni, int nroTelefono, String email) {
        this.entidadFinanciera = entidadFinanciera;
        this.nroTarjeta = nroTarjeta;
        this.saldoDisponible = saldoDisponible;
        this.persona = new Persona(nombre, apellido, nroDni, nroTelefono, email);

    }

    public String getEntidadFinanciera(){
        return entidadFinanciera;
    }
    public Persona getCliente() {
        return persona;
    }

    public int getNumeroTarjeta() {
        return nroTarjeta;
    }

    public double getSaldoDisponible() {
        return saldoDisponible;
    }

    public double validarMonto(double montoIngresado, int cuota) {
        if (montoIngresado < saldoDisponible) {
            double montoFinal = this.calcularCuota(montoIngresado, cuota);
            return montoFinal;
        } else {
            System.out.println("Saldo insuficiente");
            return 0;
        }

    }

    public double calcularCuota(double montoIngresado, int cuota) {
        double recarga = 1;
        if (cuota > 1) {
            recarga = ((cuota - 1) * 3) / (double) 100;

        }

        double porcentajeDeRecargo = montoIngresado * recarga;
        double montoFinal = montoIngresado + porcentajeDeRecargo;

        saldoDisponible -= montoFinal;
        return montoFinal;

    }

}
