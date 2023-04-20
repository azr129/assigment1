<script src="jquery-3.4.1.js"></script>

    <script>
    $(document).ready(function(){
    $('#getUser').on('click',fucntion(){
        $.ajax({
            type:'POST'
            url:'getData.php',
            dataType: "json",
            data: {
                "username": $(#username").val(),
                "password": $("password").val()
            },
            sucess:function(data){
                if(data.status == 'ok'){
                    alert("log_in_sucessful");
                    window.location.href="index.php"
                }else{ alerts("wrong_username_or_password");
                } }});});
    $("#username").blur(function() {
        $.ajax({
            type: 'POST',
            url: 'getData.php',
            dataType: "json",
            data:{
                "username": $("username").val()
            },
            success: function(data){
                if(data.status == 'ok'){
                }else{
                    alert("invalid_username");
                } }});});});
</script>

