$(function() {

    $('#searchStudent').keyup(function() {
    var optionSelected = $('#select').find("option:selected");
    var valueSelected  = optionSelected.val();

    var PSelected = $('#selectP').find("option:selected");
    var valuePSelected  = PSelected.val();

        $.ajax({
            type: "POST",
            url: "searchStudent",
            data: {
                'search_text' : $('#searchStudent').val(),
                'val': valueSelected,
                'place':valuePSelected,
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