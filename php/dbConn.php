<?php
	$host = 'localhost';
	$username = 'selab';
	$password = 'selab';
	$database = 'smartdoor';

	$conn = mysqli_connect($host, $username, $password, $database);
	
	if($conn->connect_error){
		die("Connection failed : ". $conn->connect_error);
	}
?>