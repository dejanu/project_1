<?php
$name = htmlspecialchars($_GET['name'] ?? 'World');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PHP App</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 80px auto; text-align: center; }
        input { padding: 8px; font-size: 1rem; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 8px 16px; font-size: 1rem; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer; }
        h1 { color: #4f46e5; }
    </style>
</head>
<body>
    <h1>Hello, <?= $name ?>!</h1>
    <form method="GET">
        <input type="text" name="name" placeholder="Enter your name" />
        <button type="submit">Greet</button>
    </form>
    <p style="color:#888; margin-top:40px;">PHP version: <?= phpversion() ?></p>
</body>
</html>
