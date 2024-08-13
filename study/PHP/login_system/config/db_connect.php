<?php
$servername = "localhost";
$username = "ss"; // Replace with your MySQL username
$password = "7147"; // Replace with your MySQL password
$database = "assignment2"; // Replace with your MySQL database name

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
