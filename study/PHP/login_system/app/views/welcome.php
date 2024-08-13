<?php
session_start();

if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    echo "Welcome to our site!<br>";
    echo "You have successfully registered and logged in.";
} else {
    header("location: ../login.html");
    exit;
}
?>
