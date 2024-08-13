<?php
class RolePermission {
    private $roleId;
    private $permissionId;
    
    public function __construct($roleId, $permissionId) {
        $this->roleId = $roleId;
        $this->permissionId = $permissionId;
    }
    
    public function getRoleId() {
        return $this->roleId;
    }
    
    public function getPermissionId() {
        return $this->permissionId;
    }
}
?>
