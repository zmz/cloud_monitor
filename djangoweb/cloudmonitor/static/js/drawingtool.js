
function draw(legend, xAxis, yAxis){

    var myChart = echarts.init(document.getElementById('graph'));

    option = {
        title : {
            text: 'Lenovo Monitor Disc',
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

//function ajaxLoading(imageid){
//
//    alert(imageid)
//
//    var xmlhttp;
//    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
//        xmlhttp = new XMLHttpRequest();
//    } else {// code for IE6, IE5
//        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
//    }
//    xmlhttp.onreadystatechange = function() {
//        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
//            document.getElementById("datail").innerHTML = xmlhttp.responseText;
//        }
//    }
//    xmlhttp.open("get", imageid + "/", false);
//    xmlhttp.send(null);
//
//}

