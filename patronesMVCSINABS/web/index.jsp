<%-- 
    Document   : index
    Created on : 15/05/2019, 05:51:02 PM
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
        <h1>REGISTRO USUARIO</h1>
    <center>
        <form name="form1" action="controlUsu" method="POST" >
            <marquee> LOGIN</marquee>
            <input type="text" placeholder="INGRESE USER" id="user" name="user"><br><br>
            <input type="password" placeholder="INGRESE PASSWORD" id="pass" name="pass"><br><BR>
            <input type="submit" id="btn" value="ENTRAR">
        </form>
      </center>  
        
    </body>
</html>
