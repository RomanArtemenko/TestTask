$(document).ready(function(){
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            }
        }
    });

    // ������� ������������� ��� �������� ��� ��������� �������
    var delay = (function(){
        var timer = 0;
        return function(callback, ms){
            clearTimeout (timer);
            timer = setTimeout(callback, ms);
        };
    })();

    // ������� ��� �������� ���� ���������� ������� massive.sort(compareNumeric)
    function compareNumeric(a, b) {
        if (a > b) return 1;
        if (a < b) return -1;
    }

    // ������� ��� ������ ����� � ������� �� �������� (������������ ��� ������ ������)
    function get_key (data, value, notvalue) {
        for (key in data) {
            if (data[key] == value && key != notvalue)
                return key;
        }
        return null;
    };

    // ������� ��������� ������� ������� � textarea, ��������� ��������� ��������� � ������ ���������� ������
    $('textarea[name="inpText"]').on('keyup', function () {
        delay(function() {
            $inp_text = $('textarea[name="inpText"]');
            $shift = $('input[name="shift"]');

            // ���� � textarea �����, �� �������
            if ($inp_text.val().length == 0) {
                $shift.val('');
                return;
            }

            var data = {};
            var txt = $inp_text.val().replace(/[^a-z]/g, "");

            for (var i = 0; i < txt.length; i++) {
                if (data[txt[i]] === undefined) {
                    data[txt[i]] = 0;
                }
                data[txt[i]] += 1;
            }

            var keys = Object.keys(data);
            keys.sort();

            var dataSlices = [];
            var ticks = [];

            for (var i=0; i<keys.length; i++) {
                ticks.push(keys[i]);
                dataSlices.push(data[keys[i]]);
            }

            var barData = {
                labels: ticks,
                datasets: [
                    {
                        label: '��������� ��������� ��������� ������',
                        currentStyle: null,
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1,
                        data: dataSlices
                    }
                ]
            };
            drawChart(barData);

            // ������� ����������� ������ ����������� ������ � ������, ���� � ������ ����� 10-�� ���������� ��������
            if (keys.length > 10) {
                var values = dataSlices.sort(compareNumeric).reverse();;
                var hf1 = get_key(data, values[0], null);
                var hf2 = get_key(data, values[1], hf1);
                var hf = ['e', 't', 'a', 'o'];

                if (hf.indexOf(hf1) == 0 || hf.indexOf(hf2) == 0) {
                    $shift.val('������ ���');
                } else {
                    var sh1 = hf1.charCodeAt(0) - 'e'.charCodeAt(0);
                    if (sh1 < 0) sh1 += 26;
                    var sh2 = hf2.charCodeAt(0) - 'e'.charCodeAt(0);
                    if (sh2 < 0) sh2 += 26;

                    $shift.val('�����: ' + (sh1).toString() + ' ��� ' + (sh2).toString());
                }
            }else $shift.val('');

        }, 1000 );
    });

    // ������� ��������� �������
    function drawChart(data){
        $('#results-graph').remove();
        var c = document.createElement('canvas');
        c.id = 'results-graph';
        document.getElementById('graph-container').appendChild(c);

        var context = document.getElementById('results-graph').getContext('2d');
        context.canvas.width = 750;
        context.canvas.height = 250;
        var myBarChart = new Chart(context, {
            type: 'bar',
            data: data,
            options: {
                maintainAspectRatio: true,

                scales: {
                    yAxes: [
                        {
                            ticks: {
                                beginAtZero: true,
                                fixedStepSize: 10
                            }
                        }
                    ]
                }
            }
        });
    }

    // ���������� ������� �� ���������� ������ � ������� ������ � ��������� ��� � inp textarea
    $('button.loadtext').on('click',function(){
        var $inp_text = $('textarea[name="inpText"]');
        var $out_text = $('textarea[name="outText"]');

        $.ajax({
                type: "POST",
                url:  "/get_text",
                data: JSON.stringify({'id': $(this).val()}),
                contentType: 'application/json',
                cache: false,
                success: function(data){
                    $inp_text.val(data.text);
                    $out_text.val('');
                },
                error: function (xhr) {
                    console.log(xhr);
                }});

        $inp_text.keyup();

    });

    // ���������� ������� �� ������ ���������/����������� � ��������� ���������� � out textarea
    $('button.search').on('click',function(){
        var $inp_query = $('input[name="inpQuery"]');

        if ($inp_query.val()){
            $.ajax({
                type: "POST",
                url: "/",
                data: JSON.stringify({'query': $inp_query.val().toLowerCase()}),
                contentType: "application/json",
                cache: false,
                success: function(data){
                    alert(data.filter('table'));
                    //console.log(data);
                },
                error: function(xhr){
                    console.log(xhr);
                }
            });
        }
    });
});