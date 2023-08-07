<?php
    //로그인을 하면 session에 정보를 저장하고 각 페이지들에서 모두 사용하고자 함.
    //로그인에 따라 화면구성이 다르기에 세션에 저장되어 있는 회원정보 중 id, name, level 값 읽어오기
    session_start(); //세션을 저장하든 읽어오든 사용하고자 하면 이 함수로 시작
    
    $userid = "";
    $username = "";

    if( isset($_SESSION['userid'])) $userid = $_SESSION['userid'];
    if( isset($_SESSION['username'])) $username = $_SESSION['username'];
    
?>
<div class="header">
	<h1><a href="index.php"><img src="img\logo.png" alt="logo"></a></h1></li>
	<div class="menu">
		<ul>
			<li><a href="introduce.php">소개</a></li>
			<?php if(!$userid){?>
			<li><a href="" onclick="alert('로그인 후 사용 가능한 서비스입니다.')">계좌</a></li>
			<?php }else{?>
			<li><a href="account.php">계좌</a></li>
			<?php } ?>
		</ul>
	</div>
	<div class="login">
		<?php if(!$userid){  ?>
			<div class="nl">
				<li>
					<a href="signin.php">로그인</a> / <a href="signup.php">회원가입</a>
				</li>
			</div>
        <?php }else{ ?>
			<div class="login-success">
            	<li><a href="#"><?php echo $username?></a></li>
            	<li> | </li>
            	<li><a href="login\logout.php">로그아웃</a></li>
			</div>
        <?php }?>
	</div>
</div>