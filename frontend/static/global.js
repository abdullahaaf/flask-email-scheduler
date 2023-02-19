$(document).ready(function(){
    populateSelectEvent()
});

function populateSelectEvent() {
    $.ajax({
        url: "http://192.168.71.145:5000/api/event",
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