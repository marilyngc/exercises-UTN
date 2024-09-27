/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dependencia;

import java.util.Scanner;

/**
 *
 * @author Marilyn
 */
public class Impresora {
    private boolean estaEncendida;
    
    private String hoja;
    public void encender(){
        estaEncendida = true;
    }
    
    public void imprimir(Documento documento){
        if(!estaEncendida){
            throw new RuntimeException("Imopresora apagada");
            
        }
        System.out.println(documento.getTitulo());
        
    }
    
    
    public Documento getNewDocumento(){
        return new Documento("sin titulo","sin cuerpo");
    }
    public void setHoja(){
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrese tipo de hoja");
        hoja = input.next();
    }
}
