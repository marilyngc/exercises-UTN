package compumundo;

/**
 * Lenguajes
 */
public enum Lenguajes {
    PYTHON("interpretado",1), // sinleton
    JAVA("Hibrido",2),
    CSHARP("Hibrido",2),
    JAVASCRIPT("Interpretado",3),
    HTML("Marcado",3);

    private String tipo;
    private int cuatrimestre;

    private Lenguajes(String tipo, int cuatrimestre){
        this.tipo = tipo;
        this.cuatrimestre = cuatrimestre;
    }

    public String getTipo(){
        return tipo;
    }

    public int getCuatrimestre(){
        return cuatrimestre;
    }
    
    @Override
    public String toString() {
        
        String  nombre = super.toString();
        String capitalizado = nombre.substring(0,1) + nombre.substring(1).toLowerCase();
        return capitalizado;
    }
}