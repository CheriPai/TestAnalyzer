var data = {};
var average = [0.2708, 0.3376, 0.2896];
var ctx = $("#ctx");
var tmp = new Chart(ctx, {type: "horizontalBar"});


function analyze() {
    var repoURL = $("#repoURL").val();
    $.ajax({
        url: "/analyze",
        data: {"URL": $("#repoURL").val()}, 
        success: function(result){
            data = result;
            populateCtx();
    }});
}

function populateCtx() {
    var ratios = [data["test_lines"] / data["code_lines"], data["test_classes"] / data["code_classes"], data["test_functions"] / data["code_functions"]];
    var bar = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: ["Lines", "Classes", "Functions"],
            datasets: [
                {
                    label: "Your Project",
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    data: ratios,
                    borderWidth: 1
                },
                {
                    label: "GitHub Average",
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    data: average,
                    borderWidth: 1
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}
