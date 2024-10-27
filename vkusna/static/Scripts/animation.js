const animate = document.querySelectorAll('p')
/*
animate.addEventListener('click',function (e) {
    alert(a.toString())
    var t = new Transport(1, 'efg')
    console.warn(t)
})
*/
for (let animateElement of animate) {
    console.log(animateElement);
//       animation: 7s 2s infinite cubic-bezier(0.87, -0.24, 0, 0.26) Alts;
    animateElement.addEventListener('dblclick', (e) => {
        e.target.style.animation = '7s 2s infinite cubic-bezier(0.87, -0.24, 0, 0.26) Alts'
    })
}
for (let i = 0; i < animate.length; i++) {
    let p = animate[i]
    p.textContent = v[i].toString()

}
