<?php
    function random_str(
        $length = 20,
        $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ) {
        $account= '';
        $max = mb_strlen($chars) - 1;
        for ($i = 0; $i < $length; $i++)
        {
            $rand_index = random_int(0, $max);
            $account .= $chars[$rand_index];
        }
        return $account;
    }
 
    $account = random_str();

   
    // session_start();
    // $MyAccount = "";
    // $MyAsset = "";
    // if( isset($_SESSION['MyAccount'])) $MyAccount = $_SESSION['MyAcccount'];
    // if( isset($_SESSION['MyAsset'])) $MyAsset = $_SESSION['MyAsset'];
?>

<!DOCTYPE html>
<html lang = "ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="img/icon.png" rel="shortcut icon" type="image/x-icon">
        <title>계좌 - Finger Pay</title>

        <link href="css\index.css" rel="stylesheet">
        <link href="css\header.css" rel="stylesheet">
        <link href="css\account.css" rel="stylesheet">
        <link href="css\footer.css" rel="stylesheet">
    </head>
    <body>
        <header><?php include "./main/header.php"?></header>
        <?php 
        include "./login/dbconn.php";

        $sql = "SELECT * FROM users WHERE id='$userid'";
        $result = mysqli_query($conn, $sql);

        $row=mysqli_fetch_array($result, MYSQLI_ASSOC);
        $MyAccount=$row['account'];
        $MyAsset=$row['coin'];
        mysqli_close($conn);
        ?>

        <section>
        <div id="account-wrapper">
            <div id="account-box">
        <?php if(!$MyAccount){  ?>
            <h2>계좌 생성</h2>
            <div class="centered-form">
                <form id="account_Form" action="./add_account.php?id=<?=$userid?>" method="post" name="account_form">
                    <input type="text" id="account" name="account" value="<?= $account?>" readonly>
                    <input type="submit" value="등록">
                </form>
            </div>
        <?php }else{ ?>
            <h2>My Account</h2>
            <div class="centered-form">
                <form id="account_Form" name="account_form">
                    <input type="text" id="account" name="account" value="<?php echo $MyAccount?>" readonly>
                    <input type="text" id="coin" name="coin" value="<?php echo $MyAsset?>JJ" readonly>
                </form>
            </div>
        <?php }?>
            </div>
        </div>
        </section>
        <footer><?php include "./main/footer.php"?></footer>
    </body>
</html>

