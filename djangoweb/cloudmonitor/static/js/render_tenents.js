/**
 * @author zhangxg
 */

function render_tenents(tenents){
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
			div.appendChild(document.createTextNode(tenents[i+j]));
			div.setAttribute('id', tenents[i+j]);
			
			var num = Math.floor(Math.random()*10 + 1);
			if (num%2 == 0) {
				div.setAttribute('class', 'level_high');
			} else if (num%5 == 0) {
				div.setAttribute('class', 'level_warn');
			} else {
				div.setAttribute('class', 'level_normal');
			}

			td.appendChild(div);
			tr.appendChild(td);
		}
		i += 5;
		table.appendChild(tr);
	}
}
