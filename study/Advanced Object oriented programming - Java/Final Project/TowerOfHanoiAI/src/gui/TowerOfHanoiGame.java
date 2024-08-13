package gui;

import db.DBHelper;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import logic.GameLogic;

public class TowerOfHanoiGame extends Application {
    private DBHelper dbHelper;

    @Override
    public void start(Stage primaryStage) {
        dbHelper = new DBHelper();
        
        primaryStage.setTitle("Tower of Hanoi Game");
        
        VBox loginBox = new VBox();
        TextField usernameField = new TextField();
        usernameField.setPromptText("Username");
        PasswordField passwordField = new PasswordField();
        passwordField.setPromptText("Password");
        Button loginButton = new Button("Login");
        Button registerButton = new Button("Register");
        Label messageLabel = new Label();
        
        loginBox.getChildren().addAll(new Label("Username:"), usernameField, new Label("Password:"), passwordField, loginButton, registerButton, messageLabel);
        
        loginButton.setOnAction(e -> {
            String username = usernameField.getText();
            String password = passwordField.getText();
            if (dbHelper.checkUserCredential(username, password)) {
                messageLabel.setText("Login successful!");
                showGameScreen(primaryStage);
            } else {
                messageLabel.setText("Login failed, incorrect username or password!");
            }
        });
        
        registerButton.setOnAction(e -> {
            String username = usernameField.getText();
            String password = passwordField.getText();
            if (dbHelper.createNewUser(username, password)) {
                messageLabel.setText("Registration successful!");
            } else {
                messageLabel.setText("Registration failed!");
            }
        });
        
        Scene loginScene = new Scene(loginBox, 300, 200);
        primaryStage.setScene(loginScene);
        primaryStage.show();
    }

    private void showGameScreen(Stage primaryStage) {
        VBox gameBox = new VBox();
        Label gameLabel = new Label("Welcome to the Tower of Hanoi Game!");
        Button startButton = new Button("Start Game");
        
        startButton.setOnAction(e -> {
            GameLogic gameLogic = new GameLogic();
            gameLogic.startGame();
        });
        
        gameBox.getChildren().addAll(gameLabel, startButton);
        
        Scene gameScene = new Scene(gameBox, 400, 300);
        primaryStage.setScene(gameScene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
