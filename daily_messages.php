<!DOCTYPE html>

<html lang="en-US">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta content="Sriramchandra.org" name="author" />
	<meta content="sriramchandra.org, raja yoga, pranahuti, purpose of meditation,institute of sri ramchandra conciousness"
	 name="keywords" />
	 <meta content="Institure of sri ramchandra conciousness" name="description" />


    <link href='http://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
    <link href="assets/css/font-awesome.css" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.css" type="text/css">
    <link rel="stylesheet" href="assets/css/selectize.css" type="text/css">
    <link rel="stylesheet" href="assets/css/owl.carousel.css" type="text/css">
    <link rel="stylesheet" href="assets/css/vanillabox/vanillabox.css" type="text/css">

    <link rel="stylesheet" href="assets/css/style.css" type="text/css">
    <style>
.collapsible {
	background-color: #DCE0EF;
	color: #006;
	cursor: pointer;
	padding: 18px;
	width: 100%;
	border: none;
	text-align: left;
	outline: none;
	font-size: 15px;
	font-weight: 600;
}



.content {
    padding: 0 18px;
    display: none;
    overflow: hidden;
    background-color: #f1f1f1;

}
.newcontainer1{
	width: 80%;
	padding:10px;
	Margin:left;
}

</style>

     <title>Institute of Sri Ramchandra Consciousness --- Daily Message </title>
<script>

        function playAudio(audioEleId, startTime = 0, endTime = Number.POSITIVE_INFINITY) {
            // audioEleId: audio element's id. start time to end time in seconds
            // playAudio("babuji" , 10, 20);
            console.log('Entering')
            const audio = document.getElementById(audioEleId);
            console.log(audio.id)

            if (startTime !== undefined && startTime !== null) {
                //  Play the audio from start time to endtime in seconds
                audio.currentTime = startTime;
                audio.play();
                const intervalId = setInterval(() => {
                    if (audio.currentTime >= endTime) {
                        audio.pause();
                        clearInterval(intervalId);
                    }
                }, 100); // Check every 100ms
            } else {
                //  Play the entire audio
                audio.play();
            }
        }
    </script>

</head>

<body class="page-sub-page page-about-us">
<!-- Wrapper -->
<div class="wrapper">
<!-- Header -->
<?php include_once('includes/header.php');?>

<!-- Breadcrumb -->

    <ol class="breadcrumb">
        <li><a href="index.php">Home</a></li>
        <li class="active"> daily Messages</li>
    </ol>
</div>
<!-- end Breadcrumb -->

<!-- Page Content -->
<div id="page-content">
    <div class="container">
        <div class="row">
            <!--MAIN Content-->
            <div class="col-md-8">
                <div id="page-main">
                  <section id="Prayer">


<div class="container text-center">
<?php
    $babujixml = simplexml_load_file('xml/peerlesspearls_crossreference.xml');
    $matchesObj = $babujixml->xpath("message//reference//era_dt[contains(@from, '".date('Y-m-d',time())."')]"); // search attributes containing today's date


    $today = $_GET['date'] ?? date('d-m-y');
    // $today = date('01-01-18');

    foreach($babujixml->children() as $item)
	{
	   $date = date($item->date);

	   if ($date == $today)
	   {
		   $displaydate1= $item->date;
           $date_title= $item->date['title'];
           $date_ref =$item->date['ref'];
		   $babuji_message =$item->message;
		   $date_era1= $item->era_dt;
		   $babuji_message_reference= $item->reference;
		   $babuji_message_href= $item->message['href'];
           $kcn_title=  $item->kcn;
		   $kcn_audio = $item->kcn['audio'];
		   $kcn_text = $item->kcn['txt'];
           $kcn_partial_text = $item->kcn['partial_txt'];
           $kcn_audio_start = $item->kcn['start'];
           $kcn_audio_end = $item->kcn['end'];

           $babuji_title =$item->babuji;
           $babuji_audio = $item->babuji['audio'];
		   $babuji_text = $item->babuji['txt'];
	   }
    }

    $kcvxml = simplexml_load_file('xml/kcvmessages.xml');
    foreach($kcvxml->children() as $item)
	{
	   $date = date($item->date);

	   if ($date == $today)
	   {
		   $kcvxml =$item->message;
           $kcv_message =$item->message;
		   $kcv_message_reference= $item->reference;
		   $kcv_message_href= $item->message['href'];
	   }
    }


?>
<?php if ( isset($date_title) ){ ?>
    <div class ="centered">
        <h3><a target='_blank' href='<?php echo  $date_ref;  ?>'><?php echo  $date_title ;  ?></a>  </h3>
    </div>
<?php } ?>
<div class="newcontainer1">
    <table>
        <div class="top-left">
            <tr>
                <td width="80%">
                    <?php echo ' <h1>'.$date_era1."&nbsp;&nbsp;</h1>" ;?>
                </td>
                <td align="right">
                    <?php echo ' <h1>'.$displaydate1."</h1>"; ?>
                </td>
            </tr>
        </div>
</table>
<div class ="centered">

    <h3>Rev. Babuji Maharaj's Book Message !</h3>
    <p style="font-size:20px; color:#C00; ">
        <?php echo  $babuji_message;  ?>
	</p>
    <p>
        <a href='<?php echo  $babuji_message_href;  ?>'><?php echo  $babuji_message_reference;  ?></a>
    </p>
    <br>
</div>
<div class ="centered">

    <h3>Rev. Dr K.C. Varadachari's Book Message !</h3>
    <p style="font-size:20px; color:#C00; ">
        <?php echo  $kcv_message;  ?>
	</p>
    <p>
        <a href='<?php echo  $kcv_message_href;  ?>'><?php echo  $kcv_message_reference;  ?></a>
    </p>
    <br>
</div>
<?php if ( isset($kcn_title) ){ ?>
<div class ="centered">
    <h3>Rev. K.C.Narayana's reference to Master's Message !</h3>
     <?php if (isset($kcn_partial_text) ){ ?>
        <p>Pertinent:  <a target='_blank' href='<?php echo  $kcn_partial_text;  ?>'><?php echo  $kcn_title ."<br>" ;  ?></a>  </p>
    <?php } ?>
    <div class ="centered">
        <p>Complete:  <a target='_blank' href='<?php echo  $kcn_text;  ?>'><?php echo  $kcn_title ."<br>" ;  ?></a>  </p>
    </div>
    <p>Audio </p>
    <audio id='kcn_audio' controls autoplay>
            <source src='<?php echo  $kcn_audio;  ?>' type="audio/mpeg">
            Your browser does not support the audio element.
    </audio>
     <?php if (isset($kcn_audio_start) ){ ?>
        <button onclick="playAudio('kcn_audio',<?php echo (int)$kcn_audio_start ?>, <?php echo (int)$kcn_audio_end ?>)">Pertinent</button>
        <button onclick="playAudio('kcn_audio')">Complete</button>
    <?php } ?>

</div>
<?php } ?>
</div>
<?php if ( isset($babuji_audio) ){ ?>
<div class ="centered">
    <h3>Rev. Babuji Audio Message !</h3>
    <div class ="centered">
        <p><a target="_blank" href='<?php echo  $babuji_text;  ?>'><?php echo  $babuji_title ."<br>" ;  ?></a>  </p>
    </div>
    <audio controls autoplay>
            <source src='<?php echo  $babuji_audio;  ?>' type="audio/mpeg">
            Your browser does not support the audio element.
    </audio>

</div>
<?php } ?>

</div>


</section>
</div><!-- /#page-main -->
</div><!-- /.col-md-8 -->
</div><!-- /.row -->
</div><!-- /.container -->
</div>
<!-- end Page Content -->

<?php include_once('includes/footer.php');?>