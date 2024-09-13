package posnet;

public class TestPosnetMain {
    public static void main(String[] args){
        Tarjeta tarjetaUno = new Tarjeta( "Visa", 56578523, 30000, "Marilyn", "Celis",95403554 , 1147546587, "marlyn@gmail.com");
        Tarjeta tarjetaDos = new Tarjeta("Visa", 12754923, 100000, "Marilyn", "Celis",95403554 , 1147546587, "marlyn@gmail.com");

        Tarjeta tarjetaVacia = new Tarjeta( "Visa", 12754923, 100000, "", "Celis",95403554 , 1147546587, "marlyn@gmail.com");

        Posnet posnetUno = new Posnet(20000, 5, tarjetaUno);
        Posnet posnetDos = new Posnet(10000, 2, tarjetaDos);
        
        Posnet posnetVacia = new Posnet(10000, 2, tarjetaVacia);

        posnetUno.efectuarPago();
        posnetDos.efectuarPago();
        posnetVacia.efectuarPago();
    }
}
