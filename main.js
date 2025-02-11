const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

canvas.width = 800;
canvas.height = 500;

// Car Object
let car = { x: 100, y: 400, width: 40, height: 60, speed: 5 };

function drawCar() {
    ctx.fillStyle = "red";
    ctx.fillRect(car.x, car.y, car.width, car.height);
}

// Car Movement
document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowUp") car.y -= car.speed;
    if (event.key === "ArrowDown") car.y += car.speed;
    if (event.key === "ArrowLeft") car.x -= car.speed;
    if (event.key === "ArrowRight") car.x += car.speed;
});

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawCar();
    requestAnimationFrame(gameLoop);
}

gameLoop();
