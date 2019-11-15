$(document).change(function() {
    var optionSelected = $('#select').find("option:selected");
    var valueSelected  = optionSelected.val();

    var PSelected = $('#selectP').find("option:selected");
    var valuePSelected  = PSelected.val();


    $('#searchStudent').val('');
            $.ajax({
                type: "POST",
                url: "branchlistshow",
                data: {
                    'val': valueSelected,
                    'place':valuePSelected,
                    'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                },
                success:searchSuccess,
                dataType: 'html'
            });
    });

function searchSuccess(data)
{
   var lis = document.getElementById("mainlist");
        lis.style.display = "none";
    $('#branch_results').html(data)
}