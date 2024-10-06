package compumundo;



public class Dispositivo {
    private final String ID;
    private double precio;
    private TipoDispositivo tipoDispositivos;


    public Dispositivo(String ID, double precio, TipoDispositivo tipoDispositivos){
        this.ID = ID;
        this.precio = precio;
        this.tipoDispositivos = tipoDispositivos;
    }
   

    public TipoDispositivo getTipo(){
        return tipoDispositivos;
    }
    
    public String getID(){
        return ID;
    }
    @Override
    public String toString() {
        
        return super.toString();
    }
}
