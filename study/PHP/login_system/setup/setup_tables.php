<?php
// Include the database connection file
require_once 'db_connect.php';

// Create tables
$sql = "CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)";

// Execute SQL query
if (mysqli_query($conn, $sql)) {
    echo "Table 'users' created successfully.<br>";
} else {
    echo "Error creating table: " . mysqli_error($conn) . "<br>";
}

// You can create more tables and fill them with data here

// Close connection
mysqli_close($conn);
?>
