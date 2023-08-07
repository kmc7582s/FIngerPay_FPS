<!DOCTYPE html>
<html lang = "ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="img/icon.png" rel="shortcut icon" type="image/x-icon">
        <title>회원가입 - Finger Pay</title>
        <link href="css\register.css" rel="stylesheet">
        <link href="css\index.css" rel="stylesheet">
        <link href="css\header.css" rel="stylesheet">
        <link href="css\footer.css" rel="stylesheet">
        
        <script>
        // 서밋 버튼 이미지 클릭시
        function submitForm(){
 
            // 입력값 중에 비어있으면 안되는 것들이 있음.
 
            // id칸이 비어 있는가?
            if(!document.register_form.id.value){
                alert("아이디를 입력하세요.");
                //커서(포커스)를 아이디 인풋요소로 이동
                document.register_form.id.focus();
                //아래의 submit()을 하면 안되므로...
                return;
            }
            // 비밀번호 비어 있는가?
            if(!document.register_form.pw.value){
                alert("비밀번호를 입력하세요.");
                document.register_form.pw.focus();
                return;
            }
             // 비밀번호 확인 비어 있는가?
             if(!document.register_form.pw_confirm.value){
                alert("비밀번호 확인을 입력하세요.");
                document.register_form.pw_confirm.focus();
                return;
            }
            
            // 비밀번호와 비밀번호 확인 칸의 입력값이 같은지 비교
            if(document.register_form.pw.value != document.register_form.pw_confirm.value){
                alert("비밀번호가 일치하지 않습니다.\n다시 입력해 주세요.");
                document.register_form.pw.focus();
                // 커서가 이동하고 그곳에 써있는 글씨가 선택되어 있음.
                document.register_form.pw.select();
                return;
            } 
            // 이름 비어 있는가?
             if(!document.register_form.name.value){
                alert("이름을 입력하세요.");
                document.register_form.name.focus();
                return;
            }
            
            if(!document.register_form.email1.value){
                alert("이메일을 입력하세요.");
                document.register_form.email1.focus();
                return;
            }
            if(!document.register_form.email2.value){
                alert("이메일주소를 입력하세요.");
                document.register_form.email2.focus();
                return;
            }
            if(!document.register_form.age.value){
                alert("나이를 입력하세요.");
                document.register_form.age.focus();
                return;
            }
 
            // form요소를 직접 submit하는 메소드
            document.register_form.submit(); //겟 엘리먼트 안하고 폼, 인풋을 name속성이 document 배열로 찾을 수 있음.
        }// 리셋
        // function resetForm(){
        //     document.register_form.id.value="";
        //     document.register_form.pw.value="";
        //     document.register_form.pw_confirm.value="";
        //     document.register_form.name.value="";
        //     document.register_form.email1.value="";
        //     document.register_form.email2.value="";
        //     document.register_form.age.value="";
 
        //     // 첫번째 입력 요소로 이동
        //     document.register_form.id.focus();
        // }

        // 아이디 중복 확인 버튼 클릭
        function checkId(){
            // 사용자가 입력한 id값 얻어오기
            var userid=document.register_form.id.value;

            window.open("./login/check_id.php?id="+userid,"아이디체크","width=300, height=100, left=200, top=100");

        }
 
    </script>
    </head>

    <body>
        <header><?php include "./main/header.php"?></header>
        <section><?php include "./login/register_form.php"?></section>
        <footer><?php include "./main/footer.php"?></footer>
    </body>
</html>