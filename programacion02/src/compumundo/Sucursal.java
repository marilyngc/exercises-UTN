package compumundo;

import java.util.ArrayList;
import java.util.Iterator;

public class Sucursal {
    private String nombre;
    private ArrayList<Dispositivo> dispositivos;

    public Sucursal(String nombre) {
        this.nombre = nombre;
        dispositivos = new ArrayList<>();
    }

    // == es para comparar primitivos (tipo identidad) tiene el mismo hash en
    // memoria
    // equals() para comparar objetos
    // Los enums se puede comprarar con los dos
    public ArrayList<Dispositivo> dispositivosPorTipos(TipoDispositivo tipo) {
        ArrayList<Dispositivo> listaRetorno = new ArrayList<>();
        for (Dispositivo dispositivo : listaRetorno) {
            if (dispositivo.getTipo().equals(tipo)) {
                listaRetorno.add(dispositivo);
            }

        }
        return listaRetorno;
    }

    public String getName(){
        return nombre;
    }
    public void agregarDispositivo(Dispositivo d) {
        if (d != null) {
            dispositivos.add(d);

        }
    }

    public void listarDispositivos() {
        if (dispositivos.isEmpty()) {
            System.out.println("NO hay dispositivos");
        } else {
            for (Dispositivo dispositivo : dispositivos) {
                System.out.println(dispositivo);
            }
        }
    }

    // private Dispositivo buscarDispositivo(String id) {

    //     int i = 0;

    //     while (i < dispositivos.size() && !(dispositivos.get(i).getID().equals(id))) {

    //         i++;
    //     }

    //     return (i == dispositivos.size() ? null : dispositivos.get(i));
    // }

    public Dispositivo borrarDispositivo(String id) {
        Iterator<Dispositivo> iterador = dispositivos.iterator();

        while (iterador.hasNext()) {
            Dispositivo d = iterador.next();
            // iterador
            if (d.getID().equals(id)) {
                iterador.remove();
                return d;

            }

        }
        return null;

    }


    public double[] porDispositivoPorTipo(){
        int [] cantidades = new int[TipoDispositivo.values().length];
        for (Dispositivo d : dispositivos) {
            // recorro dispositivo y dio:
           cantidades[d.getTipo().ordinal()] ++; 
        }

        

        return porcentualizar(cantidades);

    }

    private double [] porcentualizar(int [] cantidades){

        double [] porcentajes = new double[cantidades.length];
        int total = dispositivos.size();
        for(int i = 0; i < cantidades.length; i++){
            porcentajes[i] = (double)(cantidades[i] * 100) / total;
        }

        return porcentajes;
    }
}
