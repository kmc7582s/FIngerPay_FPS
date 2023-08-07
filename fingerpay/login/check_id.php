<meta charset="utf-8">

<?php

    $id= $_GET['id'];
    
    // 값을 전달하지 않을 수도 있으니
    if(!$id){
        echo "아이디를 입력하세요.";
        exit;
    }

    // 데이터베이스 접속 공통모듈 사용
    include "../login/dbconn.php";

    // 전달받은 id가 users테이블에 있는지 검사
    $sql= "SELECT * FROM users WHERE id='$id'";
    $result= mysqli_query($conn, $sql);
    $rowNum=mysqli_num_rows($result);

    // $rowNum이 0이 아니면 중복
    if($rowNum){ 
        echo "아이디가 중복 됩니다.<br>다른 아이디를 사용하세요.";
        exit;
    }else{ 
        echo "사용가능한 아이디 입니다.";
        exit;
    }

    mysqli_close($conn);

?>