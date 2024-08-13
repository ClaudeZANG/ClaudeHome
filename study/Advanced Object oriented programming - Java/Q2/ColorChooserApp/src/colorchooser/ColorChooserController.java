package colorchooser;

import javafx.beans.binding.Bindings;
import javafx.fxml.FXML;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class ColorChooserController {
    @FXML
    private Slider redSlider;
    @FXML
    private Slider greenSlider;
    @FXML
    private Slider blueSlider;
    @FXML
    private Slider alphaSlider;
    @FXML
    private TextField redTextField;
    @FXML
    private TextField greenTextField;
    @FXML
    private TextField blueTextField;
    @FXML
    private TextField alphaTextField;
    @FXML
    private Rectangle colorRectangle;

    public void initialize() {
        redTextField.textProperty().bind(
            Bindings.format("%.0f", redSlider.valueProperty()));
        greenTextField.textProperty().bind(
            Bindings.format("%.0f", greenSlider.valueProperty()));
        blueTextField.textProperty().bind(
            Bindings.format("%.0f", blueSlider.valueProperty()));
        alphaTextField.textProperty().bind(
            Bindings.format("%.2f", alphaSlider.valueProperty()));

        colorRectangle.fillProperty().bind(
            Bindings.createObjectBinding(() -> 
                Color.rgb((int) redSlider.getValue(), 
                          (int) greenSlider.getValue(), 
                          (int) blueSlider.getValue(), 
                          alphaSlider.getValue()),
                redSlider.valueProperty(), 
                greenSlider.valueProperty(), 
                blueSlider.valueProperty(), 
                alphaSlider.valueProperty()));
    }
}
