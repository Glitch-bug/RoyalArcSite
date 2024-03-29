var fullImageSet = document.getElementsByClassName('fullImage')[0]
var navBar = document.getElementsByClassName('navbar')[0]
var img = fullImageSet.childNodes[1]
var images = document.getElementsByClassName('cImg')
var gala = document.getElementById('gala')
var data = '{{ gallery_qs }}'
var id = 0
var slide_info = document.getElementById('slide-info')


document.addEventListener('DOMContentLoaded', function(){
  var cala = document.querySelector('#gala')
  var imgContainers = cala.querySelectorAll('.img')
  for (i=0; i<imgContainers.length; i++){
     pimg = imgContainers[i].querySelector('.cImg')
     cala.querySelectorAll('.img')[i].querySelector('.cImg').outerHTML = `<img id="${i+1}" class="cImg" src='${pimg.src}' placeholder="image not found" onclick="openFullImg(this.src, this.id)"></img>`
  }
  console.log(document.querySelectorAll('.cImg'))
});

function closeFullImg() {
  fullImageSet.style.display = 'none'
  navBar.style.display = 'flex'
  stop()
}

function openFullImg(src, did) {
  fullImageSet.style.display = 'flex'
  navBar.style.display = 'none'
  img.src = src
  id = did
  console.log()
}

function prev() {
  if (id < images.length) {
    src = document.getElementById(id+1).src
    img.src = src
    id += 1
  }else {
    src = document.getElementById(1).src
    id = 1
  }
}

function next() {
  if (id > 1) {
    src = document.getElementById(id-1).src
    img.src = src
    id -= 1
    
  }else {
    src = document.getElementById(images.length).src
    img.src = src
    id = images.length
  }
};

function slide() {
  document.getElementById('slide').outerHTML ='<ion-icon id="slide" name="stop-circle-outline" onclick="stop()"></ion-icon>'
  intId = setInterval(next, 2500)
  slide_info.innerHTML = "end slideshow"
}

function stop() {
  document.getElementById('slide').outerHTML ='<ion-icon id="slide" name="caret-forward-circle-outline" onclick="slide()"></ion-icon>'
  slide_info.innerHTML = "slideshow"
  clearInterval(intId)
}
