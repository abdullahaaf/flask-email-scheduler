$(document).ready(function(){
    populateSelectEvent()
});

function populateSelectEvent() {
    $.ajax({
        url: api_base_url+"/api/events",
        type: 'GET',
        success: function (data) {
            // Remove existing options from the select element
            $('#event_id').empty();
            // Loop through the data and add an option for each item
            $.each(data, function (index, item) {
                $('#event_id').append($('<option>', {
                    value: item.event_id,
                    text: item.event_name
                }));
            });
        }
    });
}