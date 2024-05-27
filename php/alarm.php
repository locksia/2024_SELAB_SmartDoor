<?php
// 데이터베이스 연결 설정
include("dbConn.php");

// 쿼리 실행 (entryTime 필드의 데이터 형식이 YYYY.MM.DD - HH:MM:SS 인 것으로 가정)
$sql = "SELECT * FROM raspi_alarm ORDER BY id DESC";
$result = mysqli_query($conn, $sql);

// 결과를 배열로 변환
$data = array();
while ($row = mysqli_fetch_assoc($result)) {
    $data[] = $row;
}

// JSON으로 변환하여 출력
echo json_encode($data);
?>