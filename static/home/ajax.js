$(document).ready(function() {
  $(window).keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  });
});


$(function() {

    $('#searchStudent').keyup(function() {

        $.ajax({
            type: "POST",
            url: "search",
            data: {
                'search_text' : $('#searchStudent').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{   
    let lis = document.getElementById("mainlist");
    // console.log(sres.childNodes.length    )
        lis.style.display = "none";

    $('#search_results').html(data)
}