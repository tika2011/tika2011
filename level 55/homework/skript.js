window.onload = function() {
    const a = 10;
    const b = 5;

    console.log("ჯამი:", a + b);
    console.log("გაყოფა:", a / b);
    console.log("გამრავლება:", a * b);
    console.log("განაყოფი:", a - b);
};
const button = document.getElementById("my-button");

button.addEventListener("click", function() {
    button.style.color = "white";
    button.style.backgroundColor = "green";
    button.style.borderRadius = "10px"; 
    button.style.width = "200px";
});
