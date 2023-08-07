<?php
    $id = $_POST['id'];
    $pw = $_POST['pw'];
    $name = $_POST['name'];
    $email1 = $_POST['email1'];
    $email2 = $_POST['email2'];
    $age = $_POST['age'];

    // 이메일
    $email = $email1 . "@" . $email2;

    // 등록일
    $regist_day = date("Y-m-d H:i");

    include "../login/dbconn.php";

    //중복된 아이디 여부 확인
    $sql = "SELECT * FROM users WHERE id='$id'";
    $result = mysqli_query($conn, $sql);
    $rowNum = mysqli_num_rows($result);

    // $rowNum 값이 0이 아니면 중복값 존재
    if($rowNum){
        echo("
            <script>
                alert('해당 아이디가 이미 존재합니다.');
                history.back();
            </script>
        ");
        exit;
    }

    //회원정보 insert
    $sql = "INSERT INTO users(id, pw, name, email, regist_day, age) VALUES('$id', '$pw', '$name', '$email', '$regist_day', '$age')";

    mysqli_query($conn,$sql);
    mysqli_close($conn);
    
    echo "
    <script>
        location.href='../index.php';
    </script>
    ";

?>