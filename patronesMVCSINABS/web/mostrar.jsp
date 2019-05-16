<%-- 
    Document   : mostrar
    Created on : 15/05/2019, 07:29:16 PM
    Author     : Edward
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <% 
        
          String nom= (String) request.getAttribute("nombre");
        %>
        <h1>USUARIO: <% out.print(nom);%></h1>
        <center>
        <form name="form2" action="calcularPrecServlet" method="POST" >
            <marquee> LOGIN</marquee>
            <label>TIPO DE VEHICULO :</label><BR>
            <label>AUTO :</label><input type="radio" checked="checked" name="movil"  id="auto"  value="auto"><br><br>
            <label>MOTOCICLETA :</label><input type="radio" checked="checked" name="movil"  id="moto"  value="moto"><BR>
          <input type="text" placeholder="INGRESA CANTIDAD" id="pass" name="cant"><br><BR>
            <input type="submit" id="btn" value="ENVIAR">
        </form>
      </center> 
    </body>
</html>
