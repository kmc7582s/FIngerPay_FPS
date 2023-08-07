<div class="register-wrapper">
    <div class="register-box">
        <h2>회원가입</h2>
            <form action="login/register.php" method="post" name="register_form" id="register-form">
                <input type="text" name="id" placeholder="아이디(20자 이하)">
                <div id="checkid"><button type="button" onclick="checkId()">중복 확인</button></div>
 
                <input type="password" name="pw" placeholder="비밀번호">
                
                <input type="password" name="pw_confirm" placeholder="비밀번호 확인">
                
                <input type="text" name="name" placeholder="이름">
                
                <div id="email"><input type="text" name="email1" placeholder="이메일">@<input type="text" name="email2" placeholder="이메일 주소"></div>
                
                <input type="text" name="age" placeholder="나이">

                <button type="button" onclick="submitForm()">Register</button>
                <!-- <button type="button" onclick="resetForm()">Reset</button> -->
            </form>
    </div>
</div>