var myChart = echarts.init(document.getElementById('main'));

option = {
    title : {
        text: 'Lenovo Monitor Disc',
        subtext: ''
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:{{legend_title | safe}}
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : {{ x_axis | safe }}
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel : {
                formatter: '{value} /s'
            }
        }
    ],
    series : [
        {
            name:'IO/s ',
            type:'line',
            data:{{y_axis}},
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