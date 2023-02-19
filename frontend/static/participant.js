$(document).ready(function(){
    $('#btn_add_participant').on('click', function(e){
        let event_id = $('#event_id').val()
        let full_name = $('#full_name').val()
        let email = $('#email').val()

        $.ajax({
            url: "http://192.168.71.145:5000/api/participant",
            type: 'POST',
            contentType: "application/json",
            data: JSON.stringify({
                "event_id": event_id,
                "full_name": full_name,
                "email" : email
            }),
            success: function (response) {
                alert("Success add participant")
                location.reload()
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert("Error add participant")
            }
        })
        e.preventDefault()
    });
});