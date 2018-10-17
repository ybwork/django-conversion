$('#currency-rate').on('submit', function(e) {
    e.preventDefault();

    var form = $(this)
    var action = form.attr('action')
    var method = form.attr('method')
    var data = form.serialize()

    $.ajax({
        url: action,
        type: method,
        data: data,


        success: function(data) {
            console.log(data)
            // var response = $.parseJSON(data);
        },
        error: function(e) {
            console.log(e)
            // var errors = e.responseJSON;
        }
    });
});