package posnet;

public class Persona {
    private String nombre;
    private String apellido;
    private int nroDni;
    private int nroTelefono;
    private String email;

    public Persona( String nombre,String apellido,int nroDni,int nroTelefono,String email){
        this.nombre = nombre;
        this.apellido = apellido;
        this.nroDni = nroDni;
        this.nroTelefono = nroTelefono;
        this.email = email;

    }
   
     // Getters para cada atributo
     public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public int getNroDni() {
        return nroDni;
    }

    public int getNroTelefono() {
        return nroTelefono;
    }

    public String getEmail() {
        return email;
    }
}
