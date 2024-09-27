/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejerciciouno;

/**
 *
 * @author Marilyn
 */
public class Libro {

    private String titulo;
    private String autor;
    private int numeroDePaginas;
    private int paginaActual;

    public Libro(String titulo, String autor, int numeroDePaginas, int paginaActual) {
        this.titulo = titulo;
        this.autor = autor;
        this.numeroDePaginas = numeroDePaginas;
        this.paginaActual = paginaActual;

    }

    public void retrocederPagina() {
        if (paginaActual == 0) {
            System.out.println("Está en la página principal");
            
        }

        paginaActual -= 1;
        System.out.printf("Retrocedió a la página: %d\n " , paginaActual);
    }

    public void avanzarPagina() {
        if (paginaActual >= numeroDePaginas) {
            System.out.println("Terminó el libro");
        }
        paginaActual += 1;
        System.out.println("Avanzó a la página: " + paginaActual);
    }

    public void estadoLibro() {
        if (paginaActual >= numeroDePaginas) {
            System.out.println("Terminó el libro");
        } else {
            System.out.printf("Está en la pagina: %d\n", paginaActual);
        }

    }

}
