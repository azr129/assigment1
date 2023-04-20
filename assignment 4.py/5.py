<?php
$index = $_GET['index'];
    $conn = new mysqli('localhost','root','','app');
$data = array();
$sql = "SELECT * FROM members":
$query = $conn->query($sql);
while($row = $query->fetch_assoc()){
      $data[]= $row;
}

$data= json_encode($data);
$data_array = json_decode($data);

$row=$data_array[$index];

$data= json_encode($data, JSON_PRETTY_PRINT);
$data = "delete from members where id=$row->id";
        $query = $conn->query($sql);
    

header('location: index.php');
unset($data[$index]);
?>