/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package MVC;

import Singleton.SingletonConexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;




/**
 *
 * @author Edward
 */
public class validarUsu {
    PreparedStatement p;
   ResultSet  rs = null;
  
   String result;
   
   public String  getUser(String user,String pass)
    {

         try {
              Connection c=SingletonConexion.get_Ins().get_conexion();
             p = c.prepareStatement("select user from usuario where user='"+user+"'and password='"+pass+"';");       
            rs = p.executeQuery();        
            if(rs.next()){
             result=rs.getString(1);
             
            }           
            p.close();
            rs.close();
           
        } catch (SQLException e) {
            result="error";
        }     
    return result;
    }
  
    
}
