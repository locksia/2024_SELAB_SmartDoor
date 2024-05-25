<?php
    include("dbConn.php");

    // SQL 쿼리 작성 (최근 20개의 레코드를 불러옴)
    $sql = "SELECT id, recordedVideo, recordedTime FROM raspi_recordedvideos ORDER BY recordedTime DESC LIMIT 20";
    $result = $conn->query($sql);

    
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>EntryTime JSON</title>
    </head>
    <body>
        <h1>EntryTime JSON</h1>
    </body>
</html>