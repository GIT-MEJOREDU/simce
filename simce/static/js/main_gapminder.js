/*
*    main_gapminder.js
*    Mastering Data Visualization with D3.js
*    Project 2 - Gapminder Clone
*/
d3.json("../../static/datos/data_gapminder.json").then(function (all_data) {
	//console.log(all_data);

	all_data.forEach(function (d) { d.year = +d.year; });
	//data = data[0];
	//console.log("all_data: ", all_data);

	//Se filtran registros de ciudades que no tienen cifras en Expectativa de vida e ingresos
	all_data.filter(descartar);

	//se definen margenes
	var margin = { left: 50, right: 50, top: 10, bottom: 50 };

	//se definen dimensones del canvas svg
	var width = 900 - margin.left - margin.right,
		height = 600 - margin.top - margin.bottom;
	//console.log("width: ", width);
	//console.log("hight: ", height);


	var continent_color = d3.scaleOrdinal()
		.range(["#d62728", "#ff7f0e", "#ffff00", "#2ca02c"]);

	//se crea grupo en tag ID = cart_area
	var g = d3.select("#chart-area")
		.append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
		.append("g")
		.attr("transform", "translate(" + margin.left + ", " + margin.top + ")")

	// Tooltip
	var tip = d3.tip()
		.attr('class', 'd3-tip')
		.html(function (d) {
			var text = "<strong>Country:</strong> <span style='color:red'>" + d.country + "</span><br>";
			text += "<strong>Continent:</strong> <span style='color:red;text-transform:capitalize'>" + d.continent + "</span><br>";
			text += "<strong>Life Expectancy:</strong> <span style='color:red'>" + d3.format(".2f")(d.life_exp) + "</span><br>";
			text += "<strong>GDP Per Capita:</strong> <span style='color:red'>" + d3.format("$,.0f")(d.income) + "</span><br>";
			text += "<strong>Population:</strong> <span style='color:red'>" + d3.format(",.0f")(d.population) + "</span><br>";
			return text;
		})

	g.call(tip);

	var continents = ["europe", "asia", "americas", "africa"];

	var colorContinent = d3.scaleOrdinal()
		.domain(continents)
		.range(["#2ca02c", "#ff7f0e", "#d62728", "#CACA0B"]);
	//verde,Anaranjado,rojo,amarillo    

	//Escala logarítmica para eje x
	var xScaleLog = d3.scaleLog()
		.domain([200, 250000])  //.domain([50, 400000])
		.range([0, width])
		.base(10);

	//Escala lineal para eje Y
	var yScale = d3.scaleLinear()
		.domain([90, 0])
		.range([0, height]);

	var minPopulation = d3.min([all_data[0]], function (d) {
		var countryMin = d3.min(d.countries, function (d) {
			return d.population;
		})
		return countryMin;
	});
	console.log("minPopulation", minPopulation);

	var maxPopulation = d3.max([all_data[0]], function (d) {
		var countryMax = d3.max(d.countries, function (d) {
			return d.population;
		})
		return countryMax;
	});
	console.log("maxPopulation", maxPopulation);

	//Escala para definir el radio de los circulos que representan cada pais
	//El tamaño del circulo representa la población
	var areaScale = d3.scaleLinear()
		.domain([minPopulation, maxPopulation])
		.range([28, 1300]);	//rango en área, para calcular el radio de cada circulo

	//eje X
	var xAxisCall = d3.axisBottom(xScaleLog)
		.tickValues([2000, 20000, 200000])
		.tickFormat(d3.format("($.2f"));
	//.tickFormat(function(d){ return "$USD:"});

	//Eje Y
	var yAxisCall = d3.axisLeft(yScale);
	g.append("g")
		.attr("class", "y-axis")
		.call(yAxisCall);

	// X label
	g.append("text")
		.attr("class", "x axis-label")
		.attr("x", width / 2)
		.attr("y", height + 40)
		.attr("font-size", "20px")
		.attr("text-anchor", "middle")
		.text("Ingreso PerCapita");

	// Y label
	g.append("text")
		.attr("class", "y axis-label")
		.attr("x", -(height / 2))
		.attr("y", -30)
		.attr("font-size", "20px")
		.attr("text-anchor", "middle")
		.attr("transform", "rotate(-90)")
		.text("Promedio de Vida");

	g.append("g")
		.attr("class", "x-axis")
		.attr("transform", "translate (0," + height + ")")
		.call(xAxisCall);

	var data = [];

	//Agregando grupo para leyenda
	var legend = g.selectAll("legend")
		.data(continents)
		.enter().append("g")
		.attr("class", "legend")
		.attr("transform", function (d, i) { return "translate(" + (width - margin.right - 20) + "," + (height - (2 * margin.bottom) - (i * 20)) + ")"; })
		.style("font", "18px sans-serif");

	//Se agregan rectángulos a la leyenda
	legend.append("rect")
		.attr("x", 70)
		.attr("width", 18)
		.attr("height", 18)
		.attr("fill", colorContinent);

	//Se agrega texto a la leyenda
	legend.append("text")
		.attr("x", 50)
		.attr("y", 9)
		.attr("dy", ".35em")
		.attr("text-anchor", "end")
		.text(function (d) { return d; });

	//Etiqueta Año
	var yearLabel = g.append("g")
		.attr("transform", "translate (" + (width - margin.right - 80) + "," + (height - margin.bottom) + ")")
		.attr("test-anchor", "end")
		.append("text")
		.text("AÑO: " + all_data[0].year)
		.attr("class", "title")
		.attr("font-size", "30px");

	//console.log("all_data: ", all_data.length);

	function update() {
		//console.log("interval: ",cont);

		data = all_data[cont].countries;
		//console.log("data:", data);

		var circles = g.selectAll("circle")
			.data(data);

		circles.exit().remove();

/*  		circles
			.attr("fill", "green")
			.attr("cx", function (d, i) {
				if (d.income > 0 && d.life_exp > 0) { return xScaleLog(d.income) };
			})
			.attr("cy", function (d, i) {
				if (d.income > 0 && d.life_exp > 0) { return yScale(d.life_exp) };
			})
			.attr("fill", function (d) { return colorContinent(d.continent) })
			.attr("r", function (d) { return circleRadio(areaScale(d.population)) });  */
			circles
			.attr("fill", "green")
			.attr("cx", function (d, i) {return xScaleLog(d.income); })
			.attr("cy", function (d, i) {return yScale(d.life_exp); })
			.attr("fill", function (d) { return colorContinent(d.continent) })
			.attr("r", function (d) { return circleRadio(areaScale(d.population)) });

		circles.enter()
			.append("circle")
			.attr("fill", "green")
			.attr("cx", function (d, i) {
				return xScaleLog(d.income);
			})
			.attr("cy", function (d, i) {
				return yScale(d.life_exp);
			})
			.attr("fill", function (d) { return colorContinent(d.continent) })
			.attr("r", function (d) { return circleRadio(areaScale(d.population)) })
			.on("mouseover", tip.show)
			.on("mouseout", tip.hide);

		//Se actualiza la etiqueta AÑO
		yearLabel.text("AÑO: " + all_data[cont].year);

		cont = cont + 1;
		if (cont >= all_data.length) { cont = 0; }
	}

	var cont = 0
	update();
	d3.interval(function () { update() }, 200);

	function descartar(item) {
		//se filtran las ciudades que no tienen cifras en expectativa de vida y ingresos
		f_item = item.countries.filter(country => (country.life_exp !== null && country.income !== null));
		item.countries = f_item;
		return item;
	}

	/*
		Radio 28.274328000000004 =	3
		Radio 1300 =				20.342146841672946
	*/
	//Se obtiene el RADIO de un circulo a partir del AREA 
	function circleRadio(area) {
		return Math.sqrt(area / 3.141592);
	}


});
