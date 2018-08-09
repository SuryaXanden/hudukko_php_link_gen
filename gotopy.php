<?php
//gotopy
if($price<=0)
{
	$api_link = "localhost/ipapi/index.php?prod=".$prod."&price=";
}
else
	$api_link = "localhost/ipapi/index.php?prod=".$prod."&price=".$price;

$py_path = "python safe\\skrape.py";


$results = (object) array('1' => shell_exec($py_path));

//output foo
echo $results->{'1'};

?>