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

	for (var i = 0; i < data.length; i++) {

		var detail = data[i].detail.cpu_util;
		if (detail) {
			var graphHolder = document.getElementById(i + "cpu");

			var unit = detail.counter_unit;
			var timestamps = detail.timestamp;

			var xAxis = new Array();
			var yAxis = new Array();
			for (var j = 0; j < timestamps.length; j++) {
				xAxis[j] = timestamps[j][0];
				yAxis[j] = timestamps[j][1];
			}
			drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
		}
	}
}

function drawMemeoryGraph(data) {
	for (var i = 0; i < data.length; i++) {
		var detail = data[i].detail.memory;
		if (detail) {
			var graphHolder = document.getElementById(i + "mem");
			var unit = detail.counter_unit;
			var timestamps = detail.timestamp;

			var xAxis = new Array();
			var yAxis = new Array();
			for (var j = 0; j < timestamps.length; j++) {
				xAxis[j] = timestamps[j][0];
				yAxis[j] = timestamps[j][1];
			}
			drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
		}

	}
}

function drawDiscReadGraph(data) {
	for (var i = 0; i < data.length; i++) {
		var detail = data[i].detail.volume_read;
		if (detail) {
			var graphHolder = document.getElementById(i + "disk_read");
			var unit = detail.counter_unit;

			var volumes = new Array();
			for (var j = 0; j < detail.volumes.length; j++) {
				var volume = detail.volumes[j];
				var volume_id = volume[0];
				var timeSeries = volume[1];

				var xAxis = new Array();
				var yAxis = new Array();
				for (var k = 0; k < timeSeries.length; k++) {
					xAxis[k] = timeSeries[k][0];
					yAxis[k] = timeSeries[k][1];
				}
			}
			drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
		}
	}
}

function drawDiscWriteGraph(data) {
	for (var i = 0; i < data.length; i++) {
		var detail = data[i].detail.volume_write;
		if (detail) {
			var graphHolder = document.getElementById(i + "disk_write");
			var unit = detail.counter_unit;

			var volumes = new Array();
			for (var j = 0; j < detail.volumes.length; j++) {
				var volume = detail.volumes[j];
				var volume_id = volume[0];
				var timeSeries = volume[1];

				var xAxis = new Array();
				var yAxis = new Array();
				for (var k = 0; k < timeSeries.length; k++) {
					xAxis[k] = timeSeries[k][0];
					yAxis[k] = timeSeries[k][1];
				}
			}
			drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
		}
	}
}

function drawNetworkInGraph(data) {
	for (var i = 0; i < data.length; i++) {
		var detail = data[i].detail.network_in;
		if (detail) {
			var graphHolder = document.getElementById(i + "network_in");
			var unit = detail.counter_unit;

			var taps = new Array();
			for (var j = 0; j < detail.taps.length; j++) {
				var tap = detail.taps[j];
				var tap_id = tap[0];
				var timeSeries = tap[1];

				var xAxis = new Array();
				var yAxis = new Array();
				for (var k = 0; k < timeSeries.length; k++) {
					xAxis[k] = timeSeries[k][0];
					yAxis[k] = timeSeries[k][1];
				}
			}
			drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
		}
	}
}

function drawNetworkOutGraph(data) {
	for (var i = 0; i < data.length; i++) {
		var detail = data[i].detail.network_out;
		if (detail) {
			var graphHolder = document.getElementById(i + "network_out");
			var unit = detail.counter_unit;

			var taps = new Array();
			for (var j = 0; j < detail.taps.length; j++) {
				var tap = detail.taps[j];
				var tap_id = tap[0];
				var timeSeries = tap[1];

				var xAxis = new Array();
				var yAxis = new Array();
				for (var k = 0; k < timeSeries.length; k++) {
					xAxis[k] = timeSeries[k][0];
					yAxis[k] = timeSeries[k][1];
				}
			}
			drawGraph(graphHolder, ["abc"], xAxis, yAxis, unit);
		}
	}
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

function render_tenents(tenents) {
	var div_summary = document.getElementById("summary");

	div_summary.appendChild(document.createTextNode("Current Tenents: " + tenents.length));
	div_summary.appendChild(document.createElement("br"));
	div_summary.appendChild(document.createTextNode("High Consumpation: " + 3));
	div_summary.appendChild(document.createElement("br"));
	div_summary.appendChild(document.createTextNode("Normal Consumpation: " + 10));

	var table = document.getElementById('table_tenent_detail');

	// var data = JSON.parse(dataStr);

	for (var i = 0; i < tenents.length; i++) {
		var tr = document.createElement('tr');

		// var td_image_id = document.createElement('td');
		// td_image_id.appendChild(document.createTextNode(data[i].vm_id));

		for (var j = 0; j < 5; j++) {
			var td = document.createElement('td');
			var div = document.createElement('div');

			var link = document.createElement("a");
			link.setAttribute("href", "/cloudmonitor/dashboard/tenents/" + tenents[i + j]);
			link.appendChild(document.createTextNode(tenents[i + j]));
			div.appendChild(link);
			div.setAttribute('id', tenents[i + j]);

			var num = Math.floor(Math.random() * 10 + 1);
			if (num % 2 == 0) {
				div.setAttribute('class', 'level_high');
			} else if (num % 5 == 0) {
				div.setAttribute('class', 'level_warn');
			} else {
				div.setAttribute('class', 'level_normal');
			}

			// div.addEventListener('click', eh_tenent_selection, false);

			td.appendChild(div);
			tr.appendChild(td);
		}
		i += 5;
		table.appendChild(tr);
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
	drawDiscReadGraph(data);
	drawDiscWriteGraph(data);
	drawNetworkInGraph(data);
	drawNetworkOutGraph(data);

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

function registerEventHandler() {
	var tenentSelection = document.getElementById("sel_tenent_selection");
	tenentSelection.addEventListener('change', eh_tenent_selection, false);

	var timeframeConfirmBtn = document.getElementsByName("btn_time_frame_confirm")[0];
	timeframeConfirmBtn.addEventListener('click', eh_timeframe_button_confirm, false);
}

var eh_timeframe_button_confirm = function(event) {
	Ajax("get/", renderTenentList);
};

var eh_tenent_selection = function(event) {
	Ajax(event.target.value + "/", renderTenentDetailTable);
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

