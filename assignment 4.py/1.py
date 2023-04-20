<?php
if(isset($_POST['save'])){
    $conn = new mysqli('localhost','root','app');
    $input = array(
        'id'=> $_POST['id']
        'password' => $_POST['password']
        'username' => $_POST['username']

    );  
    $data[]= $input;
    $data = json_encode($data);
    $data = json_decode($data);
    echo $data[0]->id;
      foreach ($data as $user) {
        $sql='INSERT INTO members (id, username,userpassword) VALUES ($user->id,'$user->username','$user->password')";
            echo $sql;
        $result = $conn -> query($sql);
        echo $result;
      } 
      header('location: index.php');                                          
}     
?>