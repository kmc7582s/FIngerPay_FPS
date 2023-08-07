<?php

// POST 데이터에서 이메일과 비밀번호 값 받기
$id = $_POST['id'];
$pw = $_POST['pw'];

// 데이터베이스 연결
$conn= new mysqli('localhost','kmc7582s','FPS597582@', 'kmc7582s');

// 연결 확인
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// 데이터베이스에서 아이디 일치하는 사용자 정보 조회
$sql = "SELECT * FROM users WHERE id='$id' and pw='$pw'";
$result= mysqli_query($conn,$sql);
$rowNum= mysqli_num_rows($result);

if (!$rowNum) {
    // 로그인 실패
    echo failure;
    exit;
} else {
    $row=mysqli_fetch_array($result, MYSQLI_ASSOC);
    session_start();
    $_SESSION['id']=$row['id'];
    $_SESSION['name']=$row['name'];
    $_SESSION['pw']=$row['pw'];
    $_SESSION['email']=$row['email'];
    $_SESSION['age']=$row['age'];
    $_SESSION['account']=$row['account'];
    $_SESSION['coin']=$row['coin'];

    echo success;
}

$conn->close();

?>