const obj = document.getElementById('myCanvas')
const ctx = obj.getContext('2d')

const l = obj.offsetLeft;
const t = obj.offsetTop;

ctx.lineWidth = 20;
ctx.lineCap = "round";
ctx.strokeStyle = "white";

let prevX = 0;
let prevY = 0;
let isDrawing = 0;
obj.addEventListener("mousedown", (e)=>{
	isDrawing=1;
	prevX = e.clientX-l;
	prevY = e.clientY-t;
});

obj.addEventListener("mousemove", (e)=>{
    // console.log(e.clientX - obj.offsetLeft, e.clientY - obj.offsetTop)
	if(isDrawing){
		let x = e.clientX-l;
		let y = e.clientY-t;
		// console.log(prevX, prevY, x, y);
		ctx.beginPath();
		ctx.moveTo(prevX,prevY);
		ctx.lineTo(x,y);
		ctx.stroke();
		prevX = x;
		prevY = y;
	}
});

let data;
obj.addEventListener("mouseup", (e)=>{
	isDrawing=0;
    data = obj.toDataURL("image/jpeg");
    // console.log(data)
    let form = document.getElementById("myForm");
    let input = document.getElementById("myText");
    input.value = `${data}`
    // console.log(input.value)
    form.submit()
});

obj.addEventListener("mouseout", (e)=>{
	let prevX = 0;
	let prevY = 0;
	isDrawing = 0;
})

const first = document.querySelectorAll('.subcontainer')
function draw(o){
	    for(let i = 0; i < 10; i++){
	        let value = Math.round(o[i]);
	        let firsto = first[i];
	        let second = firsto.querySelectorAll('.subsubcontainer')
	        for(let j = 0; j < value; j++){
	        second[j].style.backgroundColor = "blue";
	    }
	}
}




