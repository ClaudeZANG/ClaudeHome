module EnhancedTipCalculator {
    requires javafx.controls;
    requires javafx.fxml;

    opens tipcalculator to javafx.fxml;
    exports tipcalculator;
}
