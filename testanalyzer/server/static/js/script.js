var data = {};
var average = [0.2708, 0.3376, 0.2896];
var ctx = $("#ctx");
var tmp = new Chart(ctx, {type: "horizontalBar"});
var ratios = [];
var weight = 1.5;


function sigmoid(x) {
    return 1 / (1 + Math.pow(Math.E, -x))
}


function analyze() {
    var repoURL = $("#repoURL").val();
    $.ajax({
        url: "/analyze",
        data: {"URL": $("#repoURL").val()}, 
        success: function(result){
            data = result;
            if (data["error"]) {
                alert(data["error"]);
            }
            else {
                populateCtx();
            }
    }});
}

function populateCtx() {
    tmp.destroy();
    ratios = [
        (data["test_lines"] / data["code_lines"]).toFixed(4),
        (data["test_classes"] / data["code_classes"]).toFixed(4),
        (data["test_functions"] / data["code_functions"]).toFixed(4)
        ];
    var bar = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: ["Lines", "Classes", "Functions"],
            datasets: [
                {
                    label: data["project_name"],
                    backgroundColor: 'rgba(54, 162, 235, 0.4)',
                    data: ratios,
                    borderWidth: 1
                },
                {
                    label: "GitHub Average",
                    backgroundColor: 'rgba(255, 99, 132, 0.4)',
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
    var score = sigmoid(weight * ((ratios[0] - average[0]) + (ratios[1] - average[1]) + (ratios[2] - average[2])));
    score = (score*100).toFixed(2);
    $("#score").html(score);
    tmp = bar;
}

