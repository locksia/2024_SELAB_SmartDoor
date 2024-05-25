<?php
    include("dbConn.php");

    // SQL 쿼리 작성 (최근 20개의 레코드를 불러옴)
    $sql = "SELECT id, recordedVideo, recordedTime FROM raspi_recordedvideos ORDER BY recordedTime DESC LIMIT 20";
    $result = $conn->query($sql);

    $videos = [];

    if ($result->num_rows > 0) {
        // 결과에서 데이터 가져오기
        while ($row = $result->fetch_assoc()) {
            $videos[] = $row;
        }
    } else {
        echo "No videos found.";
        exit;
    }

    $conn->close();
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>녹화된 영상</title>
    </head>
    <body>
        <h1>녹화된 영상</h1>
        <h3>사람이 감지되었거나, 문이 강제로 개방되었을 때의 녹화된 상황입니다.</h3>
        <?php foreach ($videos as $video): ?>
            <div>
                <p>녹화된 시간: <?php echo htmlspecialchars($video['recordedTime']); ?></p>
                <video width="1600" height="900" controls>
                    <source src="data:video/mp4;base64,<?php echo base64_encode($video['recordedVideo']); ?>" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            <hr>
        <?php endforeach; ?>
    </body>
</html>