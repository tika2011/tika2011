   function changeColor() {
    document.getElementById("myParagraph").style.color = "blue";
  }
  function checkNumber() {
    var num = Number(document.getElementById("numberInput").value);
    if (num % 2 === 0) {
      console.log("This number is even.");
    } else {
      console.log("This number is odd.");
    }
  }
  function toggleParagraphs() {
    document.getElementById("para1").style.display = "none";
    document.getElementById("para2").style.display = "block";
  }
  function checkWord() {
    var word = document.getElementById("wordInput").value;
    if (word === "admin") {
      document.body.style.backgroundColor = "black";
    } else {
      document.body.style.backgroundColor = "pink";
    }
  }
  function askName() {
    var name = prompt("what your name?");
    alert("hallo, " + name + "!");
  }
  function askAge() {
    alert("hi");
    var age = prompt("how old are you");
    console.log("your age " + age);
  }