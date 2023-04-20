<?php
    if(isset($_POST['save'])){
             
        $conn = new mysqli('localhost','root','','app');
        $input = array(
            'id'=>$_POST['id']
            'username'=> $_POST['username'],
            'password'=> $_POST['password'],

        );

        $data_array[$index]= $input;

        $data= json_encode($data_aaray);
        $data = json_decode($data);
        echo $data[0]->id;
        foreach ($data as $user) {
            
            $sql="update members set username='$user->username',password=$user->password' hwere id=$user->id";
            echo $sql
            $ersult = $conn->query($sql);
            echo $result;
        }

        header('location: index.php')
    }
?>
