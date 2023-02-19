$(document).ready(function(){
    $('#btn_add_event').on('click', function(e){
        let event_name = $('#event_name').val();
        $.ajax({
            url: api_base_url+"/api/event",
            type: 'POST',
            contentType: "application/json",
            data: JSON.stringify({
                "event_name": event_name
            }),
            success: function(response){
                alert("Success add new event")
                location.reload()
            },
            error: function (jqXHR, textStatus, errorThrown){
                alert("Error add new event")
            }
        })
        e.preventDefault();
    })
});