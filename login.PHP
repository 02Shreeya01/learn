<?php 

require_once = "config.php";
require_once = "secssion.php";

$error = ' ';
if ($_SERVER["REQUEST_METHOD"] == "Post" && isset($_POST['submit'])) {
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);

    //validate if email is empty 
    if (empty($email)) {
        $error = '<p class = "error">Please enter email.</p>';
    } 

    //validate if Password is empty
    if (empty($password)) {
        $error = '<p class = "error">Please enter Password.</p>'; 
    } 

    if(empty($error)) {
        if ($query = $db->prepare ("SELECT * FROM user WHERE email = ?"")) {
            $query -> bind_param('s',$email);
            $query ->execute();
            $row = $query ->fetch();
            if ($row) {
                if (Password_verify($password ,$row["Password])) {
                    $_SESSION["userid"] = $row['id'];
                    $_SESSION["user"] = $row;

                    //Redirect the userto welcome page
                    header("location: Welcome myphpadmin db.");
                    exit;
                } else {
                    $error = <'p class = "error">The password is not valid.</p>';
                } else {
                    $error = <'p class = "error">No User exit with that email address.</p>';
                } 
            }  
        }  
        $query -> close() ;     
    } 
    // Close connection
    mysqli_close($db);
}
?>
<!DOCTYPE html>
<html lang = "en">
    <head>
        <meta charset = "UTF - 8">
        <title>Login </title> 
        <link rel = "stylesheet" href = "http://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    </head>
    <body>
        <div class = "container">
            <div class = "row">
                <div class = "col-md-12">
                    <h2> Login </h2>
                    <p> Please fill in your email and Password.</p>
                    <?php echo $error;?>
                    <form action ="" method = "post">
                        <div class = "form-group">
                            <label> Email Address </label> 
                            <input type = "email" name = "email" class = "form-control"required /> 
                        </div>
                        <div class = "form-group">
                            <label> Password </label> 
                            <input type = "Password" name = "Password" class = "form-control"required > 
                        </div>
                        <div class = "form-group">
                            <label> Password </label> 
                            <input type = "Submit" name = "Submit" class = "btn btn-primary" value = "Submit" > 
                        </div>
                        <p> Don't have an account? <a href = "register.php">Register here </a>.</p>
                    </form> 
                </div>
            </div>  
        </div>   
    </body>  
</html>