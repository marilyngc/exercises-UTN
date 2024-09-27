package ejerciciouno;

public class Rectangulo {

    private double ancho;
    private double alto;

    public Rectangulo(double ancho, double alto) {
        this.ancho = ancho;
        this.alto = alto;
    }

    public void verificarRectangulo() {
        if (ancho == alto) {
            esCuadrado();
        } else {
            calcularArea();
            calcularPerimetro();
        }
    }

    public boolean esCuadrado() {
        System.out.println("es cuadrado");
        return true;

    }

    private void calcularArea() {
        double area = ancho * alto;
        System.out.println("es cuadrado"); 

    }

    private void calcularPerimetro() {
        double perimetro = 2 * alto + 2 * ancho;
    }

 

    public  Rectangulo sumarRectangulo(Rectangulo otroRectangulo){
        double sumaAncho = ancho + otroRectangulo.ancho;
        double sumaAlto = alto + otroRectangulo.alto;
        
        return new Rectangulo(sumaAncho, sumaAlto);
    }
    
    public void mostrarDimensiones(){
        System.out.printf("el ancho es: %.2f y el alto es: %.2f\n",ancho, alto);
    }
    
    public static Rectangulo sumarRectangulos(Rectangulo r1, Rectangulo r2){
        double sumaAncho = r1.ancho+ r2.ancho;
        double sumaAlto = r1.alto + r2.alto;
        
        return new Rectangulo(sumaAncho, sumaAlto);
    }
}
