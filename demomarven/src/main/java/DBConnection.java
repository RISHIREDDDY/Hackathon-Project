import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnection {

    // Replace with your actual database connection details
    private static final String URL = "jdbc:mysql://localhost:3306/library";
    private static final String USER = "root";
    private static final String PASSWORD = "1234";

    private static Connection conn;

    private DBConnection() {
        // Private constructor to prevent instantiation
    }

    public static Connection getConnection() {
        if (conn == null) {
            try {
                // Register MySQL JDBC Driver
                Class.forName("com.mysql.cj.jdbc.Driver");

                // Open the connection
                conn = DriverManager.getConnection(URL, USER, PASSWORD);
                System.out.println("Database connected successfully!");

            } catch (ClassNotFoundException e) {
                System.out.println("JDBC Driver not found: " + e.getMessage());
                // Additional logging can be added here

            } catch (SQLException e) {
                System.out.println("Database connection failed: " + e.getMessage());
                // Additional logging can be added here
            }
        }
        return conn;
    }
}
