<?php
if(!empty($_POST['username'])){
   $data = array()

   $dbHost  =  'localhost';
   $dbUsername = 'root';
   $dbPassword = '';
   $dbName = 'app';

   $db= new mysqli($dbHost,$dbUsername, $dbPassword, $dbName);
   if($sb->connect_error){
      die("Unable to connect database:" . $db->connect_error);
    }

    $query= $db->query("select * FROM members WHERE username = {$_POST['username']} and password = {$_POST['password']}");

    if($query->num_rows > 0){
        $userData = $query->fetch_assoc();
        $data['status']= 'ok';
        $data['result']= $userData;
    }else{
        $data['status']= 'err';
        $data['result']= '';
    }


    echo json_encode($data);
}
?>
                                                                                                                  