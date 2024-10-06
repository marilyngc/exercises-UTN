package compumundo;

import java.util.ArrayList;

public class Empresa {
    private ArrayList<Sucursal> sucursales;

    public Empresa() {
        sucursales = new ArrayList<>();
    }

    public void listarDispositivos() {
        if (sucursales.isEmpty()) {
            System.out.println("No hay sucursal");

        } else {
            for (Sucursal sucursal : sucursales) {
                sucursal.listarDispositivos();
                System.out.println("********************************");
            }
        }
    }

    public void agregarSucursal(Sucursal suc) {
        if (suc != null) {
            sucursales.add(suc);

        }
    }

    public ArrayList<Dispositivo> dispositivosPorTipos(TipoDispositivo tipo) {
        ArrayList<Dispositivo> listaRetorno = new ArrayList<>();
        for (Sucursal suc : sucursales) {
            listaRetorno.addAll(suc.dispositivosPorTipos(tipo));
        }
        return listaRetorno;
    }

    public Dispositivo borrarDispositivo(String id) {
        Dispositivo borrado = null;

        int i = 0;

        while (i < sucursales.size() && borrado == null) {

            borrado = sucursales.get(i).borrarDispositivo(id);

            i++;
        }

        return borrado;
    }

    private Sucursal buscarSucursal(String nombre){
        int i = 0;
        Sucursal taret = null;
        while (i < sucursales.size() && taret == null) {

            if (sucursales.get(i).getName().equals(nombre)) {
                taret = sucursales.get(i);
                
            }
            i++;
        }

        return taret;
    }
    public double[] porDispositivoPorTipo(String nomSucursal){
        Sucursal sucursal = buscarSucursal(nomSucursal);

        return sucursal == null ? null : sucursal.porDispositivoPorTipo();

    }
}
