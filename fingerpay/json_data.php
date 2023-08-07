<?php
session_start();
$id = "";
$pw = "";
$email = "";
$name = "";
$age = "";
$account = "";
$coin = "";
	
if( isset($_SESSION['id'])) $userid = $_SESSION['id'];
if( isset($_SESSION['pw'])) $username = $_SESSION['pw'];
if( isset($_SESSION['name'])) $username = $_SESSION['name'];
if( isset($_SESSION['email'])) $username = $_SESSION['email'];
if( isset($_SESSION['age'])) $username = $_SESSION['age'];
if( isset($_SESSION['account'])) $username = $_SESSION['account'];
if( isset($_SESSION['coin'])) $username = $_SESSION['coin'];

echo json_encode($_SESSION);
?>