// input animation

const inputs = document.querySelectorAll("input");

inputs.forEach(input => {

    input.addEventListener("focus", () => {
        input.style.boxShadow = "0 0 10px #00e5ff";
    });

    input.addEventListener("blur", () => {
        input.style.boxShadow = "none";
    });

});


// floating background animation
// INPUT GLOW ANIMATION



inputs.forEach(input => {

    input.addEventListener("focus", () => {
        input.style.boxShadow = "0 0 12px #00e5ff";
    });

    input.addEventListener("blur", () => {
        input.style.boxShadow = "none";
    });

});


// FLOATING BACKGROUND BUBBLES

const body = document.querySelector("body");

setInterval(()=>{

    const bubble = document.createElement("span");

    let size = Math.random() * 30 + 10;

    bubble.style.position = "absolute";
    bubble.style.width = size + "px";
    bubble.style.height = size + "px";
    bubble.style.background = "rgba(255,255,255,0.2)";
    bubble.style.borderRadius = "50%";

    bubble.style.left = Math.random() * window.innerWidth + "px";
    bubble.style.top = "100%";

    bubble.style.animation = "float 8s linear";

    body.appendChild(bubble);

    setTimeout(()=>{
        bubble.remove();
    },8000)

},400);