$(document).change(function() {
    var optionSelected = $('#select').find("option:selected");
    var valueSelected  = optionSelected.val();
    var place=$('#placed').is(':checked');
            $.ajax({
                type: "POST",
                url: "branchlist",
                data: {
                    'val': valueSelected,
                    'place':place,
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