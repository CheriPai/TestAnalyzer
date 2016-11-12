function analyze() {
    var repoURL = $("#repoURL").val();
    $.ajax({
        url: "/analyze",
        data: {"URL": $("#repoURL").val()}, 
        success: function(result){
            alert(result);
    }});
}
