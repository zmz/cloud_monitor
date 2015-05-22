
function draw(title, legend, xAxis, yAxis){

    var myChart = echarts.init(document.getElementById('graph'));

    option = {
        title : {
            text: title,
            subtext: ''
        },
        tooltip : {
            trigger: 'axis'
        },
        legend: {
              data:legend
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                boundaryGap : false,
                data: xAxis
            }
        ],
        yAxis : [
            {
                type : 'value'
//                axisLabel : {
//                    formatter: '{value} /s'
//                }
            }
        ],
        series : [
            {
                name:'IO/s ',
                type:'line',
                data:yAxis,
                smooth:true,
                markLine : {
                    data : [
                        {type : 'average', name: 'Average'}
                    ]
                }
            }
        ]
    };

    myChart.setOption(option);
}

