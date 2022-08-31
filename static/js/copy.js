var btn = document.getElementById('copybutton');
btn.addEventListener('click',copiar,false);

function copiar(){
    var copytext = document.getElementById('copytext');
    var inputF = document.createElement('input');
    inputF.setAttribute("value",copytext.innerHTML);
    document.body.append(inputF);
    inputF.select();
    document.execCommand('copy');
    document.body.removeChild(inputF);
}