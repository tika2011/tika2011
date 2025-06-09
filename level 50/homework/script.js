
let example = "მაგალითი";
let title = document.getElementById("myTitle");
let paragraph = document.getElementById("myParagraph");

title.style.color = "darkblue";
title.style.fontSize = "36px";
title.style.fontFamily = "Georgia, serif";

paragraph.style.color = "darkgreen";
paragraph.style.fontSize = "20px";
paragraph.style.fontFamily = "Courier New, monospace";


console.log("სათაური ელემენტი:", title);
console.log("პარაგრაფი ელემენტი:", paragraph);

console.log("სათურის ფერი:", title.style.color);
console.log("პარაგრაფის ფონტი:", paragraph.style.fontFamily);
