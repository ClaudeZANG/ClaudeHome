<?php
class Role {
    private $id;
    private $name;

    public function __construct($id, $name) {
        $this->id = $id;
        $this->name = $name;
    }

    // Method to get role ID
    public function getId() {
        return $this->id;
    }

    // Method to get role name
    public function getName() {
        return $this->name;
    }
}
?>
