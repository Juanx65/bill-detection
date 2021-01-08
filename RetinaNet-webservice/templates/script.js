document.getElementById('btin').addEventListener("click",()=>{
	decir(document.getElementById("min").value);
});

function decir(texto){
	speechSynthesis.speak(new SpeechSynthesisUtterance(texto));
}