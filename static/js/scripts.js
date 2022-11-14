function handleClick(e){
	if (e.shiftKey) {
		console.log("screenX: " + e.screenX);
		console.log("screenY: " + e.screenY);
		console.log("clientX: " + e.clientX);
		console.log("clientY: " + e.clientY);
	}
}

const btn = document.getElementById("header");
btn.addEventListener("mouseover", (e) => e.target.style.backgroundColor = "red", true);
btn.addEventListener("mouseout", (e) => e.target.style.backgroundColor = "white", true);
btn.addEventListener("click", handleClick, true);

for(var i=0; i<searchForm.elements.length;i++)
    document.write(searchForm.elements[i].name + "<br/>");