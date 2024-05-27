<?php
include("dbConn.php");

// 선택된 월 가져오기
$selectedMonth = isset($_GET['month']) ? $_GET['month'] : date('m');

// 총 녹화된 영상의 개수 가져오기
$sqlTotalCount = "SELECT COUNT(*) as totalCount FROM raspi_recordedvideos";
$totalCountResult = $conn->query($sqlTotalCount);
$totalCount = $totalCountResult->fetch_assoc()['totalCount'];

// 각 월의 녹화된 영상의 개수 가져오기
$monthlyCounts = [];
for ($m=1; $m<=12; $m++) {
    $month = str_pad($m, 2, '0', STR_PAD_LEFT);
    $sqlMonthCount = "SELECT COUNT(*) as monthCount FROM raspi_recordedvideos 
                      WHERE DATE_FORMAT(recordedTime, '%m') = '$month'";
    $monthCountResult = $conn->query($sqlMonthCount);
    $monthlyCounts[$month] = $monthCountResult->fetch_assoc()['monthCount'];
}

// 선택된 월의 녹화된 영상의 개수 가져오기
$selectedMonthCount = $monthlyCounts[$selectedMonth];

// SQL 쿼리 작성 (선택된 월의 레코드를 불러옴)
$sql = "SELECT id, recordedVideo, recordedTime FROM raspi_recordedvideos 
        WHERE DATE_FORMAT(recordedTime, '%m') = '$selectedMonth' 
        ORDER BY recordedTime DESC LIMIT 20";
$result = $conn->query($sql);

$videos = [];

if ($result->num_rows > 0) {
    // 결과에서 데이터 가져오기
    while ($row = $result->fetch_assoc()) {
        $videos[] = $row;
    }
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

    <p>총 녹화된 영상: <?php echo $totalCount; ?> 개</p>
    <p>선택된 월의 녹화된 영상: <?php echo $selectedMonthCount; ?> 개</p>
    
    <form method="GET" action="">
        <label for="month">월 선택:</label>
        <select name="month" id="month">
            <?php 
            for ($m=1; $m<=12; $m++) {
                $month = str_pad($m, 2, '0', STR_PAD_LEFT);
                $selected = ($month == $selectedMonth) ? 'selected' : '';
                $count = isset($monthlyCounts[$month]) ? $monthlyCounts[$month] : 0;
                echo "<option value='$month' $selected>$month ($count)</option>";
            }
            ?>
        </select>
        <button type="submit">조회</button>
    </form>

    <?php if (empty($videos)): ?>
        <p>해당 월에 녹화된 영상이 없습니다.</p>
    <?php else: ?>
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
    <?php endif; ?>
</body>
</html>