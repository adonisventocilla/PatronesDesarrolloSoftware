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
public class moto implements Ivehiculos{
int cantidad;
 int precio=2500;
    public moto(int cantidad) {
        this.cantidad = cantidad;
    }

 
  public double cotizacion(){ 
    int res=cantidad*precio;
      return res;
    } 
  @Override
     public String getTipo(){
       
         String mens="\n PRECIO UNIT: "+precio+"\n\n"
                 + "PRECIO TOT: "+cotizacion();
                 
         return mens ;
     }
    
}
