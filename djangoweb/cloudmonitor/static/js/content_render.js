/**
 * @author zhangxg
 */
function drawCpuGraph(graphHolder, row, data){
	var myChart = echarts.init(graphHolder);

    option = {
        title : {
            text: '',
            subtext: ''
        },
        tooltip : {
            trigger: 'axis'
        },
        legend: {
              data:['Temp']
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                boundaryGap : false,
                data: ['周一','周二','周三','周四','周五','周六','周日']
            }
        ],
        yAxis : [
            {
                type : 'value'
            }
        ],
        series : [
            {
                name:'IO/s ',
                type:'line',
                data:[1, -2, 2, 5, 3, 2, 0],
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


function drawMemeoryGraph(){
	
}

function drawDiscReadGraph() {
	
}

function drawDiscWriteGraph(){
	
}

function drawNetworkReadGraph() {
	
}

function drawNetworkWriteGraph(){
	
}

function renderTenentList(tenents) {
	var sel = document.getElementById("sel_tenent_selection");

	for (var i = 0; i < tenents.length; i++) {
		var opt = document.createElement("option");
		opt.value = tenents[i];
		opt.text = tenents[i];
		sel.add(opt);
	}
}

function renderTenentDetailTable() {
	var table = document.getElementById('table_tenent_detail');
	for (var i = 1; i < 4; i++) {
		var tr = document.createElement('tr');
		
		var td_image_id = document.createElement('td');
		td_image_id.appendChild(document.createTextNode("image" + i));
		
		var td_cpu = document.createElement('td');
		var div_cpu = document.createElement('div');
		div_cpu.setAttribute('id', i+'cpu');
		div_cpu.setAttribute('class', 'col_cpu');
		td_cpu.appendChild(div_cpu);
		
		var td_mem = document.createElement('td');
		var div_mem = document.createElement('div');
		div_mem.setAttribute('id', i+'mem');
		div_mem.setAttribute('class', 'col_mem');
		td_mem.appendChild(div_mem);
		
		var td_disk_read = document.createElement('td');
		var div_disk_read = document.createElement('div');
		div_disk_read.setAttribute('id', i+'disk_read');
		div_disk_read.setAttribute('class', 'col_disk_read');
		td_disk_read.appendChild(div_disk_read);
		
		var td_disk_write = document.createElement('td');
		var div_disk_write = document.createElement('div');
		div_disk_write.setAttribute('id', i+'disk_write');
		div_disk_write.setAttribute('class', 'col_disk_write');
		td_disk_write.appendChild(div_disk_write);
		
		var td_network_in = document.createElement('td');
		var div_network_in = document.createElement('div');
		div_network_in.setAttribute('id', i+'network_in');
		div_network_in.setAttribute('class', 'col_network_in');
		td_network_in.appendChild(div_network_in);
		
		var td_netwrok_out = document.createElement('td');
		var div_network_out = document.createElement('div');
		div_network_out.setAttribute('id', i+'network_out');
		div_network_out.setAttribute('class', 'col_network_out');
		td_netwrok_out.appendChild(div_network_out);
		
		tr.appendChild(td_image_id);
		tr.appendChild(td_cpu);
		tr.appendChild(td_mem);
		tr.appendChild(td_disk_read);
		tr.appendChild(td_disk_write);
		tr.appendChild(td_network_in);
		tr.appendChild(td_netwrok_out);

		table.appendChild(tr);
		
	}
}


function drawGraphs(){
	for (var i = 1; i < 4; i++) {
		drawCpuGraph(document.getElementById(i+'cpu'),i,null);
		drawCpuGraph(document.getElementById(i+'mem'),i,null);
		drawCpuGraph(document.getElementById(i+'disk_read'),i,null);
		drawCpuGraph(document.getElementById(i+'disk_write'),i,null);
		drawCpuGraph(document.getElementById(i+'network_in'),i,null);
		drawCpuGraph(document.getElementById(i+'network_out'),i,null);
	}
}

