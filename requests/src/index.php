<?php
if(isset($_GET['view_source'])){
    die(highlight_file(__FILE__));
}
if($_SERVER['REQUEST_METHOD'] === "POST"){
    $url = $_POST['url'];
   
    if(preg_match("/index|php|passwd|shadow/i", $url)){
        die("No Hack ^_^");
    }

    system(escapeshellcmd('curl '. $url));
}
?>
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title> R E Q U E S T </title>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <section class="wrapper">
        <div class="content">
        <header>
            <h5>SIMPLE IS BEST</h5>
        </header>
        <section>
            <form method="POST" class="form-url">
            <div class="input-group">
                <label for="url">URL</label>
                <input type="text" placeholder="https://www.naver.com" class="url" name="url" required>
            </div>
            <div class="input-group"><button type="submit">SEND!</button></div><br>
            <br>
            <!--<a href="?view_source">View Source</a>-->
            </form>
        </section>
        </div>
        </section>
    </body>
</html>