package compumundo;



public class TestCompumundo{
    public static void main(String[] args) {


// ITERADORES
        // ArrayList<Integer> numeros = new ArrayList<>();
        // numeros.add(5);
        // numeros.add(2);
        // numeros.add(78);

        // Iterator<Integer> it = numeros.iterator();

        // // pasan todos
        // while (it.hasNext()) {
        //     System.out.println(it.next());
        // }
    



    //   Lenguajes.JAVASCRIPT.toString();






        Empresa empresa = new Empresa();

        cargarEmpresa(empresa);

        empresa.listarDispositivos();

        for(Dispositivo d :empresa.dispositivosPorTipos(TipoDispositivo.Computadora)){
            System.out.println(d);
        }

        System.out.println("BORRAR DISPOSITIVO ******************************");
        System.out.println(empresa.borrarDispositivo("a346tte"));


        empresa.listarDispositivos();

        System.out.println("************************");

        double[] p = empresa.porDispositivoPorTipo("Sucursal A");
        
        for (double d : p) {
            System.out.printf("%.2f %%\n",d);
        }

        
       
    }

    private static void cargarEmpresa(Empresa empresa){
        Sucursal suc1 = new Sucursal("Sucursal A");
        Sucursal suc2 = new Sucursal("Sucursal B");

        suc1.agregarDispositivo(new Dispositivo("aa35", 12400,TipoDispositivo.Computadora ));
        suc1.agregarDispositivo(new Dispositivo("a34gg", 24566,TipoDispositivo.Tablet ));
        suc1.agregarDispositivo(new Dispositivo("a56hyrf", 30000,TipoDispositivo.Telefono));

        suc2.agregarDispositivo(new Dispositivo("a346tte", 12400,TipoDispositivo.Tablet));
        suc2.agregarDispositivo(new Dispositivo("trwe", 34687,TipoDispositivo.Computadora));
        suc2.agregarDispositivo(new Dispositivo("age5", 30000,TipoDispositivo.Telefono));

        empresa.agregarSucursal(suc1);
        empresa.agregarSucursal(suc2);
    }


}