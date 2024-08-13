<?php
class User {
    private $username;
    private $password;
    private $conn;

    public function __construct($username, $password, $conn) {
        $this->username = $username;
        $this->password = $password;
        $this->conn = $conn;
    }

    // Method to perform user login
    public function login() {
        // Query to check if user exists with provided username and password
        $sql = "SELECT * FROM users WHERE username = ? AND password = ?";
        $stmt = $this->conn->prepare($sql);
        $stmt->bind_param("ss", $this->username, $this->password);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows == 1) {
            // User exists with provided credentials
            return true;
        } else {
            // User does not exist with provided credentials
            return false;
        }
    }
}
?>
