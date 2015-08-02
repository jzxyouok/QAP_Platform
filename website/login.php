<?php
/**
 * Created by PhpStorm.
 * User: taozhengkai
 * Date: 15/8/2
 * Time: 23:39
 */

$username = $_POST["username"];
$password = $_POST["password"];

echo "username: ".$username.", password: ".$password."<br>";

//set POST variables
$url = "http://127.0.0.1:10100/doUserAct";
$fields = array(
    'username' => urlencode($username),
    'password' => urlencode($password)
);

//url-ify the data for the POST
foreach($fields as $key => $value) {
    $fields_string .= $key.'='.$value.'&';
}
rtrim($fields_string, '&');

//open connection
$ch = curl_init();

//set the url, number of POST vars, POST data
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, count($fields));
curl_setopt($ch, CURLOPT_POSTFIELDS, $fields_string);

//execute post
$result = curl_exec($ch);

//close connection
curl_close($ch);

echo "result: ".$result."<br>";
