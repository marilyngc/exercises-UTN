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

}
