package model;

import java.io.Serializable;

public class SaveGame implements Serializable {
    private static final long serialVersionUID = 1L;
    private String username;
    private int[][] gameState;
    private long elapsedTime;

    public SaveGame(String username, int[][] gameState, long elapsedTime) {
        this.username = username;
        this.gameState = gameState;
        this.elapsedTime = elapsedTime;
    }

    // Getters and setters
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public int[][] getGameState() {
        return gameState;
    }

    public void setGameState(int[][] gameState) {
        this.gameState = gameState;
    }

    public long getElapsedTime() {
        return elapsedTime;
    }

    public void setElapsedTime(long elapsedTime) {
        this.elapsedTime = elapsedTime;
    }
}
