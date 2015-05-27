/**
 * @author zhangxg
 */

function drawGraph(graphHolder, seriesLabels, xAxis, yAxis, unit) {
	var myChart = echarts.init(graphHolder);

	option = {
		title : {
			text : '',
			subtext : ''
		},
		tooltip : {
			trigger : 'axis'
		},
		legend : {
			data : seriesLabels
		},
		calculable : true,
		xAxis : [{
			type : 'category',
			boundaryGap : false,
			data : xAxis
		}],
		yAxis : [{
			type : 'value'
		}],
		series : [{
			name : unit,
			type : 'line',
			data : yAxis,
			smooth : true,
			markLine : {
				data : [{
					type : 'average',
					name : 'Average'
				}]
			}
		}]
	};

	myChart.setOption(option);
}

function drawCpuGraph(data) {
	
	for(var i = 0; i < data.length; i++) {
		var graphHolder = document.getElementById(i+"cpu");
		
		var detail = data[i].detail.cpu_util;
		var unit = detail.counter_unit;
		var timestamps = detail.timestamp;
		
		var xAxis = new Array();
		var yAxis = new Array();
		for (var j = 0; j < timestamps.length; j++){
			xAxis[j] = timestamps[j][0];
			yAxis[j] = timestamps[j][1];
		}
		drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
	}
}

function drawMemeoryGraph(data) {
	for(var i = 0; i < data.length; i++) {
		var graphHolder = document.getElementById(i+"mem");
		
		var detail = data[i].detail.memory_usage;
		var unit = detail.counter_unit;
		var timestamps = detail.timestamp;
		
		var xAxis = new Array();
		var yAxis = new Array();
		for (var j = 0; j < timestamps.length; j++){
			xAxis[j] = timestamps[j][0];
			yAxis[j] = timestamps[j][1];
		}
		drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
	}
}

function drawDiscReadGraph() {
	
}

function drawDiscWriteGraph() {

}

function drawNetworkReadGraph() {

}

function drawNetworkWriteGraph() {

}

function renderTenentList(data) {
	var sel = document.getElementById("sel_tenent_selection");	
	var json = JSON.parse(data);
	var tenents = json.tenents;
	for (var i = 0; i < tenents.length; i++) {
		var opt = document.createElement("option");
		opt.value = tenents[i];
		opt.text = tenents[i];
		sel.add(opt);
	}
}

function renderTenentDetailTable(dataStr) {
	var table = document.getElementById('table_tenent_detail');
	
	var data = JSON.parse(dataStr);
	
	for (var i = 0; i < data.length; i++) {
		var tr = document.createElement('tr');

		var td_image_id = document.createElement('td');
		td_image_id.appendChild(document.createTextNode(data[i].vm_id));

		var td_cpu = document.createElement('td');
		var div_cpu = document.createElement('div');
		div_cpu.setAttribute('id', i + 'cpu');
		div_cpu.setAttribute('class', 'col_cpu');
		td_cpu.appendChild(div_cpu);

		var td_mem = document.createElement('td');
		var div_mem = document.createElement('div');
		div_mem.setAttribute('id', i + 'mem');
		div_mem.setAttribute('class', 'col_mem');
		td_mem.appendChild(div_mem);

		var td_disk_read = document.createElement('td');
		var div_disk_read = document.createElement('div');
		div_disk_read.setAttribute('id', i + 'disk_read');
		div_disk_read.setAttribute('class', 'col_disk_read');
		td_disk_read.appendChild(div_disk_read);

		var td_disk_write = document.createElement('td');
		var div_disk_write = document.createElement('div');
		div_disk_write.setAttribute('id', i + 'disk_write');
		div_disk_write.setAttribute('class', 'col_disk_write');
		td_disk_write.appendChild(div_disk_write);

		var td_network_in = document.createElement('td');
		var div_network_in = document.createElement('div');
		div_network_in.setAttribute('id', i + 'network_in');
		div_network_in.setAttribute('class', 'col_network_in');
		td_network_in.appendChild(div_network_in);

		var td_netwrok_out = document.createElement('td');
		var div_network_out = document.createElement('div');
		div_network_out.setAttribute('id', i + 'network_out');
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
	
	//draw graphs
	drawCpuGraph(data);
	drawMemeoryGraph(data);
	
}

function drawGraphs() {
	for (var i = 1; i < 4; i++) {
		drawCpuGraph(document.getElementById(i + 'cpu'), i, null);
		drawCpuGraph(document.getElementById(i + 'mem'), i, null);
		drawCpuGraph(document.getElementById(i + 'disk_read'), i, null);
		drawCpuGraph(document.getElementById(i + 'disk_write'), i, null);
		drawCpuGraph(document.getElementById(i + 'network_in'), i, null);
		drawCpuGraph(document.getElementById(i + 'network_out'), i, null);
	}
}

function registerEventHandler(){
	var tenentSelection = document.getElementById("sel_tenent_selection");
	tenentSelection.addEventListener('change', eh_selection_change, false);
	
	var timeframeConfirmBtn = document.getElementsByName("btn_time_frame_confirm")[0];
	timeframeConfirmBtn.addEventListener('click', eh_timeframe_button_confirm, false);
}

var eh_timeframe_button_confirm = function(event){
	Ajax("get/", renderTenentList);
};

var eh_selection_change = function(event) {
	Ajax(event.target.value+"/", renderTenentDetailTable);
};

var Ajax = function(url, callback) {
	var xmlhttp;
	if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp = new XMLHttpRequest();
	} else {// code for IE6, IE5
		xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			var data = xmlhttp.responseText;
			callback(data);
		}
	};
	xmlhttp.open("get", url, false);
	xmlhttp.send(null);
};

