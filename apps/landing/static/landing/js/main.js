/**
 * Created with PyCharm.
 * User: arthur
 * Date: 7/07/13
 * Time: 10:16 AM
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function () {
    $('a[rel]').overlay({
        fixed: false
    });

    $.noConflict();
    $('#id_appointment_date').datepicker({
        dateFormat: 'dd/mm/yy'
    });
});
