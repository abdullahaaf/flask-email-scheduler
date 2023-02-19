$(document).ready(function(){
    $('#btn_schedule_email').on('click', function(e){
        let event_id = $('#event_id').val()
        let email_subject = $('#email_subject').val()
        let email_content =  $('#email_content').val()
        let timestamp = $('#timestamp').val().replace("T"," ")
        let schedule_data = {
            "event_id": event_id,
            "email_subject": email_subject,
            "email_content": email_content,
            "timestamp" : timestamp
        }

        $.ajax({
            url: api_base_url+"/api/save_emails",
            type: 'POST',
            contentType: "application/json",
            data: JSON.stringify(schedule_data),
            success: function (response) {
                alert("Success schedule email")
                location.reload()
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert("Error schedule")
            }
        })
        e.preventDefault()
    });
});