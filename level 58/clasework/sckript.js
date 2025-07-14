    let name = prompt("Enter your name");
    alert("გამარჯობა, " + name);
    let adult = confirm("Are you over 18?");
    console.log("adult:", adult);
    function run() {
      let input = document.getElementById("text").value;
      console.log("Enter Text:", input);
      document.getElementById("result").innerText = input;
    }