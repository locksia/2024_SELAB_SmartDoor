<?php
$server = "192.168.0.41";
$port = 8000;
$url = "/stream.mjpg";
set_time_limit(0); 
$fp = fsockopen($server, $port, $errno, $errstr, 30);
if (!$fp) {
        echo "$errstr ($errno)<br>\n";
} else {
        $urlstring = "GET ".$url." HTTP/1.1\r\n\r\n";
        fputs ($fp, $urlstring);
        while ($str = trim(fgets($fp, 4096)))
        header($str);
        fpassthru($fp);
        fclose($fp);
}
?>