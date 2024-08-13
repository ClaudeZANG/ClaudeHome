<?php
// Include the database connection file
require_once '../model/DBConnect.php';

session_start();

$db = new DBConnect();
$conn = $db->getConnection();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve and sanitize user input
    $username = $conn->real_escape_string(trim($_POST['username']));
    $password = $conn->real_escape_string(trim($_POST['password']));
    
    // Hash the password
    $passwordHash = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement to insert user data
    $sql = "INSERT INTO users (Username, Password) VALUES (?, ?)";
    
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("ss", $username, $passwordHash);
        
        if($stmt->execute()) {
            // If you want to use PHP to redirect to the login page
            // header("Location: ../view/login.html");
            echo "Registration successful. You can now <a href='../view/login.html'>login</a>.";
        } else {
            echo "Error: " . $stmt->error;
        }
        
        $stmt->close();
    } else {
        echo "Error preparing statement: " . $conn->error;
    }

    $conn->close();
}
?>
