<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Installation</title>
</head>
<body>
    <h2>Database Configuration</h2>
    <form action="init_database.php" method="post">
        <label for="hostname">Hostname:</label>
        <input type="text" id="hostname" name="hostname" required><br><br>
        
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <label for="database">Database Name:</label>
        <input type="text" id="database" name="database" required><br><br>
        
        <button type="submit">Install</button>
    </form>
</body>
</html>
