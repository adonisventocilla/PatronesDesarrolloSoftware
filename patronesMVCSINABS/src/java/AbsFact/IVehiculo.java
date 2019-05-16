/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AbsFact;

/**
 *
 * @author Edward
 */
public  class IVehiculo {
    
    private String tipo;
    private int cantidad;

   

    public static Ivehiculos create(String tipo,int cantidad){ 
      
       if(tipo.equalsIgnoreCase("auto")){
          return new auto(cantidad);
       }
       if(tipo.equalsIgnoreCase("moto")){
          return new moto(cantidad);
       }
       return null;
    }

    

    
}
