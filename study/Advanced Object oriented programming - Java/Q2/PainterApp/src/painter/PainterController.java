package painter;

import colorchooser.ColorChooserController;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.ColorPicker;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.IOException;

public class PainterController {
    @FXML
    private Canvas canvas;
    @FXML
    private ColorPicker colorPicker;

    private Color brushColor = Color.BLACK;

    public void initialize() {
        GraphicsContext gc = canvas.getGraphicsContext2D();
        gc.setStroke(brushColor);
        gc.setLineWidth(5);

        canvas.addEventHandler(MouseEvent.MOUSE_DRAGGED, event -> {
            gc.lineTo(event.getX(), event.getY());
            gc.stroke();
        });

        canvas.addEventHandler(MouseEvent.MOUSE_PRESSED, event -> {
            gc.beginPath();
            gc.moveTo(event.getX(), event.getY());
            gc.stroke();
        });

        colorPicker.setOnAction(event -> {
            brushColor = colorPicker.getValue();
            gc.setStroke(brushColor);
        });

        openColorChooser();
    }

    private void openColorChooser() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/colorchooser/ColorChooser.fxml"));
            Pane root = loader.load();

            ColorChooserController controller = loader.getController();
            controller.initialize();

            Stage stage = new Stage();
            stage.setTitle("Color Chooser");
            stage.setScene(new Scene(root));
            stage.show();

            controller.colorProperty().addListener((obs, oldColor, newColor) -> {
                brushColor = newColor;
                gc.setStroke(brushColor);
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
