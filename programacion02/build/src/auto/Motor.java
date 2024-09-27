/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

//La gregacion es cuando en el atributo de una clse tene una clase
// composicion es una relacion fuerte
package auto;

/**
 *
 * @author Marilyn
 */
public class Motor {
    private String numero;
    private double cilindrada;
    private String tipo;
    private int rpm;

    public Motor(String numero, double cilindrada, String tipo) {
        this.numero = numero;
        this.cilindrada = cilindrada;
        this.tipo = tipo;
    }
    
    public void subirRpm(){
        rpm += 1000;
    }
    public void setCilindrada(double cilindrada){
        if(cilindrada > 0){
             this.cilindrada = cilindrada;
            
        }
    }

    
    @Override
    public String toString() {
        return "Motor{" + "numero=" + numero + ", cilindrada=" + cilindrada + ", tipo=" + tipo + ", rpm=" + rpm + '}';
    }

    
   
    
}
