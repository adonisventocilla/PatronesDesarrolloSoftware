<%-- 
    Document   : resultado
    Created on : 15/05/2019, 09:27:58 PM
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
        <% String men=(String) request.getAttribute("mensaje"); %>
        <% String tip=(String) request.getAttribute("tipo"); %>
      <% String cant=(String) request.getAttribute("cantidad"); %>
        <h1>CALCULANDO PRECIO DE <% out.print(tip.toUpperCase());%></h1><br><br>
         <p>CANTIDAD: <% out.print(cant);%></p>
        <p><% out.print(men);%></p>
    </body>
</html>
