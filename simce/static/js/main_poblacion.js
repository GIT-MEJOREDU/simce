/*
*    main_gapminder.js
*    Mastering Data Visualization with D3.js
*    Project 2 - Gapminder Clone
*/
d3.json("../../static/datos/dimension_data.json").then(function (all_data) {
	//console.log(all_data);

	//data = data[0];
	//console.log("all_data: ", all_data);

	//se definen margenes
	var margin = { left: 50, right: 50, top: 10, bottom: 70 };

	//se definen dimensones del canvas svg
	var width = 900 - margin.left - margin.right,
		height = 600 - margin.top - margin.bottom;
	//console.log("width: ", width);
	//console.log("hight: ", height);


	var idCiclos = ["1", "102", "203", "304", "405", "506", "607", "708", "809", "910", "1011", "1112", "1213", "1314", "1415", "1516"];

	var ciclos = ["2000-2001", "2001-2002", "2002-2003", "2003-2004", "2004-2005", "2005-2006",
		"2006-2007", "2007-2008", "2008-2009", "2009-2010", "2010-2011", "2011-2012",
		"2012-2013", "2013-2014", "2014-2015", "2015-2016"];

	var rangoCiclos = d3.scaleOrdinal()
		.domain(ciclos)
		.range(idCiclos);

	//se agregan opciones al select de ciclo
	var opcCiclo = d3.select("#ciclo").selectAll("option")
		.data(ciclos)
		.enter().append("option")
		.text(d => d);

	var edad = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24];

	//se agregan opciones al select de edad
	var opcEdad = d3.select("#edad").selectAll("option")
		.data(edad)
		.enter().append("option")
		.text(d => d);


	var idEntidadFed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
	var entidadFederativa = ["AGS", "BC", "BCSUR", "CAMP", "COAH",
		"COL", "CHIS", "CHIH", "CDMX", "DURGO",
		"GUAN", "GUERR", "HID", "JAL", "MEX",
		"MICH", "MOR", "NAY", "NL", "OAX",
		"PUE", "QUER", "QROO", "SLP", "SIN",
		"SON", "TAB", "TAMPS", "TLAX", "VER", "YUC", "ZAC", "REPM"];

	var rangoEntidades = d3.scaleOrdinal()
		.domain(idEntidadFed)
		.range(entidadFederativa);

	// Rango de colores
	var myColor = d3.scaleOrdinal()
		.domain(edad)
		//.range(["#2ca02c", "#ff7f0e", "#d62728", "#CACA0B"]);
		.range(["gold", "blue", "green", "yellow", "black", "grey", "darkgreen", "pink", "brown", "slateblue", "grey1", "orange"]);
	//.range(["blue", "red"]);

	//se crea grupo en tag ID = chart_area
	var g = d3.select("#chart-area")
		.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
		.append("g")
		.attr("transform", "translate(" + margin.left + ", " + margin.top + ")");

	var poblacionMax = d3.max(all_data, function (d) {
		return d.poblacion;
	})
	var poblacionMin = d3.min(all_data, function (d) {
		return d.poblacion;
	});
	console.log("poblacion min", poblacionMin);
	console.log("poblacion max", poblacionMax);

	//Escala logarítmica para eje y
	var yScale = d3.scaleLog()
		.domain([poblacionMax, 9000])
		//.domain([350000, 9000])
		.range([0, height])
		.base(10);

	//Escala lineal para eje X
	var xScale = d3.scaleBand()
		.range([margin.left, width - margin.right])
		.domain(all_data.map(function (d) { return rangoEntidades(d.id_estado); }))
		.padding(0.1)
		.align(0.1);


	//Eje Y
	var yAxisCall = d3.axisLeft(yScale)
		.tickValues([1000, 10000, 100000, 1000000, 10000000])
		.tickFormat(d3.format(">r"))
	g.append("g")
		.attr("transform", "translate (" + margin.left + ",0)")
		.attr("class", "y-axis")
		.call(yAxisCall);

	//eje X
	var xAxisCall = d3.axisBottom(xScale)
	g.append("g")
		.attr("transform", "translate (0," + height + ")")
		.attr("class", "x-axis")
		.call(xAxisCall)
		.selectAll("text")
		.attr("y", "10")
		.attr("x", "-5")
		.attr("text-anchor", "end")
		.attr("transform", "rotate(-40)");

	// Tooltip
	var tip = d3.tip()
		.attr('class', 'd3-tip')
		.html(function (d) {
			var text = "<strong>Edad:</strong> <span style='color:red'>" + d.edad + "</span><br>";
			text += "<strong>Grupo de Edad:</strong> <span style='color:red;text-transform:capitalize'>" + d.edad_grupo + "</span><br>";
			text += "<strong>Estado</strong> <span style='color:red;text-transform:capitalize'>" + rangoEntidades(d.id_estado) + "</span><br>";
			text += "<strong>Población:</strong> <span style='color:red'>" + d.poblacion + "</span><br>";
			return text;
		})

	g.call(tip);

	// X label
	g.append("text")
		.attr("class", "x axis-label")
		.attr("x", width / 2)
		.attr("y", height + 60)
		.attr("font-size", "20px")
		.attr("text-anchor", "middle")
		.text("Entidad Federativa");

	// Y label
	g.append("text")
		.attr("class", "y axis-label")
		.attr("x", -(height / 2))
		.attr("y", -30)
		.attr("font-size", "20px")
		.attr("text-anchor", "middle")
		.attr("transform", "rotate(-90)")
		.text("Población");

	//Se selecciona un ciclo en específico
	var data = all_data.filter(function (d) { return d["id_ciclo"] == 1 });
	//console.log("Data Set Selected: ", data);

	//var circles = g.selectAll("circle");

	//update(1);
	update(rangoCiclos(d3.select("#ciclo").property("value")), d3.select("#edad").property("value"), 24)

	function update(idCiclo, edad1, edad2) {
		console.log("ciclo: ", idCiclo);
		console.log("color: ", myColor(edad1), myColor(edad2));
		var color = myColor(edad1)
		//console.log("interval: ",cont);

		var data_int = all_data.filter(function (d) { return d["id_ciclo"] == idCiclo });
		var data = data_int.filter(function (d) { return (d["edad"] == edad1 || d["edad"] == edad2) });
		//var data = data_int.filter(function (d) { return d["edad"] == edad1 });

		//var data = data_int;
		console.log("data:", data);

		//se agregan nuevos datos
		var circles = g.selectAll("circle")
			.data(data);

		//Se borran puntos anteriores
		circles.exit().remove();

		circles
			.attr("cx", function (d) { return xScale(rangoEntidades(d.id_estado)); })
			.attr("cy", function (d) { return yScale(d.poblacion); })
			.attr("fill", function (d) { return myColor(d.edad) })
			.attr("r", 5)
			.attr("stroke", "black")
			.attr("stroke-width", 1);

		//se despliega gráfica con nuevos datos
		circles.enter()
			.append("circle")
			.attr("cx", function (d) {
				return xScale(rangoEntidades(d.id_estado));
			})
			.attr("cy", function (d) {
				return yScale(d.poblacion);
			})
			.attr("fill", function (d) { return myColor(d.edad) })
			.attr("r", 5)
			.attr("stroke", "black")
			.attr("stroke-width", 1)
			.on("mouseover", tip.show)
			.on("mouseout", tip.hide);

	}

	//Se selecciona el Ciclo (2001-2001 al 2015-2016)
	var selectCiclo = d3.select("#ciclo")
		.on("change", function () {
			update(rangoCiclos(d3.select("#ciclo").property("value")), d3.select("#edad").property("value"), 24)
		})

	//Se selecciona edad entre 3 y 24
	var selecEdad = d3.select("#edad")
		.on("change", function () {
			update(rangoCiclos(d3.select("#ciclo").property("value")), d3.select("#edad").property("value"), 24)
		})

});
