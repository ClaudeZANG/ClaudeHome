module TowerOfHanoiAI {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens gui to javafx.graphics, javafx.fxml;
    opens db to javafx.base;
}
