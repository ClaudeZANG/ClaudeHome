<?php
// Include database connection file
require_once '../model/DBConnect.php'; 

// Start session
session_start();

// 实例化数据库连接
$db = new DBConnect();
$conn = $db->getConnection();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve and sanitize user input
    $username = $conn->real_escape_string(trim($_POST['username']));
    $password = trim($_POST['password']);
    
    // Prepare the SQL statement to find the user
    $sql = "SELECT UserID, Username, Password FROM users WHERE Username = ?";
    
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("s", $username);
        
        // Execute the statement
        if($stmt->execute()) {
            // Store result
            $stmt->store_result();
            
            // Check if username exists, if yes then verify password
            if($stmt->num_rows == 1) {
                // Bind result variables
                $stmt->bind_result($userID, $username, $hashedPassword);
                if($stmt->fetch()) {
                    if(password_verify($password, $hashedPassword)) {
                        // Password is correct, so start a new session
                        $_SESSION["loggedin"] = true;
                        $_SESSION["UserID"] = $userID;
                        $_SESSION["Username"] = $username;
                        
                        // Redirect user to chat room page
                        header("Location: ../view/chatroom.php");
                        exit;
                    } else {
                        // Display an error message if password is not valid
                        echo "The password you entered was not valid.";
                    }
                }
            } else {
                // Display an error message if username doesn't exist
                echo "No account found with that username.";
            }
        } else {
            echo "Oops! Something went wrong. Please try again later.";
        }
        
        // Close statement
        $stmt->close();
    }
}

// Close connection
$conn->close();
?>
