// creates the constants height and width based on the user's size input
$('#sizePicker').submit(function (evt){
    evt.preventDefault();
    const height = $('#inputHeight').val();
    const width = $('#inputWidth').val();
    makeGrid(height, width)
})

// the function makeGrid aims to create a grid based on the user's size input
function makeGrid(gridHeight, gridWidth) {
    // removes table rows that have been created before
    $('tr').remove();
    // loops over gridHeight and gridWidth and appends rows & cells to the table
    for (let i = 1; i <= gridHeight; i++) {
        $('#pixelCanvas').append('<tr id=table' + i + '></tr>');
        for (let j = 1; j <= gridWidth; j++) {
            $('#table' + i).append('<td></td>');
        }
    }
    // adds picked colour to a cell the user has clicked on
    $('td').click(function addColor() {
    const color = $('#colorPicker').val();
    // if the selected cell has a color, it'll be removed. If not, a color is added.
    if($(this).attr('style')) {
       $(this).removeAttr('style')
    } else {
      $(this).attr('style', 'background-color:' + color);
    }
  })
}
