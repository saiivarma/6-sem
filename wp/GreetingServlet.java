import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.ServletException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.GregorianCalendar;
public class GreetingServlet extends HttpServlet
{
protected void doPost(HttpServletRequest request,HttpServletResponse response) throws ServletException,IOException
{
String name=request.getParameter("name");
String email=request.getParameter("email");
String message=null;
/*GregorianCalendar calendar=new GregorianCalendar();
if(calendar.get(Calendar.AM_PM)==Calendar.AM)
{
message="Good morning";
}
else
{
message="Good afternoon";
}
*/
response.setContentType("text/html");
PrintWriter out=response.getWriter();
out.println("<html>");
out.println("<body>");
out.println("<p>"+message+","+name+"</p>");
out.println("<p> thanks for registering your email("+email+")with us.</p>");
out.println("<p>-the projava team </p>");
out.println("</body>");
out.println("</html>");
out.close();
}
}