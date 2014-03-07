<?php

	include_once('setting.php');
	include_once('dblib.php');
	include_once('dbshortcuts.php');



	extract($_REQUEST);
	$tableName="regusers"
	$fieldsArr = array('email'=>$email, 'password'=>$password);
	$checkExists = FALSE;
	$print = TRUE;
	$checkAdded = FALSE;
	$updateBool = FALSE;
	$addNewFields = TRUE;
	rollAdd($tableName, $fieldsArr, $checkExists, $print ,$checkAdded, $updateBool, $addNewFields);


	echo('added');

?>