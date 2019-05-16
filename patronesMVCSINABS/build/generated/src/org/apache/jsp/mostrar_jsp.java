package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class mostrar_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <title>JSP Page</title>\n");
      out.write("    </head>\n");
      out.write("    <body>\n");
      out.write("        ");
 
        
          String nom= (String) request.getAttribute("nombre");
        
      out.write("\n");
      out.write("        <h1>USUARIO: ");
 out.print(nom);
      out.write("</h1>\n");
      out.write("        <center>\n");
      out.write("        <form name=\"form2\" action=\"calcularPrecServlet\" method=\"POST\" >\n");
      out.write("            <marquee> LOGIN</marquee>\n");
      out.write("            <label>TIPO DE VEHICULO :</label><BR>\n");
      out.write("            <label>AUTO :</label><input type=\"radio\" checked=\"checked\" name=\"movil\"  id=\"auto\"  value=\"AUTO\"><tr>\n");
      out.write("            <label>MOTOCICLETA :</label><input type=\"radio\" checked=\"checked\" name=\"movil\"  id=\"moto\"  value=\"MOTOCICLETA\"><BR>\n");
      out.write("            <label>CANTIDAD :</label><input type=\"text\" placeholder=\"INGRESA CANTIDAD\" id=\"pass\" name=\"cant\"><br><BR>\n");
      out.write("            <input type=\"submit\" id=\"btn\" value=\"ENVIAR\">\n");
      out.write("        </form>\n");
      out.write("      </center> \n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
