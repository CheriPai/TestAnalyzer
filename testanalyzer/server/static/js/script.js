var data = {};

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
    var ctx = $("#ctx");
    var bar = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: ["Lines", "Classes", "Functions"],
            datasets: [{
                label: "Ratio of test over code",
                data: ratios,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderWidth: 1
            }]
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
