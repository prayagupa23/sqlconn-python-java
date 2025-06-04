import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

class demo{
    public static void main(String args[]){
        String url = "jdbc:mysql://localhost:3306/experiment3";
        String user= "root";
        String password= "Prayag@2308";
        String query = "INSERT INTO student(s_id,name,age,email) VALUES (3,'Pra',22,'prmd@mail')";
        
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection c= DriverManager.getConnection(url,user,password);
            Statement s= c.createStatement();
            int count= s.executeUpdate(query);
            System.out.println("Number of rows affected: "+count);
            s.close();
            c.close();
        }
        catch(ClassNotFoundException e){
            System.out.println("Driver not found");
        }
        catch(SQLException e){
            System.out.println("SQL Exception Found");
        }
    }
}