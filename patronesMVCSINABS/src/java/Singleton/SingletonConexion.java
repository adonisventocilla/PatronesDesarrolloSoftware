/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Singleton;

import java.sql.Connection;
import java.sql.DriverManager;

/**
 *
 * @author Edward
 */
public class SingletonConexion {
    private static SingletonConexion instance=null;
    private SingletonConexion(){
        
    }
    
    public static SingletonConexion get_Ins(){
        if(instance==null){
            instance=new SingletonConexion(); 
            return  instance; 
        }
        return instance;
    }
    
    public Connection get_conexion(){
          Connection cn=null;
         
          try{
             Class.forName("com.mysql.jdbc.Driver");
             cn=DriverManager.getConnection("jdbc:mysql://localhost/login","root","46514716"); 
             conectar();
          }catch(Exception e){ 
              desconectar();
          }
        return cn;  
    }
    
    private void conectar(){
        System.out.println("SE CONECTO A LA BD");
    }
    private void desconectar(){
        System.out.println("SE DESCONECTO A LA BD");
    }
    
   
  
    
}
