<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $hostname = $_POST['hostname'];
    $username = $_POST['username'];
    $password = $_POST['password'];
    $database = $_POST['database'];

    // Attempt to establish connection to MySQL server
    $conn = mysqli_connect($hostname, $username, $password);

    // Check connection
    if ($conn === false) {
        die("Error: Could not connect to the database. " . mysqli_connect_error());
    }

    // Create database
    $sql = "CREATE DATABASE IF NOT EXISTS $database";
    if (mysqli_query($conn, $sql)) {
        echo "Database created successfully.<br>";

        // Include the database connection file
        require_once 'db_connect.php';

        // Include the setup tables file
        require_once 'setup_tables.php';
    } else {
        echo "Error creating database: " . mysqli_error($conn) . "<br>";
    }

    // Close connection
    mysqli_close($conn);
}
?>
