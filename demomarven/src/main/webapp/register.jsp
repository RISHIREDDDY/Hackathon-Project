<%@ page import="java.sql.*" %>
<%@ page import="DBConnection" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration Result</title>
</head>
<body>
<%
    String name = request.getParameter("name");
    String email = request.getParameter("email");

    Connection conn = null;
    PreparedStatement pstmt = null;

    try {
        conn = DBConnection.getConnection();
        String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, name);
        pstmt.setString(2, email);
        int rowsAffected = pstmt.executeUpdate();

        if (rowsAffected > 0) {
            out.println("<h2>Registration Successful!</h2>");
            out.println("<p>Name: " + name + "</p>");
            out.println("<p>Email: " + email + "</p>");
        } else {
            out.println("<h2>Registration Failed!</h2>");
        }
    } catch (SQLException e) {
        e.printStackTrace();
        out.println("<h2>Error: " + e.getMessage() + "</h2>");
    } finally {
        if (pstmt != null) try { pstmt.close(); } catch (SQLException ignored) {}
        if (conn != null) try { conn.close(); } catch (SQLException ignored) {}
    }
%>
</body>
</html>
