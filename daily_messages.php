<?php
// Start php code
// Load xml file into xml_data variable
$xml_data = simplexml_load_file("config/peerlesspearls.xml") or
die("Error: Object Creation failure");
$myhashmap = array();
// Use foreach loop to display data and for sub elements access,
// We will use children() function
foreach ($xml_data->children() as $data)
{
    //display each sub element in xml file
    echo "Date : ", $data->date . "<br> ";
    echo "Display Date : ", $data->displaydate . "<br> ";
    echo "Message : ", $data->message . "<br> ";
    echo "Reference : ", $data->reference . "<br>";
    echo "Era : ", $data->era . 
    ;
    echo "------------------------------------";
    echo "<br>";
    $a =   $data->date .
    $b = $data->message .
    $myhashmap +=  [$a => $b];
}
echo  $myhashmap["01-01-25"]
?>