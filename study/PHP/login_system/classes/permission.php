<?php
class UserRole {
    private $userId;
    private $roleId;
    
    public function __construct($userId, $roleId) {
        $this->userId = $userId;
        $this->roleId = $roleId;
    }
    
    public function getUserId() {
        return $this->userId;
    }
    
    public function getRoleId() {
        return $this->roleId;
    }
}
?>
