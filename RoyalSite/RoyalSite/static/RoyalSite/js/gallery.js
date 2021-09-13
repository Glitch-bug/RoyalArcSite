var fullImageSet = document.getElementsByClassName('fullImage')[0]
    var navBar = document.getElementsByClassName('navbar')[0]
    var img = fullImageSet.childNodes[1]
    var images = document.getElementsByClassName('cImg')
    var gala = document.getElementById('gala')
    var data = '{{ gallery_qs }}'
    var id = 0
    var slide = False
  


    function closeFullImg() {
      fullImageSet.style.display = 'none'
      navBar.style.display = 'flex'
    }

    function openFullImg(src, did) {
      fullImageSet.style.display = 'flex'
      navBar.style.display = 'none'
      img.src = src
      id = did
      console.log(id)
    }

    function prev() {
      if (id < images.length) {
        src = document.getElementById(id+1).src
        console.log(img.src)
        img.src = src
        console.log(img.src)
        id += 1
      }else {
        src = document.getElementById(1).src
        id = 1
      }
    }

    function next() {
      if (id > 1) {
        src = document.getElementById(id-1).src
        console.log(img.src)
        img.src = src
        console.log(img.src)
        id -= 1
        
      }else {
        src = document.getElementById(images.length).src
        img.src = src
        id = images.length
      }
      console.log(id)
    };
    