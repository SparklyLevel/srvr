const playerHTML = document.querySelector('.red')
let player = {
    speed: 10,
    x: 0,
    y: 0,
    z: 0,
    main: playerHTML,
    loadCords() {
        const localPlayer = JSON.parse(localStorage.getItem('player'));
        this.y = localPlayer.y;
        this.x = localPlayer.x;
        this.main.style.margin = `${player.y}px ${player.x}px`;
        this.main.textContent = `x:${player.x} \n y:${player.y}`
    },
    saveCords() {
        localStorage.setItem('player', JSON.stringify(player))
    }
}


window.addEventListener("keydown", (e) => {
    console.log(e.code)
    switch (e.code) {
        case 'KeyS':
            player.y += player.speed;
            break;
        case 'KeyA':
            player.x - player.speed > 0 ? player.x -= player.speed : null;
            break;
        case 'KeyW':
            player.y - player.speed > 0 ? player.y -= player.speed : null;
            break;
        case 'KeyD':
            player.x += player.speed;
            break;
    }
    player.main.textContent = `x:${player.x} \n y:${player.y}`
    player.main.style.margin = `${player.y}px ${player.x}px`
})

