<?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);

    
    $id = $_GET['id'];
    include "./login/dbconn.php";

    $account1 = $_POST['account'];
    $coin = 1000;

    //중복체크
    $sql = "SELECT * FROM users WHERE account='$account1'";
    $result = mysqli_query($conn, $sql);
    $rowNum = mysqli_num_rows($result);

    if ($rowNum) {
        echo "
        <script>
            alert('죄송합니다 중복된 계좌입니다.\n 자동으로 새로고침이 진행됩니다.');
            history.back();
        </script>
        ";
    } 
    
    $sql1 = "UPDATE users SET account='$account1',coin='$coin' WHERE id='$id'";
    mysqli_query($conn, $sql1);
    mysqli_close($conn);
    
    echo "
    <script>
        location.href='alert.php';
    </script>
    ";

?>