function updateDiskPartitionTable() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'diskPart'},
        error: function() {
            $( '#error-dialog' ).dialog( "open" );
        },
        success: function(data) {
            $( '#disk-partition-table' ).html(data["jstable"]);
            $( '#disk-partition-date' ).text(data["request_time"]);
        }
    });
}

function updateMemIntensiveProcesses() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'cpuIntensProc'},
        error: function() {
            $( '#error-dialog' ).dialog( "open" );
        },
        success: function(data) {
            $( '#ram-intens-proc-table' ).html(data["jstable"]);
            $( '#ram-intens-proc-date' ).text(data["request_time"]);
        }
    });
}

function updateCpuIntensiveProcesses() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'ramIntensProc'},
        error: function() {
            $( '#error-dialog' ).dialog( "open" );
        },
        success: function(data) {
            $( '#cpu-intens-proc-table' ).html(data["jstable"]);
            $( '#cpu-intens-proc-date' ).text(data["request_time"]);
        }
    });
}

var smoothieRamUsage =       new SmoothieChart({maxValue:100,minValue:0});
var smoothieCpuAvgLoad =     new SmoothieChart({maxValueScale:1.06});
var smoothieCpuUtilization = new SmoothieChart({maxValue:100,minValue:0});

var ramUsageLine =           new TimeSeries();
var cpuUtilizationLine =     new TimeSeries();
var cpuAvgLoadLine1mins =    new TimeSeries();
var cpuAvgLoadLine5mins =    new TimeSeries();
var cpuAvgLoadLine15mins =   new TimeSeries();

var intervalListener;

function updateRamUsageCharts() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'ramUsageCharts'},
        error: function() {},
        success: function(data) {
            $( '#ram-usage-date' ).text(data["request_time"]);
            var ram_usage_perc = data["timeseries_data"];
            ramUsageLine.append(new Date().getTime(), ram_usage_perc);
            $( '#ram-usage-used' ).text(data["free_ram"] + ' MB (' + ram_usage_perc.toFixed(1) + '%)');
            $( '#ram-usage-free' ).text(data["used_ram"] + ' MB of ' + data["total_ram"] + ' MB');
        }
    });
}

function updateCpuAvgLoadCharts() {
    $.ajax({
        url: '/sysdata',
        type: 'get',
        cache: false,
        data: {'data_name': 'cpuAvgLoadCharts'},
        error: function() {},
        success: function(data) {
            $( '#cpu-avg-load-date' ).text(data["request_time"]);

            cpuAvgLoadLine1mins.append(new Date().getTime(), data["timeseries_data1"]);
            $( '#avg-load-1-min' ).text(data["timeseries_data1"]);

            cpuAvgLoadLine5mins.append(new Date().getTime(), data["timeseries_data5"]);
            $( '#avg-load-5-min' ).text(data["timeseries_data5"]);

            cpuAvgLoadLine15mins.append(new Date().getTime(), data["timeseries_data15"]);
            $( '#avg-load-15-min' ).text(data["timeseries_data15"]);
        }
    });
}

function updateCpuUtilizationCharts() {
    $.ajax({
        url: '/sysdata',
        cache: false,
        type: 'get',
        data: {'data_name': 'cpuUtilizationCharts'},
        error: function() {},
        success: function(data) {
            $( '#cpu-utilization-date' ).text(data["request_time"]);
            var cpu_util_perc = data["timeseries_data"];
            cpuUtilizationLine.append(new Date().getTime(), cpu_util_perc);
            $( '#cpu-utilization-percentage' ).text(cpu_util_perc.toFixed(2) + "%")
        }
    });
}

$( document ).ready(function() {
    updateDiskPartitionTable();
    updateCpuIntensiveProcesses();
    updateMemIntensiveProcesses();
    updateCpuAvgLoadCharts();
    updateRamUsageCharts();
    updateCpuUtilizationCharts();

    smoothieRamUsage.streamTo(document.getElementById("ram-usage-canvas"));
    smoothieCpuAvgLoad.streamTo(document.getElementById("cpu-avg-load-canvas"));
    smoothieCpuUtilization.streamTo(document.getElementById("cpu-util-canvas"));

    setInterval(function() {
        updateCpuAvgLoadCharts();
    }, 1500);
    setInterval(function() {
        updateRamUsageCharts();
    }, 1500);
    setInterval(function() {
        updateCpuUtilizationCharts();
    }, 1500);

    smoothieRamUsage.addTimeSeries(ramUsageLine,
        {lineWidth:2,strokeStyle:'#0000ff',fillStyle:'rgba(0,128,255,0.30)'});
    smoothieCpuUtilization.addTimeSeries(cpuUtilizationLine,
        {lineWidth:2,strokeStyle:'#0000ff',fillStyle:'rgba(0,128,255,0.30)'});
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine1mins,
        {lineWidth:2,strokeStyle:'#C7002C'});
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine5mins,
        {lineWidth:2,strokeStyle:'#08876B'});
    smoothieCpuAvgLoad.addTimeSeries(cpuAvgLoadLine15mins,
        {lineWidth:2,strokeStyle:'#147AE0'});

    var sourceSwap = function () {
        var $this = $(this);
        var newSource = $this.data('alt-src');
        $this.data('alt-src', $this.attr('src'));
        $this.attr('src', newSource);
    }

    $('img.reload').hover(sourceSwap, sourceSwap);

	$( '#error-dialog' ).dialog({
		autoOpen: false
	});

	$( '#job-success-dialog' ).dialog({
		autoOpen: false,
		resizable: false,
		modal: true,
		buttons: {
			"Ok": function () {
				$(this).dialog('close');
			}
		}
	});

    $( '#ram-intens-proc-reload' ).click(function(e) {
        e.preventDefault();
        updateMemIntensiveProcesses();
	});
    $( '#cpu-intens-proc-reload' ).click(function(e) {
        e.preventDefault();
        updateCpuIntensiveProcesses();
	});
    $( '#disk-partition-reload' ).click(function(e) {
        e.preventDefault();
        updateDiskPartitionTable();
	});
});
