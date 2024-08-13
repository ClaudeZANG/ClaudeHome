<?php
require_once('../models/user.php');
require_once('../config/db_connect.php');

// Check if form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){
    // Check if username and password are empty
    if(empty(trim($_POST["username"])) || empty(trim($_POST["password"]))){
        header("Location: /login_system/public/login.html?error=empty");
        exit;
    } else{
        // Prepare a select statement
        $sql = "SELECT id, username, password FROM users WHERE username = ?";
        
        if($stmt = $conn->prepare($sql)){
            // Bind variables to the prepared statement as parameters
            $stmt->bind_param("s", $param_username);
            
            // Set parameters
            $param_username = trim($_POST["username"]);
            
            // Attempt to execute the prepared statement
            if($stmt->execute()){
                // Store result
                $stmt->store_result();
                
                // Check if username exists, if yes then verify password
                if($stmt->num_rows == 1){                    
                    // Bind result variables
                    $stmt->bind_result($id, $username, $hashed_password);
                    if($stmt->fetch()){
                        if(password_verify($_POST["password"], $hashed_password)){
                            // Password is correct, start a new session
                            session_start();
                            
                            // Store data in session variables
                            $_SESSION["loggedin"] = true;
                            $_SESSION["id"] = $id;
                            $_SESSION["username"] = $username;                            
                            
                            // Redirect user to welcome page
                            header("Location: /login_system/public/welcome.php");
                        } else{
                            // Display an error message if password is not valid
                            header("Location: /login_system/public/login.html?error=invalid");
                            exit;
                        }
                    }
                } else{
                    // Display an error message if username doesn't exist
                    header("Location: /login_system/public/login.html?error=invalid");
                    exit;
                }
            } else{
                header("Location: /login_system/public/login.html?error=server");
                exit;
            }

            // Close statement
            $stmt->close();
        }
    }
    
    // Close connection
    $conn->close();
}
?>
