document.addEventListener("DOMContentLoaded", function() {
    setInterval(change, 8000);
});

var num = 0;

function change() {
    var text = rdata[num]['fields']['text']
    var italics = rdata[num]['fields']['title']
    document.getElementById('italic').innerHTML = italics
    document.getElementById('shows').innerHTML = text;
    if (num < rdata.length - 1) {
    num++;
    } else {
    num = 0
    }
    
}
