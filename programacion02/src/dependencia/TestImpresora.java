/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package dependencia;

/**
 *
 * @author Marilyn
 */
public class TestImpresora {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Impresora impresoraUno = new Impresora();
        Documento doc = new Documento("Titulo","Cuerpo");
        
      
        
        try{
              impresoraUno.imprimir(doc);
        }
        catch(RuntimeException ex){
            System.out.println(ex.getMessage());
        }
    }
    
}
